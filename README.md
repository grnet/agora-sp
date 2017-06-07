# Service Portfolio Management Tool
The service portfolio management tool is a tool that allows a company / project to manage the portfolio of services they to maintain (offered to users / customers or internal). 
The document describes the requirements, design, model and technologies used for the current implementation of the SPMT. SPMT is used in the context of two projects. The VI-SEEM service catalogue and the EUDAT2020 service catalogue. 
URLs of the instances are provided below:
 
### VI-SEEM

**Service Catalogue:** 

```
https://services.vi-seem.eu/
```

**Service Portfolio (need login credentials):** 

```
https://services.vi-seem.eu/ui/portfolio/services/
```

**API:** 

```
https://services.vi-seem.eu/api/v1/portfolio/services
```

**API DOC:** 

```
https://services.vi-seem.eu/api/docs
``` 
 
### EUDAT

**Service Catalogue:** 

```
https://sp.eudat.eu/
```

**Service Portfolio (need login credentials):** 

```
https://sp.eudat.eu/ui/portfolio/services/
```

**API:** 

```
https://sp.eudat.eu/api/v1/portfolio/services
```

**API DOC:** 

```
https://sp.eudat.eu/api/docs
```
 
**Source Code** 

```
https://code.vi-seem.eu/stdario/agora **BRANCH:** eudat
```

**Access:** 
To get access try to apply with VI-SEEM Login and it will be arranged


# Installation guide for Agora project

## Getting started

This installation guide requires the following prerequisites:

