FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=blog.settings.prod
ENV APP_USER=app
ENV APP_GROUP=app_group
ENV APP_DIR=/app
ENV SRC_DIR=${APP_DIR}/src
ENV SHARED_DIR=${APP_DIR}/shared
ENV STATIC_ROOT=${SHARED_DIR}/static_root
ENV MEDIA_ROOT=${SHARED_DIR}/media_root
ENV LOG_DIR=${SHARED_DIR}/logs


COPY src/requirements.txt .
COPY src/requirements.prod.txt .
COPY data/media_root ${MEDIA_ROOT}

RUN apk update \
    && apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    && apk add --no-cache \
    postgresql-dev \
    gettext \
    jpeg-dev \
    zlib-dev \
    libmemcached-dev \
    && pip install --no-cache-dir --disable-pip-version-check --requirement requirements.txt \
    && pip install --no-cache-dir --disable-pip-version-check --requirement requirements.prod.txt \
    && apk del .build-deps

COPY src ${SRC_DIR}

RUN addgroup \
    --system \
    ${APP_GROUP} \
    && adduser \
    --system \
    --home /app \
    --disabled-password \
    --no-create-home \
    --shell /bin/sh \
    --uid 5000 \
    ${APP_USER} ${APP_GROUP} \
    && mkdir -p ${STATIC_ROOT} ${MEDIA_ROOT} ${LOG_DIR} \
    && chown -R ${APP_USER}:${APP_GROUP} ${APP_DIR}


COPY /entrypoints/blog.sh .

WORKDIR ${SRC_DIR}

EXPOSE 8000

USER ${APP_USER}

ENTRYPOINT ["/blog.sh"]

