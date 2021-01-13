# Agora catalog ui

Agora catalog ui is a single page front-end application built with react (and create-react-app tool) that displays a catalog of provider and resource information published publicly on an agora api endpoint. 

## Configuration 
In `./src/config.js` there are some basic configuration properties to be set before producing the optimized build. The properties that can be set are as follows:

- `logo: "default"`
  Option to use the default or a custom logo for agora catalog navbar branding
- `brand: "agora service catalog"`
  Option to specify a brand title for the specific agora catalog instance
- `endpoint: "demo.agora.grnet.gr"`
  Option to specify a public agora api to retrieve published results from 
- `colorA:"#9c6078"`
  Option to specify a primary color for theme-ing
- `colorB:"#112130"`
  Option to specify a secondary color for theme-ing
- `basePath: "/catalog"`
  Optional parameter to specify a subfolder path where the web app will be hosted. If defined here set also accordingly the homepage parameter at package.json

## Build and deploy

Steps to build and deploy the app:

1. git clone this repo
2. Issue `npm install` 
3. Configure parameters in `./src/build`
4. Issue `npm run build`
5. Deploy contents of the `./build/` folder to the remote webserver

## Deploy on root folder on remote webserver
If the app is meant to be deployed directly in a remote node such as https://demo.agora.grnet.gr make sure that:
1. basePath parameter is omitted in `./src/config.js` file 
2. homepage parameter is omitted in `package.json` file
3. Issue `npm run build`
4. Deploy contents of the `./build/` folder to the corresponding document root folder of the remote webserver

## Deploy on a specific subfolder - for example under https://demo.agora.grnet.gr/catalog
If the app is meant to be deployed under a subfolder on the remote node make sure that:
1. basePath parameter (in `./src/config.js`) is set to the subfolder value ~ for eg. `basePath: "/catalog"`
2. homepage parameter (in `package.json`) is set to the correct domain/path value ~ for eg. "homepage":"https://demo.agora.grnet.gr/catalog"
3. Issue `npm run build`
4. Deploy contents of the `./build/` folder to the correspodning subfolder on the remote webserver

## Configure apache to host agora catalog in subfolder `./catalog`
Steps to configure apache:
1. Deploy optimized build to a folder such as `/srv/agora/catalog`
2. Use an apache Alias such as the following:
   `Alias /catalog /srv/agora/catalog`
3. Use an apache Directory configuration directive such as
``` 
<Directory "/srv/agora/catalog">
     Order deny,allow
     Allow from all
     Require all granted
 
     RewriteEngine on
     # Don't rewrite files or directories
     RewriteCond %{REQUEST_FILENAME} -f [OR]
     RewriteCond %{REQUEST_FILENAME} -d
     RewriteRule ^ - [L]
     # Rewrite everything else to index.html to allow html5 state links
     RewriteRule ^ /catalog/index.html [L]
   </Directory>   
```
