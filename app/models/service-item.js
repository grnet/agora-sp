import DS from 'ember-data';
import Ember from 'ember';
import { shorten } from '../utils/common/common';

const {
  get,
} = Ember;


export default DS.Model.extend({
  session: Ember.inject.service(),
  name: DS.attr(),
  service_type: DS.attr(),
  funders_for_service: DS.attr(),
  description_external: DS.attr(),
  value_to_customer: DS.attr(),
  risks: DS.attr(),
  description_internal: DS.attr(),
  short_description: DS.attr(),
  competitors: DS.attr(),
  logo: DS.attr(),
  request_procedures: DS.attr(),
  customer_facing: DS.attr({
    type: 'boolean',
    label: 'service_item.fields.customer_facing',
    defaultValue: true,
  }),
  internal: DS.attr({
    type: 'boolean',
    label: 'service_item.fields.internal',
    defaultValue: false,
  }),
  service_version_url: Ember.computed('id', function() {
    return `/service-versions/create?service=${Ember.get(this, 'id')}`;
  }),
  service_area: DS.belongsTo('service-area', {
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  id_contact_information: DS.belongsTo('contact-information', {
    formAttrs: {
      optionLabelAttr: 'full_name',
    },
  }),
  id_contact_information_internal: DS.belongsTo('contact-information', {
    formAttrs: {
      optionLabelAttr: 'full_name',
    },
  }),
  service_trl: DS.belongsTo('service-trl', {
    formAttrs: {
      optionLabelAttr: 'value',
    },
  }),
  service_admins_ids: DS.attr(),
  pending_service_admins_ids: DS.attr(),
  rejected_service_admins_ids: DS.attr(),

  // computed
  short_desc: Ember.computed('short_description', function() {
    return shorten(Ember.get(this, 'short_description'));
  }),

  can_apply_adminship: Ember.computed('service_admins_ids', 'pending_service_admins_ids', 'rejected_service_admins_ids', function(){
    let role = get(this, 'session.session.authenticated.role');
    if (role != 'serviceadmin') { return false; }
    let approved = get(this, 'service_admins_ids').split(',');
    let pending = get(this, 'pending_service_admins_ids').split(',');
    let rejected = get(this, 'rejected_service_admins_ids').split(',');

    let all = [...approved, ...pending, ...rejected];
    let user_id = get(this, 'session.session.authenticated.id').toString();
    return !all.includes(user_id);
  }),

  can_revoke_adminship: Ember.computed('pending_service_admins_ids', function(){
    let role = get(this, 'session.session.authenticated.role');
    if (role != 'serviceadmin') { return false; }

    let pending = get(this, 'pending_service_admins_ids').split(',');
    let user_id = get(this, 'session.session.authenticated.id').toString();
    return pending.includes(user_id);
  }),

  has_rejected_adminship: Ember.computed('rejected_service_admins_ids', function(){
    let role = get(this, 'session.session.authenticated.role');
    if (role != 'serviceadmin') { return false; }

    let rejected = get(this, 'rejected_service_admins_ids').split(',');
    let user_id = get(this, 'session.session.authenticated.id').toString();
    return rejected.includes(user_id);
  }),



  __api__: {
    path: 'services',
    serialize: function(hash, serializer) {
      // do not send readonly keys to backend
      delete hash['service_admins_ids'];
      delete hash['pending_service_admins_ids'];
      delete hash['rejected_service_admins_ids'];
      return hash;
    },
  },

});
