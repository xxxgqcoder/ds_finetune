#!/usr/bin/env bash
set -e
cd $(dirname "$0")
echo "working directory $(pwd)"

# install dependence
apt-get update

apt-get install -y build-essential git-all

pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple unsloth datasets huggingface-hub transformers