- Debian OS
- User with sudo privileges
- Python 2.7.9
- [pip](https://packaging.python.org/installing/)
- [Virtual Environments](https://virtualenvwrapper.readthedocs.io/en/latest/)

## Get the code

Since it is a security risk to add ssh keys in a vm in order to clone a private repo, you can use the local git clone on your machine to push the code to the vm.

- Inside the vm, create a directory inside the home folder, e.g. `mkdir agora && cd agora` (e.g. in `/home/<user>/agora`, and run `git init`.
- On your host machine, first run `git clone git@code.vi-seem.eu:stdario/agora.git && cd agora` to get the code, then use the command `git remote add <name> <user@vm-name>:<path-to-vm-git-directory>` (e.g. `git remote add vm me@vm-ip:/home/<user>/agora`) to add the remote vm in your local git repo and then `git push <name> <branch-name>` to upload the code.

Alternatively, you can use ssh/https to clone the code inside the vm, more information [here](https://code.vi-seem.eu/stdario/agora)

## Database

This project is set up to use a mysql database. The credentials are inside `agora/settings.py`.

```
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'agora',
		'USER': 'root',
		'PASSWORD': 'anex',
		'HOST': '127.0.0.1'
	}
}
```

It also requires a database with name `agora` to be created.

- Run `mysql -u<username> -p<password>` in order to connect to the mysql db
- Run `create database agora;` in order to create a new and empty database named `agora`

All the tables will be created from the django migrations.

## Requirements

The following packages are required for this project to work. You can install them with the following command:

```
apt-get install python mysql-server mysql-client libmysqlclient-dev build-essential libssl-dev libffi-dev python-dev apache2 apache2-doc apache2-utils
```

You should have pip installed, if not you can find documentation [here](https://packaging.python.org/installing/)

You should have virtualenvwrapper installed, if not you can find documentation [here](https://virtualenvwrapper.readthedocs.io/en/latest/)

## Installation

Create a new virtual environment by running `mkvirtualenv agora`

Inside the project directory, run `pip install -r requirements.txt --no-cache-dir` to install all the required python packages (the requirements.txt is in the root directory of the project)

To run the databse migrations, run the command `python manage.py migrate` to update the database.

### URL Configuration

This application uses a lot of links to local and external resources within its response structures. In order to consistently construct links in various deployment environments, do the following steps:

- Add the url which will host the data to the `sites.json` file. Example:

```
{
	"model": "sites.site", 
	"pk": 1, 
	"fields": {
		"domain": "localhost", 
		"name": "Local development url"
	}
}
```

- Edit the `agora/settings.py` file and add the domain inside the `ALLOWED_HOSTS` list

- Run `python manage.py loaddata sites.json`

## Apache configuration

In order for apache to be able to serve the project, WSGI must be enabled.
Edit the file `/etc/apache2/apache2.conf` and insert the following in the bottom of the file, updating the correct file paths and domain names:

```
WSGIPythonPath <path-to-root-project-dir>:<path-to-venv>/lib/python2.7/site-packages

NameVirtualHost 83.212.105.109:80
<VirtualHost *:80>

        ServerName 83.212.105.109
        Alias /static/ <path-to-root-project-dir>/static/

        <Directory <path-to-root-project-dir>/static>
            Order deny,allow
            Allow from all
            Require all granted
        </Directory>

        <Directory <path-to-root-project-dir>/agora>
            Order deny,allow
            Allow from all
            Require all granted
        </Directory>

        <Directory <path-to-root-project-dir>/agora>
        <Files wsgi.py>
            Order deny,allow
            Allow from all
            Require all granted
        </Files>
        </Directory>

        WSGIScriptAlias / <path-to-root-project-dir>/agora/wsgi.py
</VirtualHost>
```

**NOTE**

In order for apache to be able o write logs, you should give permissions to apache in order to write the logs. Inside the root directory of the project, run `chmod -R 777 logs`.

## Run the project

If all the above steps are done, just restart your apache server using the command `service apache2 restart` and go to the vm ip and you're ready!

## SAML2 Integration

Because for some reason the library that we use for SAML integration uses the HTTP-POST binding by default with the SSO we had to hardcode the HTTP-REDIRECT binding.
In order to do this you need to change the:

`<path-to-virtualenv>/lib/python2.7/dist-packages/saml2/client_base.py`

on line 139 add:

`binding=BINDING_HTTP_REDIRECT`

to hardcode the BINDING we need.

### sp.eudat.eu specific saml mods

We strongly advise not to update the SAML2 package on this instance as it may lead to other problems with B2ACCESS specific settings. Open the file:

`<path-to-virtualenv>/lib/python2.7/dist-packages/djangosaml2/backends.py`

This is some code we added to the SAML2 library to avoid the double transaction problem with the user creation.

```
# This was added by Gjorgji Strezoski to circumvent the signal transaction integrity issue.        

            message = 'THIS IS AN AUTOMATIC EMAIL NOTIFICATION \n\n\nA new user has been created in the Agora app with B2ACCESS on sp.eudat.eu!\n\n'+\
                          'Username: ' + session_info['ava']['userName'][0]+\
                          '\nName: ' + session_info['ava']['cn'][0]+\
                          '\nEmail: ' + session_info['ava']['mail'][0]+\
                          '\nOrganization: '+ session_info['ava']['o'][0]

            first_name = session_info['ava']['cn'][0].split(' ')[0]
            last_name = ' '.join(session_info['ava']['cn'][0].split(' ')[1:])

            session_info['ava']['cn'][0] = first_name
            session_info['ava']['dn'][0] = last_name

            if created:
                    send_mail(
                        '[AGORA][sp.eudat.eu] A new user has been created with B2ACCESS!',
                        message,
                        'agora.notification@gmail.com',
                        ['strezoski.g@gmail.com', 'iliaboti@grnet.gr', 'stojanovski.dario@gmail.com'],
                        fail_silently=False,
                        )
```

### sp.eudat.eu specific saml mod 2 (Email notification on failed login)

We strongly advise not to update the SAML2 package on this instance as it may lead to other problems with B2ACCESS specific settings. Open the file:

`<path-to-virtualenv>/lib/python2.7/dist-packages/djangosaml2/views.py`

Add the following code:

```
    try:
        user = auth.authenticate(session_info=session_info,
                             attribute_mapping=attribute_mapping,
                             create_unknown_user=create_unknown_user)
        if user is None:
            print(session_info)
            logger.error('The user is None')
            return HttpResponseForbidden(str(session_info))
    except Exception as e:

       message = 'ERROR with login with  B2CCESS on sp.eudat.eu!\n\n\n'+\
                          'Username: ' + session_info['ava']['userName'][0]+\
                          '\nName: ' + session_info['ava']['cn'][0]+\
                          '\nEmail: ' + session_info['ava']['mail'][0]+\
                          '\nOrganization: '+ session_info['ava']['o'][0]+\
                          '\n\n\nException data: \n\n' + str(e)

       send_mail(
                  '[AGORA][sp.eudat.eu] ERROR from login with B2ACCESS!',
                  message,
                  'agora.notification@gmail.com',
                  ['strezoski.g@gmail.com', 'iliaboti@grnet.gr', 'stojanovski.dario@gmail.com'],
                  fail_silently=False,
                  )
       return HttpResponseForbidden()
```