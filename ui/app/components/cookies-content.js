import Ember from 'ember';
import ENV from '../config/environment';

export default Ember.Component.extend({
  service_name: ENV.APP.footer["cookies_service_name"] || 'Agora',
  title: ENV.APP.footer["cookies_title"] || 'Cookie Policy',
  cookies: ENV.APP.footer["cookies"],
});
