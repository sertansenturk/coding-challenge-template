#!/bin/bash
set -e # Any subsequent commands which fail will cause the shell script to exit immediately

black src tests setup.py
