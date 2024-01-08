#!/bin/bash -x

source /home/flhtek/github/pyopencwa/venv/bin/activate
cd /home/flhtek/github/pyopencwa
python src/cwagent/entrypoints/cli.py daemon-start

