#!/usr/bin/env bash
set -e
cd $(dirname "$0")
echo "working directory $(pwd)"

log_file='finetune.log'
rm $log_file || true
touch $log_file

nohup papermill ds_finetune.ipynb ds_finetune_output.ipynb > $log_file 2>&1 &
echo "ds finetune pipeline running"