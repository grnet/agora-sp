import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr(),
  service_admins_ids: DS.attr(),
  __api__: {
    path: 'my-services',
  }

});
