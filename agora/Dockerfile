FROM python:2.7.15


RUN git clone -b devel https://github.com/grnet/agora-sp.git /home/agora-sp
RUN mkdir /etc/agora && \
    mkdir -p /tmp/agora/agora_emails && \
    mkdir -p /srv/agora && \
    cp /home/agora-sp/requirements_dev.txt /srv/agora/requirements_dev.txt && \
    cp /home/agora-sp/requirements.txt /srv/agora/requirements.txt && \
    cp /home/agora-sp/version /srv/agora/version && \
    cp -r /home/agora-sp/agora/docker/* /etc/agora/ && \
    cp -r /home/agora-sp/agora /srv/agora/agora && \
    cd /srv/agora && pip install -r requirements_dev.txt

WORKDIR /srv/agora/agora

RUN python manage.py migrate && ./populate_db.sh && \
    python manage.py loaddata fixtures/sample-providers.json && \
    python manage.py loaddata fixtures/sample-users.json && \
    python manage.py loaddata fixtures/sample-contactInformations.yaml && \
    python manage.py loaddata fixtures/sample-resources.yaml

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

