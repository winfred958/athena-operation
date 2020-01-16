#!/bin/bash

PROJECT_ROOT_PATH=$(cd "$(dirname "$0")"; cd ..; cd athena-operation/;pwd)

source "${PROJECT_ROOT_PATH}/config/env.sh"

python3 "${PROJECT_ROOT_PATH}/athena-operation/athena_opertation.py" ${*}