#!/bin/sh
echo "Execution is being started"
echo "**************************"
pytest $@
echo "**************************"
echo "Execution has been completed, please check the artifacts to download the results."
