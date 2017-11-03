import DS from 'ember-data';

export default DS.Model.extend({
  version: DS.attr(),
  component_implementation_id: DS.belongsTo('component-implementation', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  component_id: DS.belongsTo('component', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
});
