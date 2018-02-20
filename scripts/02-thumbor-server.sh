#!/usr/bin/env bash
cd `dirname "$0"`
../thumbor-redis-pubsub/runner.py \
  -c ../config/thumbor-conf.py \
  -l debug
