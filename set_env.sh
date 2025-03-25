#!/usr/bin/env bash
set -e
cd $(dirname "$0")
echo "working directory $(pwd)"

# install build enssentials
apt-get install build-essential