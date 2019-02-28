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
        const params = {
          id_service: Ember.get(value, 'id'),
          ordering: 'version',
        };
        return store.query('service-version', params);
      },
      optionLabelAttr: 'version'
    }
  }),
  my_service: DS.belongsTo('my_service', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  my_service_version: DS.belongsTo('service-version', {
    formComponent: 'select-onchange',
    formAttrs: {
      lookupField: 'my_service',
      changedChoices: function(store, value) {
        const params = {
          id_service: Ember.get(value, 'id'),
          ordering: 'version',
        }
        return store.query('service-version', params);
      },
      optionLabelAttr: 'version'
    }
  }),

  service_admins_ids: DS.attr(),

  __api__: {
    serialize: function(hash, serializer) {
      // Hacky trick: We want to send 'id_service' to backend and not 'my_service'
      if ('my_service' in hash && hash['my_service']) {
        let tmp = hash['my_service'];
        tmp = tmp.replace('my-services', 'services');
        hash['service_id'] = tmp;
      }
      if ('my_service_version' in hash && hash['my_service']) {
        hash['service_details_id'] = hash['my_service_version'];
      }

      delete hash['my_service'];
      delete hash['my_service_version'];

    //do not send unwanted keys to backend
      delete hash['service_component'];
      delete hash['service_admins_ids'];
      delete hash['service_component_implementation'];
      return hash;

    },
    normalize: function(json) {
      if ('service_id' in json) {
        json['my_service'] = json['service_id'].replace('services', 'my-services')
      }
      if ('service_details_id' in json) {
        json['my_service_version'] = json['service_details_id'];
      }

      return json
    }
  },


});
