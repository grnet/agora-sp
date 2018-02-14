FROM python:2

ADD . /srv/agora
WORKDIR /srv/agora

RUN mkdir -p /tmp/agora/agora_emails
RUN mkdir /etc/agora

COPY docker/settings.conf /etc/agora/

RUN pip install -r requirements.txt

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
RUN echo "from accounts.models import User; User.objects.create_superuser('superadmin', 'superadmin@synnefo.org', '12345', role='superadmin')" | python manage.py shell
