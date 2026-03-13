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

COPY . /blog/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD sh -c "python manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 config.wsgi:application"
