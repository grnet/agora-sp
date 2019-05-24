import Ember from 'ember';

export default Ember.Component.extend({
  tagName: 'md-input-container',
  classNameBindings: ['displayErrors:md-input-invalid'],
});
