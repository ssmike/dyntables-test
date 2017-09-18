#!/usr/bin/env python2
from __future__ import print_function
import yt.yson as yson
import yt.wrapper as yt
import sys
import os
import time

TABLE_PATH=sys.argv[1]
raw_config = open(os.environ['YT_DRIVER_CONFIG_PATH']).read()
yt.config = yson.loads(raw_config)

def yt_key(x):
    return {0:2, 1:21, 2:31, 3:41, 4:51}[x]

def wait_for_yt():
    toBreak = False
    while not toBreak:
        toBreak = True
        try:
            yt.get('/')
        except Exception as e:
            toBreak = False
            time.sleep(2)

def init_table():
    while True:
        try:
            yt.insert_rows(TABLE_PATH, [dict(key=yt_key(i), value=1)
                                             for i in range(5)])
            break
        except Exception as e:
            eprint(e)


def mount_table():
    try:
        if yt.get("//sys/tablet_cells/@count") == 0:
            for i in range(5):
                yt.create("tablet_cell", attributes={"replication_factor": 3,
                                                     "read_quorum":2,
                                                     "write_quorum":2})
        yt.remove(TABLE_PATH, force=True)
        schema = yson.loads("<strict=%true; unique_keys=%true>[{name=key;\
                                type=int64; sort_order=ascending}; {name=value; type=int64}]")
        yt.create_table(TABLE_PATH, attributes={"dynamic": True, "schema": schema})
        yt.reshard_table(TABLE_PATH, pivot_keys=[[], [20], [30], [40], [50]])
    except Exception as e:
        eprint(e)
    while yt.get(TABLE_PATH + "/@tablet_state") != "mounted":
        try:
            yt.mount_table(TABLE_PATH)
        except Exception as e:
            eprint(e)
    init_table()

if __name__ == "__main__":
    mount_table()
