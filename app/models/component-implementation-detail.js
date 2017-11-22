import DS from 'ember-data';

export default DS.Model.extend({
  version: DS.attr(),
  component_implementation_id: DS.belongsTo('component-implementation', {
    formComponent: 'select-onchange',
    formAttrs: {
      lookupField: 'component_id',
      changedChoices: function(store, value) {
        return store.query('component-implementation', {component_id: Ember.get(value, 'id')});
      },
      optionLabelAttr: 'name'
    }
  }),
  component_id: DS.belongsTo('component', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
});
