# Agora

The service portfolio management tool is a tool that allows a company / project to manage the portfolio of services they to maintain (offered to users / customers or internal).

### Dependencies

* [git](https://git-scm.com/)
* [virualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
* [pip](https://pypi.python.org/pypi/pip)

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

With virtualenv activated install dependencies

```
pip install -r requirements.txt
```

## Configuration

### Create configuration files

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

You should override it with your database settings, [you can read more information here](https://docs.djangoproject.com/en/1.9/ref/databases/).

**NOTE:** You must create a `log` folder containing a `debug.log` file in your base project directory or configure LOGGING setting with custom log options.

Finally, you should also create a `deployment.conf` file which should specify the `root_url` attribute to reflect the url of the backend server.

The default location of `deployment.conf` is in '/etc/agora/`.

Example: 

```
{
    ":root_url": "localhost"
}
```


### Migrations

Run all migrations in order to construct the database schema.

You should run:

```
python manage.py migrate
```

Once migrations finish, you can run `python manage.py runserver` to test that the application is installed properly.


You can now view your application in `http://127.0.0.1:8000/`



# Copyright and license


Copyright (C) 2017-2018 GRNET S.A.

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
