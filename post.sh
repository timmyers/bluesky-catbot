#!/usr/bin/env bash
# set -e

while true; do
  python main.py
  node index.js
  sleep 600 # pause for 1 hour (3600 seconds)
done