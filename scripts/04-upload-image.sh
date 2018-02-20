#!/usr/bin/env bash
cd `dirname "$0"`
curl \
  -v \
  -F "media=@../config/logo-thumbor.png" \
  http://localhost:8888/image
