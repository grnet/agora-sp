import Ember from 'ember';
import ENV from '../config/environment';

export default Ember.Component.extend({
  tagName: 'footer',
  classNames: ['flex', 'layout-column', 'layout-align-end'],
  version: ENV.APP.version,
});
