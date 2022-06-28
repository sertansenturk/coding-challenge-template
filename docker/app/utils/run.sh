#!/bin/bash
set -e # Any subsequent commands which fail will cause the shell script to exit immediately

ct --config ./docker/app/config.yaml --key1 value1 run_all
