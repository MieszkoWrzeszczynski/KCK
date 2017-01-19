#!/bin/bash
env="source ~/.virtualenvs/arcade/bin/activate"
eval $env
echo `date` >> program_output.log
cmd="(python3 App.py 2>&1  | tee -a program_output.log) || rm -f app_resources/bot_resources/bot* "
eval $cmd