#!/bin/bash
sed -i "s/CHANGEME/`hostname`/" /master/master_config.yson
service ssh start
tail -f /master/log #run forever
