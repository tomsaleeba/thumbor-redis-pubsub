#!/usr/bin/env bash
docker run \
  --name some-redis \
  --rm \
  -p 6379:6379 \
  redis
