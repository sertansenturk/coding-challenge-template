#!/bin/bash
set -e # Any subsequent commands which fail will cause the shell script to exit immediately

pip install -r requirements.txt

pip install .
python -m pytest -W ignore::DeprecationWarning --log-cli-level=INFO
