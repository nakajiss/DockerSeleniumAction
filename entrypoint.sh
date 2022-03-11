#!/bin/sh
pip install --upgrade pip
pip install --no-cache allure-pytest==2.9.45
pip install --no-cache pytest==7.0.1
pip install --no-cache selenium==4.1.2
echo "Execution is being started"
echo "**************************"
for f in $@*.py; do
  pytest "$f" --alluredir=results
done
echo "**************************"
echo "Execution has been completed, please check the artifacts to download the results."
