# Agora metrics ui

Agora metrics is a single page front-end application built with react (and create-react-app tool) that displays the following data based on a specific time range for an agora instance:
- new users
- new/updated providers
- new/updated resources

## Configuration

In `metrics/src/config.js` there are some basic configuration properties to be set before producing the optimized build. The properties that can be set are as follows:
- `endpoint: "http://localhost:8000"`
  Defines the agora api endpoint
- `supportMail: agora@grnet.gr`
  Defines the support mail to show in the metrics page
- `catalogueUrl: "http://localhost/catalogue"`
  Agora catalogue link. If catalogueUrl is empty it wont be visible in navbar
- `colors: {}`
  Set colors for:
   - navbar
   - navbar text
   - search button color
   - previous months table header
   - previous months table header text


## Build and deploy

Steps to build and deploy the app:

1. git clone this repo and go to metrics directory `cd agora/metrics`
2. Issue `npm install` 
3. Configure parameters in `./src/config.js`
4. Issue `npm run build`
5. Deploy contents of the `./build/` folder to the remote webserver

## Deploy on a specific subfolder - for example under https://demo.agora.grnet.gr/metrics
If the app is meant to be deployed under a subfolder on the remote node make sure that:
1. endpoint parameter (in `./src/config.js`) is set to the main url
~ for eg. `endpoint: "https://demo.agora.grnet.gr/"`
2. Issue `npm run build`
3. Deploy contents of the `./build/` folder to the correspodning subfolder on the remote webserver

## Configure apache to host agora metrics in subfolder `./metrics`
Steps to configure apache:
1. Deploy optimized build to a folder such as `/srv/agora/metrics`
2. Use an apache Alias such as the following:
   `Alias /metrics /srv/agora/metrics`
3. Use an apache Directory configuration directive such as
``` 
<Directory "/srv/agora/metrics">
     Order deny,allow
     Allow from all
     Require all granted
 
     RewriteEngine on
     # Don't rewrite files or directories
     RewriteCond %{REQUEST_FILENAME} -f [OR]
     RewriteCond %{REQUEST_FILENAME} -d
     RewriteRule ^ - [L]
     # Rewrite everything else to index.html to allow html5 state links
     RewriteRule ^ /metrics/index.html [L]
   </Directory>   
```

## Run locally with docker-compose
1. Start agora-sp docker with `docker-compose up -d`
2. Go to metrics `cd metrics`
3. Set the following setting to config.js (Its the default one)
   `endpoint: 'http://localhost:8000'`
4. Run react app
   `npm start`
