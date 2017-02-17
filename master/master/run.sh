#!/bin/bash
rm -f /master/master.log
rm -f /master/master.debug.log
ytserver-master --config /master/master_config.yson 2>/master/log 1>&2 &
echo $! > /pid
