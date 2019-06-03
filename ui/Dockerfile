FROM node:8

RUN npm install --global yarn

ADD . /srv/agora/ui
WORKDIR /srv/agora/ui

RUN yarn install --non-interactive
CMD ./node_modules/.bin/ember serve
