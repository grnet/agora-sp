FROM python:2

ADD requirements.txt /srv/agora/requirements.txt
ADD requirements_dev.txt /srv/agora/requirements_dev.txt
WORKDIR /srv/agora
RUN pip install -r requirements_dev.txt

RUN mkdir -p /tmp/agora/agora_emails
RUN mkdir /etc/agora

COPY ./agora/docker/* /etc/agora/

RUN mkdir -p /srv/agora/agora/logs/
RUN touch /srv/agora/agora/logs/debug.log

ADD ./agora /srv/agora/agora

WORKDIR /srv/agora/agora
RUN python manage.py migrate

RUN echo "from accounts.models import User; User.objects.create_superuser('superadmin', 'superadmin@synnefo.org', '12345', role='superadmin')" | python manage.py shell
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
