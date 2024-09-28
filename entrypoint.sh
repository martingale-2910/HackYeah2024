set -x
set -e

if [[ -n "${CMD}" ]];
then
    python3 -m hackyeah2024.main ${CMD} ${CMD_ARGS}
else
    echo "No CLI command provided, running Dash server"
    python3 -m "hackyeah2024.main" run-server dash
fi