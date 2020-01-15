#!/bin/bash

PROJECT_ROOT_PATH=$(cd "$(dirname "$0")"; cd ..; pwd)
export PYTHONPATH=${PROJECT_ROOT_PATH}:$PYTHONPATH