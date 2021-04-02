# Agora accounting ui

Agora accounting is a single page front-end application built with react (and create-react-app tool) that displays the following data based on a specific time range for an agora instance:
- new users
- new/updated providers
- new/updated resources

## Configuration

In `agora/src/config.js` there are some basic configuration properties to be set before producing the optimized build. The properties that can be set are as follows:
- `endpoint: "http://localhost:8000`
  Defines the agora api endpoint
- `supportMail: agora@grnet.gr`
  Defines the support mail to show in the accounting page


## Build and deploy

Steps to build and deploy the app:

1. git clone this repo and go to accounting directory `cd agora/accounting`
2. Issue `npm install` 
3. Configure parameters in `./src/config.js`
4. Issue `npm run build`
5. Deploy contents of the `./build/` folder to the remote webserver

## Deploy on a specific subfolder - for example under https://demo.agora.grnet.gr/accounting
If the app is meant to be deployed under a subfolder on the remote node make sure that:
1. endpoint parameter (in `./src/config.js`) is set to the main url
~ for eg. `endpoint: "https://demo.agora.grnet.gr/"`
2. Issue `npm run build`
3. Deploy contents of the `./build/` folder to the correspodning subfolder on the remote webserver

## Configure apache to host agora accounting in subfolder `./accounting`
Steps to configure apache:
1. Deploy optimized build to a folder such as `/srv/agora/accounting`
2. Use an apache Alias such as the following:
   `Alias /accounting /srv/agora/accounting`
3. Use an apache Directory configuration directive such as
``` 
<Directory "/srv/agora/accounting">
     Order deny,allow
     Allow from all
     Require all granted
 
     RewriteEngine on
     # Don't rewrite files or directories
     RewriteCond %{REQUEST_FILENAME} -f [OR]
     RewriteCond %{REQUEST_FILENAME} -d
     RewriteRule ^ - [L]
     # Rewrite everything else to index.html to allow html5 state links
     RewriteRule ^ /accounting/index.html [L]
   </Directory>   
```

## Run locally with docker-compose
1. Start agora-sp docker with `docker-compose up -d`
2. Go to accounting `cd accounting`
3. Set the following setting to config.js (Its the default one)
   `endpoint: 'http://localhost:8000'`
4. Run react app
   `npm start`