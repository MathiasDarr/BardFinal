FROM python:3.9

RUN pip install -U pip setuptools
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - \
&& apt-get update \
&& apt-get install -y nodejs make groff jq gettext-base vim less curl grep groff-base unzip zip \
&& apt-get clean

RUN npm install -g aws-cdk

COPY  requirements.txt ./
RUN pip install -r requirements.txt



COPY docker/aws-cli-installer.sh /usr/local/bin
RUN /usr/local/bin/aws-cli-installer.sh
COPY app.py cdk.json userdata.sh deploy.sh  ./
COPY deployment_stack ./deployment_stack
