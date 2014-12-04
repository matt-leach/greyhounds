#!/bin/bash

project_name=greyhounds
website=greyhounds.familyleach.net

source ../bin/activate

./setup_nginx.sh $project_name $website
./setup_supervisor.sh $project_name
pip install -r pip_requirements.txt

mkdir -p ../logs

touch ../logs/gunicorn_supervisor.log

supervisorctl reread
supervisorctl update
supervisorctl restart $project_name

service nginx restart