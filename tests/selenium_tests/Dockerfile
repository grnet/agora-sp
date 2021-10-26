FROM python:3.7.12-bullseye

ADD requirements.txt /srv/agora/tests/selenium_tests/requirements.txt

WORKDIR /srv/agora/tests/selenium_tests/

RUN pip install -r requirements.txt

CMD pytest agora_unit_tests.py -o junit_family=xunit2 --junitxml=reports/junit.xml

