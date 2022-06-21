#!/bin/bash
set -e # Any subsequent commands which fail will cause the shell script to exit immediately

flake8 src/challenge_template --per-file-ignores='*/__init__.py:F401' --max-line-length 88
pylint --fail-under 8.00 src/challenge_template  # keep --fail-under relatively low; we are not purists
