#! /usr/bin/env bash

set -x
set -e

if [[ -n "${CMD}" ]];
then
    python3 -m hackyeah2024.main ${CMD} ${CMD_ARGS}
else
    echo "No CLI command provided, running Streamlit server"
    python3 -m streamlit run hackyeah2024/server.py
fi
