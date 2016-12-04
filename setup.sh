#!/bin/bash

env="source ~/.virtualenvs/arcade/bin/activate"
eval $env
echo `date` >> program_output.log
cmd="python3 App.py || rm -f app_resources/bot_resources/bot* | tee -a program_output.log "
eval $cmd