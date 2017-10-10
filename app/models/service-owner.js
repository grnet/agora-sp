import DS from 'ember-data';

export default DS.Model.extend({
  first_name: DS.attr(),
  last_name: DS.attr(),
  email: DS.attr(),
  phone: DS.attr(),
  id_service_owner: DS.belongsTo('institution', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  })
});
