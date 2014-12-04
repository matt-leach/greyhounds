#!/bin/bash

project_name=$1



conf_file=/etc/supervisor/conf.d/$project_name.conf
conf_file=~/workspace/test.conf


THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
GUNICORNFILE=$THIS_DIR/gunicorn_start.sh           
LOGFILE=$THIS_DIR/../logs/gunicorn_supervisor.log



echo "[program:$project_name]" > $conf_file
echo "command = $GUNICORNFILE $project_name" >> $conf_file
echo "user = root" >> $conf_file
echo "stdout_logfile = $LOGFILE" >> $conf_file
echo "redirect_stderr = true" >> $conf_file


