FROM python:2

ADD requirements.txt /srv/agora/requirements.txt
ADD requirements_dev.txt /srv/agora/requirements_dev.txt
WORKDIR /srv/agora
RUN pip install -r requirements_dev.txt

RUN mkdir -p /tmp/agora/agora_emails
RUN mkdir /etc/agora

COPY ./agora/docker/* /etc/agora/

ADD ./agora /srv/agora/agora

WORKDIR /srv/agora/agora

CMD python manage.py migrate &&  python manage.py loaddata fixtures/users.json && \
    python manage.py runserver 0.0.0.0:80
