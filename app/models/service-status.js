import DS from 'ember-data';

export default DS.Model.extend({
  value: DS.attr(),
  order: DS.attr(),
  __api__: {
    path: 'service-status'
  }
});
