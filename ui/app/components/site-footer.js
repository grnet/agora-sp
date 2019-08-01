import Ember from 'ember';
import ENV from '../config/environment';

export default Ember.Component.extend({
  tagName: 'footer',
  classNames: ['flex', 'layout-row', 'layout-align-end-end', 'md-padding'],
  version: ENV.APP.version,
});
