#!/bin/bash
docker build -t chunk-read-file . && docker run \
--network="host" --interactive --tty --rm \
--volume=./sample.csv:/data/sample.csv chunk-read-file