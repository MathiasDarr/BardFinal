FROM python:3.8-buster

WORKDIR /usr/src/app

RUN groupadd -g 1000 -r app && useradd -m -u 1000 -s /bin/false -g app app

COPY requirements.txt ./

COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt


ADD . .
RUN pip install .

CMD gunicorn --workers 2 --timeout 300 --bind 0.0.0.0:5000 --access-logfile - wsgi:application --reload