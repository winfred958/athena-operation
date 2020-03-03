#!/bin/bash

PROJECT_ROOT_PATH=$(cd "$(dirname "$0")"; cd ..; cd athena-operation/;pwd)

source "${PROJECT_ROOT_PATH}/config/env.sh"

echo -e "${PROJECT_ROOT_PATH}/athena-operation/athena_opertation.py \\\n${*}"
python3 "${PROJECT_ROOT_PATH}/athena-operation/athena_opertation.py" "${*}"