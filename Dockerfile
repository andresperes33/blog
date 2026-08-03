FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /blog

# Install system dependencies for building psycopg2 and other packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /blog/
RUN pip install --no-cache-dir -r requirements.txt

# Variáveis de ambiente passadas pelo EasyPanel como build-args.
# Necessárias em tempo de build (collectstatic exige SECRET_KEY).
ARG SECRET_KEY
ARG DEBUG
ARG ALLOWED_HOSTS
ARG CSRF_TRUSTED_ORIGINS
ARG DATABASE_URL

ENV SECRET_KEY=$SECRET_KEY \
    DEBUG=$DEBUG \
    ALLOWED_HOSTS=$ALLOWED_HOSTS \
    CSRF_TRUSTED_ORIGINS=$CSRF_TRUSTED_ORIGINS \
    DATABASE_URL=$DATABASE_URL

COPY . /blog/

# collectstatic nao deve depender do banco de producao nem exigir psycopg2 no build
RUN DATABASE_URL="sqlite:////tmp/build.db" python manage.py collectstatic --noinput

EXPOSE 8000

CMD sh -c "python manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 config.wsgi:application"
