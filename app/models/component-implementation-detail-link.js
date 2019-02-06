import DS from 'ember-data';
import Ember from 'ember';

export default DS.Model.extend({
  configuration_parameters: DS.attr(),
  service_type: DS.attr(),
  service_component: DS.belongsTo('component', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  service_component_implementation: DS.belongsTo('component-implementation', {
    formComponent: 'select-onchange',
    formAttrs: {
      lookupField: 'service_component',
      changedChoices: function(store, value) {
        return store.query('component-implementation', {component_id: Ember.get(value, 'id')});
      },
      optionLabelAttr: 'name'
    }
  }),
  service_component_implementation_detail_id: DS.belongsTo('component-implementation-detail', {
    formComponent: 'select-onchange',
    formAttrs: {
      lookupField: 'service_component_implementation',
      changedChoices: function(store, value) {
        return store.query('component-implementation-detail', {component_implementation_id: Ember.get(value, 'id')});
      },
      optionLabelAttr: 'version'
    }
  }),
  service_id: DS.belongsTo('service-item', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  service_details_id: DS.belongsTo('service-version', {
    formComponent: 'select-onchange',
    formAttrs: {
      lookupField: 'service_id',
      changedChoices: function(store, value) {
        return store.query('service-version', {id_service: Ember.get(value, 'id')});
      },
      optionLabelAttr: 'version'
    }
  }),
  service_admins_ids: DS.attr(),
  __api__: {
    serialize: function(hash, serializer) {
      //do not send unwanted keys to backend
      delete hash['service_component'];
      delete hash['service_admins_ids'];
      delete hash['service_component_implementation'];
      return hash;
    }
  }
});
