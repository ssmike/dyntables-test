#!/bin/bash
rm -f /node/node.log
rm -f /node/node.debug.log
ytserver-node --config /node/node_config.yson 2>/node/log 1>&2 &
echo $! > /pid
