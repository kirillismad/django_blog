FROM python:3.7


ENV PYTHONUNBUFFERED 1

COPY src /src
COPY entrypoints /entrypoints

WORKDIR /src
RUN pip install --upgrade pip; \
    pip install -r requirements.txt && pip install gunicorn


ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait


RUN groupadd -r django_group && useradd -r -g django_group django; \
    chown django:django_group /wait && chmod +x /wait; \
    chown -R django:django_group /src; \
    mkdir /celery && chown -R django:django_group /celery

USER django

ENTRYPOINT ["/entrypoints/blog.sh"]

