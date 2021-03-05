import Ember from 'ember';
import ENV from '../config/environment';

export default Ember.Component.extend({
  login_service: ENV.APP.footer["privacy_login_service"],
  login_url: ENV.APP.footer["privacy_login_url"],
  service_url: ENV.APP.footer["privacy_service_url"],
});
