FROM node:8

ADD . /srv/agora/ui
WORKDIR /srv/agora/ui

RUN yarn install --non-interactive
CMD ./node_modules/.bin/ember build --watch
