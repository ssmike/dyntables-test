#!/bin/bash
ytserver-master --config /master/master_config.yson 2>/master/log 1>&2 &
echo $! > /pid
