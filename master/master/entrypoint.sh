#!/bin/bash
sed -i "s/CHANGEME/`hostname`/" /master/master_config.yson
exec ytserver-master --config /master/master_config.yson
