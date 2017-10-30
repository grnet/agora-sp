import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.belongsTo('user-role', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  role: DS.attr(),
  service_id: DS.belongsTo('service-item', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  })
});
