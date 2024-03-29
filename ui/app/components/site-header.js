import Ember from 'ember';
import ENV from '../config/environment';

export default Ember.Component.extend({
  rootURL: ENV.rootURL,
  logo: `assets/${ENV.logo}` || 'assets/logo.png',
});
