# Agora-sp Admin

Agora-sp admin is an EmberJS project that provides an intuitive user interface for the [the agora-sp](https://github.com/grnet/agora-sp) project. It allows users to create/edit/update/delete their services and components. Users can login with credentials provided by the administrator, or use the shibboleth login functionality to login with their academic account.

### Get the code

Clone or download the repo.

```
git clone https://github.com/grnet/agora-sp-admin.git
```

### Dependencies

You need to have [NodeJS](https://nodejs.org/en/download/) and [Yarn](https://yarnpkg.com/en/docs/install) installed.

### Install requirements

You must first run `yarn` inside the project root directory to install depending libraries.


### Configuration

You should edit the `config/environment.js` file to set the default configuration options. You need to specify the location of your backend server and API (the backend server is [the agora-sp repo](https://github.com/grnet/agora-sp) as well as the media root url for the static files.

Example options:

```
var ENV = {
  appURL: 'https://example.com/api/v2/',
  APP: {
    backend_host: 'https://example.com/api/v2',
    backend_media_root: 'https://example.com/static/img/',
  }
}
```

### Development

If you want to make changes/update the code, you should run ember in development mode. You can do this by running:

```
./node_modules/.bin/ember serve
```

and then visit your app at [http://localhost:4200](http://localhost:4200).

Ember then will watch for updates in your code and reload the files automatically.

### Production

In order to deliver the UI, you need to run ember in build mode. You can do this by running:

```
./node_modules/.bin/ember build
```

This will create a `dist` directory inside the project root directory, so you can serve it to deliver the UI.

# Copyright and license

Copyright (C) 2017-2018 GRNET S.A.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).
