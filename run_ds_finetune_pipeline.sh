#!/usr/bin/env bash
set -e
cd $(dirname "$0")
echo "working directory $(pwd)"

log_file='finetune.log'
rm $log_file || true
touch $log_file

nohup jupyter nbconvert --execute --to notebook --inplace ds_finetune.ipynb > $log_file 2>&1 &
echo "ds finetune pipeline running"

