#!/bin/sh
pip install --upgrade pip
pip install --no-cache pytest
pip install --no-cache termcolor
pip install --no-cache selenium==4.9
pip install --no-cache pytest-selenium
pip install --no-cache allure-python-commons
echo "Execution is being started"
echo "**************************"

python3 -m pytest -v -s --driver Chrome --driver-path /bin/chromedriver $@ &> output.log
if output.log grep -q 'failed'; then
  exit 1
fi

echo "**************************"
echo "Execution has been completed, please check the artifacts to download the results."
