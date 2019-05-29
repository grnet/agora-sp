# Agora

The service portfolio management tool is a tool that allows a company / project to manage the portfolio of services they to maintain (offered to users / customers or internal).
Agora provides an intuitive user interface which allows users to create/edit/update/delete their services and components. Users can login with credentials provided by the administrator, or use the shibboleth login functionality to login with their academic account.


### Dependencies

* [git](https://git-scm.com/)
* [virualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
* [pip](https://pypi.python.org/pypi/pip)
* [NodeJS](https://nodejs.org/en/download/)
* [Yarn](https://yarnpkg.com/en/docs/install)


## Development instructions

### Get the code

```
git clone https://github.com/grnet/agora-sp.git
```

### Create a virtualenv for agora

```
cd agora
mkvirtualenv agora
```

### Install requirements

With virtualenv activated install python dependencies:

```
pip install -r requirements.txt
```

Then run `yarn` inside the `ui` directory to install npm depending libraries.

## Configuration

### Backend configuration

You can create a configuration file in order to override the default settings for the agora project. The default location of the .conf file is `/etc/agora/settings.conf`

The default contents of `settings.conf` are:

```
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.agora.sqlite3'
    }
}

DATABASES = SQLITE
EMAIL_FILE_PATH = '/tmp/agora/agora_emails'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
```

You should override it with your database settings, [you can read more information here](https://docs.djangoproject.com/en/1.11/ref/databases/).


**NOTE:** You must create a `log` folder containing a `debug.log` file in your base project directory or configure LOGGING setting with custom log options.


Finally, you should also create a `deployment.conf` file which should specify the `root_url` attribute to reflect the url of the backend server.

The default location of `deployment.conf` is in '/etc/agora/`.

Example: 

```
{
    ":root_url": "localhost"
}
```


### UI configuration

You can edit the `ui/config/environment.js` file to set the default configuration options. You can alter the value of `rootURL` and `appURL` that define where the ui is served and what is the main endpoint  where the backend is located.

Example options:

```
var ENV = {
  rootURL: '/ui/'
  appURL: 'api/v2/',
}
```

### UI Customization

You can customize the appearance of your installation by adding your own logo, style and domestic login method text.

You can place your own logo inside `public/assets` directory under the name `logo.png`.
You can also use a custom preprocessed stylesheet, which you should place inside `styles` folder.
In order to process it and import it, you have to edit `ui/config/environment.js` file and set the `theme` option to match the name of the stylesheet `my-themes.scss`:

```
var ENV = {
    theme: 'my-theme',
}
```

In case you want to alter the text for domestic login method, you can change the configuration option in `config/environment.js` as follows:

```
var ENV = {
  APP: {
    domestic_login_msg: "My login method"
  }
}

```

### Migrations

Run all migrations in order to construct the database schema.

You should run:

```
python manage.py migrate
```


### Development

Serve ui files by running the command from inside `ui/` directory:

```
./node_modules/.bin/ember build
```

This will create a `dist` , that will be served by Agora to deliver the UI.

Finally, run `python manage.py runserver` to test that the application is installed properly.

You can now view your application in `http://127.0.0.1:8000/`



# Copyright and license


Copyright (C) 2017-2019 GRNET S.A.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see [http://www.gnu.org/licenses/]([http://www.gnu.org/licenses/).
