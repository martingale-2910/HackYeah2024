if [[ -n "${CMD}" ]];
then
    python3 -m main ${CMD} ${CMD_ARGS}
else
    echo "No CLI command provided, exiting"
    exit 1
fi