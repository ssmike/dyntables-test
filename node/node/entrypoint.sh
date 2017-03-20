#!/bin/bash
sed -i "s/CHANGEME/`hostname`/" /node/node_config.yson
service ssh start
tail 2>/dev/null -f /log #run forever
