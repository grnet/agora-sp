import DS from 'ember-data';
import gen from 'ember-gen/lib/attrs';
import ENV from '../config/environment';

const ROOT_URL = ENV.rootURL || '/';

let model = DS.Model.extend({
  privacy_policy_url: DS.attr(),
  monitoring_url: DS.attr(),
  user_manual: DS.attr(),
  admin_manual: DS.attr(),
  terms_of_use_url: DS.attr(),
  version: DS.attr(),
  use_cases: DS.attr(),
  is_in_catalogue: DS.attr({ type: 'boolean', default: false }),
  visible_to_marketplace: DS.attr({ type: 'boolean', default: false }),
  status_ext: DS.attr(),
  service_admins_ids: DS.attr(),
  access_policies: DS.hasMany('access_policy'),
  sla_url: DS.attr(),
  training_information: DS.attr(),
  maintenance_url: DS.attr(),
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
    const service = Ember.get(this, 'id_service.id');
    const service_version = Ember.get(this, 'id');

    return `${ROOT_URL}component-implementation-detail-links/create?service=${service}&service_version=${service_version}`;
  }),
  // the object resembles the value to be printed in the create/update page of this referenced model
  // e.g. name is a key from the service-item model
  id_service: gen.belongsTo('service_item', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  status: gen.belongsTo('service_status', {
    label: 'service_status.belongs.value',
    hint: 'service_version.hints.status',
    formAttrs: {
      optionLabelAttr: 'value'
    }
  }),

  __api__: {
    serialize: function(hash, serializer) {
      // do not send readonly keys to backend
      delete hash['service_admins_ids'];
      delete hash['status_ext'];
      delete hash['id_service_ext'];

      return hash;
    },
  },

});

model.reopenClass({ apimasResourceName: 'api/v2/service-versions' });

export default model;
