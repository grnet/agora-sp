/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'agora-admin',
    environment: environment,
    i18n: {
      defaultLocale: 'en'
    },
    rootURL: '/',
    locationType: 'auto',
    appURL: 'http://127.0.0.1:8080/api/v2/',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      },
      EXTEND_PROTOTYPES: {
        // Prevent Ember Data from overriding Date.parse.
        Date: false
      }
    },
    tinyMCE:{
      version: 4
    },
    APP: {
      backend_host: 'http://127.0.0.1:8080/api/v2',
      backend_media_root: 'http://127.0.0.1:8080/static/img/',
      date_format: 'DD/MM/YYYY',
      default_route: 'service-item.index',
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  ENV['ember-simple-auth'] = {
    authenticationRoute: 'auth.index',
    authorizer: 'authorizer:token'
  };

  ENV['ember-simple-auth-token'] = {
    serverTokenEndpoint: '/api/v2/auth/login/',
    identificationField: 'username',
    passwordField: 'password',
    tokenPropertyName: 'auth_token',
    authorizationPrefix: 'Token ',
    authorizationHeaderName: 'Authorization',
    headers: {},
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {

  }

  return ENV;
};
