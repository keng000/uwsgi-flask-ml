FROM python:3.7-slim

RUN apt-get update && \
    apt-get install --no-install-recommends -yq build-essential
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY myapp /var/www/myapp
ENV PYTHONPATH="$PYTHONPATH:/var/www"
ENTRYPOINT ["uwsgi", "--ini", "/var/www/myapp/config/myapp.ini"]