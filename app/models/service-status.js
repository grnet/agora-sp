import DS from 'ember-data';
import Ember from 'ember';

export default DS.Model.extend({
  value: DS.attr(),
  order: DS.attr(),
  __api__: {
    path: 'service-status'
  }
});
