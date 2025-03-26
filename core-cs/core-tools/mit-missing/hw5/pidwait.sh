#!/usr/bin/env bash

while true; do
  if kill -0 $1 2>/dev/null; then
    sleep 1
  else
    echo "Child process has finished"
    break
  fi
done
