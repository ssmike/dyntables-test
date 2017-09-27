#!/usr/bin/env python2
from __future__ import print_function
import yt.yson as yson
import yt.wrapper as yt
import sys
import os
import time
import json

TABLE_PATH=sys.argv[1]
YT_STATE=json.loads(sys.argv[2])
YT_SHARDS=json.loads(sys.argv[3])

raw_config = open(os.environ['YT_DRIVER_CONFIG_PATH']).read()
yt.config = yson.loads(raw_config)

def retry(f):
    while True:
        try:
            return f()
        except Exception as e:
            print(e)
            time.sleep(1)

def wait_for_yt():
    retry(lambda: yt.get('/'))

def init_table():
    retry(lambda: yt.insert_rows(TABLE_PATH, [dict(key=int(k), value=v) for k, v in YT_STATE.items()]))

def mount_table():
    if retry(lambda: yt.get("//sys/tablet_cells/@count")) == 0:
        for i in range(5):
            retry(lambda: yt.create("tablet_cell", attributes={"replication_factor": 3,
                                                 "read_quorum":2,
                                                 "write_quorum":2}))
    retry(lambda: yt.remove(TABLE_PATH, force=True))
    schema = yson.loads("<strict=%true; unique_keys=%true>[{name=key;\
                            type=int64; sort_order=ascending}; {name=value; type=int64}]")
    retry(lambda: yt.create_table(TABLE_PATH, attributes={"dynamic": True, "schema": schema}))
    retry(lambda: yt.reshard_table(TABLE_PATH, pivot_keys=YT_SHARDS))

    while retry(lambda: yt.get(TABLE_PATH + "/@tablet_state")) != "mounted":
        try:
            yt.mount_table(TABLE_PATH)
        except Exception as e:
            print(e, file=sys.stderr)
    init_table()

if __name__ == "__main__":
    wait_for_yt()
    mount_table()
