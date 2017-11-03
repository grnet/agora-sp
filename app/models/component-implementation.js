import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr(),
  description: DS.attr(),
  component_id: DS.belongsTo('component', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
});
