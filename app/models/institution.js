import DS from 'ember-data';

export default DS.Model.extend({
  department: DS.attr(),
  country: DS.attr(),
  name: DS.attr(),
  address: DS.attr()
});
