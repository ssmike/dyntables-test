#!/bin/bash

# usage: [PATH_TO_TABLE]

ytserver-proxy --config /control/proxy_config.yson &
sleep 1

/control/create-table.py $1
