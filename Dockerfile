FROM python:3.10

ENV PYTHONUNBUFFERED 1

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.62/linux64/chromedriver-linux64.zip
RUN unzip -j /tmp/chromedriver.zip chromedriver-linux64/chromedriver -d /bin

# set display port to avoid crash
ENV DISPLAY=:99

RUN mkdir /code
WORKDIR /code

COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh


ENTRYPOINT [ "/entrypoint.sh" ]
