FROM python:3.7.2-stretch

LABEL maintainer="audrius@tapke.eu"
LABEL version="0.1"
LABEL url="https://github.com/audriusb/fibo_sequence_sample_project"


ADD ./run.sh /

RUN groupadd -r django && useradd -r -g django django
RUN mkdir -p /app 

WORKDIR /app

ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

RUN chown -R django:django /app

USER django:django

ADD ./fibonacci /app/fibonacci
ADD ./manage.py /app/

RUN python manage.py test

EXPOSE 8000

CMD ["/bin/sh", "-c", "/run.sh"]