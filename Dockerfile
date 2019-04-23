FROM python:3.7

RUN groupadd -r django_group && useradd -r -g django_group django
ENV PYTHONUNBUFFERED 1

COPY src /src
COPY entrypoint.sh /
WORKDIR /src

RUN pip install -r requirements.txt && pip install gunicorn

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chown django:django_group /wait && chmod +x /wait

USER django

CMD ["/entrypoint.sh"]

