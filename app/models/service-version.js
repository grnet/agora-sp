import DS from 'ember-data';
import gen from 'ember-gen/lib/attrs';

let model = DS.Model.extend({
  privacy_policy_has: DS.attr({ type: 'boolean' }),
  privacy_policy_url: DS.attr(),
  monitoring_has: DS.attr({ type: 'boolean' }),
  monitoring_url: DS.attr(),
  user_documentation_has: DS.attr({ type: 'boolean' }),
  user_manual: DS.attr(),
  decommissioning_procedure_has: DS.attr({ type: 'boolean' }),
  decommissioning_procedure_url: DS.attr(),
  accounting_has: DS.attr({ type: 'boolean' }),
  accounting_url: DS.attr(),
  operations_documentation_has: DS.attr({ type: 'boolean' }),
  admin_manual: DS.attr(),
  business_continuity_plan_has: DS.attr({ type: 'boolean' }),
  business_continuity_plan_url: DS.attr(),
  disaster_recovery_plan_has: DS.attr({ type: 'boolean' }),
  disaster_recovery_plan_url: DS.attr(),
  terms_of_use_has: DS.attr({ type: 'boolean' }),
  terms_of_use_url: DS.attr(),
  features_current: DS.attr(),
  features_future: DS.attr(),
  cost_to_run: DS.attr(),
  version: DS.attr(),
  cost_to_build: DS.attr(),
  use_cases: DS.attr(),
  is_in_catalogue: DS.attr({ type: 'boolean', default: false }),
  visible_to_marketplace: DS.attr({ type: 'boolean', default: false }),
  id_service_ext: DS.attr(),
  status_ext: DS.attr(),
  service_admins_ids: DS.attr(),
  access_policies: DS.hasMany('access_policy'),
  sla_url: DS.attr(),
  training_information: DS.attr(),
  maintenance: DS.attr(),
  // id_service_ext is service.name
  id_service_ext: DS.attr(),
  service_trl: DS.belongsTo('service-trl', {
    label: 'service_version.fields.service_trl',
    hint: 'service_version.hints.service_trl',
    formAttrs: {
      optionLabelAttr: 'value',
    },
  }),
  cidl_url: Ember.computed('id', 'id_service.id', function() {
    const service =  Ember.get(this, 'id_service.id');
    const service_version = Ember.get(this, 'id');
    return `/component-implementation-detail-links/create?service=${service}&service_version=${service_version}`;
  }),
  //the object resembles the value to be printed in the create/update page of this referenced model
  //e.g. name is a key from the service-item model
  id_service: gen.belongsTo('service_item', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  my_service: gen.belongsTo('my_service', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),

  status: gen.belongsTo('service_status', {
    label: 'service_version.fields.status',
    hint: 'service_version.hints.status',
    formAttrs: {
      optionLabelAttr: 'value'
    }
  }),

  __api__: {
    serialize: function(hash, serializer) {
      // Hacky trick: We want to send 'id_service' to backend and not 'my_service'
      if ('my_service' in hash && hash['my_service']) {
        let tmp = hash['my_service'];
        tmp = tmp.replace('my-services', 'services');
        hash['id_service'] = tmp;
      }
      delete hash['my_service'];

      // do not send readonly keys to backend
      delete hash['service_admins_ids'];
      delete hash['status_ext'];
      delete hash['id_service_ext'];
      return hash;
    },
    normalize: function(json) {
      if ('id_service' in json) {
        json['my_service'] = json['id_service'].replace('services', 'my-services')
      }
      return json
    }
  },


});

model.reopenClass({ apimasResourceName: 'api/v2/service-versions' });

export default model;
