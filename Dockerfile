FROM python

RUN apt-get update
RUN	apt-get install -y virtualenv
RUN	mkdir /opt/unittest

COPY . /opt/unittest/
WORKDIR opt/unittest/

RUN virtualenv venv
RUN	. venv/bin/activate
RUN	pip install -r requirements.txt

ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0