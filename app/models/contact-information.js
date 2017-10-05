import DS from 'ember-data';

export default DS.Model.extend({
  first_name: DS.attr(),
  last_name: DS.attr(),
  url: DS.attr(),
  phone: DS.attr(),
  email: DS.attr(),
  __api__: {
    path: 'contact-information'
  }
});
