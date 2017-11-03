import DS from 'ember-data';

export default DS.Model.extend({
  configuration_parameters: DS.attr(),
  service_component_implementation_detail_id: DS.belongsTo('component-implementation-detail', {
    formAttrs: {
      optionLabelAttr: 'version'
    }
  }),
  service_id: DS.belongsTo('service-item', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  service_details_id: DS.belongsTo('service-version', {
    formAttrs: {
      optionLabelAttr: 'version'
    }
  }),
});
