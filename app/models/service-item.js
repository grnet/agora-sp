import DS from 'ember-data';
import Ember from 'ember';
import { shorten } from '../utils/common/common';

const {
  get,
} = Ember;


let model =  DS.Model.extend({
  session: Ember.inject.service(),
  name: DS.attr(),
  url: DS.attr(),
  endpoint : DS.attr(),
  tagline : DS.attr(),
  service_type: DS.attr(),
  funders_for_service: DS.attr(),
  description_external: DS.attr(),
  user_value: DS.attr(),
  target_customers: DS.attr(),
  target_users: DS.attr(),
  screenshots_videos: DS.attr(),
  languages: DS.attr(),
  standards: DS.attr(),
  certifications: DS.attr(),
  risks: DS.attr(),
  description_internal: DS.attr(),
  short_description: DS.attr(),
  competitors: DS.attr(),
  logo: DS.attr(),
  request_procedures: DS.attr(),
  service_category_ext: DS.attr(),
  service_trl_ext: DS.attr(),
  tags: DS.attr(),
  scientific_fields: DS.attr(),
  service_categories_names: DS.attr(),
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
  service_categories: DS.hasMany('service-category'),
  service_trl: DS.belongsTo('service-trl', {
    formAttrs: {
      optionLabelAttr: 'value',
    },
  }),
  service_admins_ids: DS.attr(),
  pending_service_admins_ids: DS.attr(),
  rejected_service_admins_ids: DS.attr(),
  providers: DS.hasMany('provider'),
  providers_names: DS.attr(),
  owner_name: DS.attr(),
  owner_contact: DS.attr(),
  security_name: DS.attr(),
  security_contact: DS.attr(),
  support_name: DS.attr(),
  support_contact: DS.attr(),
  helpdesk: DS.attr(),
  order: DS.attr(),
  order_type: DS.attr(),
  last_update: DS.attr('date', {
    displayComponent: 'date-formatted',
  }),
  changelog: DS.attr(),

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
      delete hash['service_category_ext'];
      delete hash['service_trl_ext'];
      delete hash['contact_external_full_name'];
      delete hash['contact_internal_full_name'];
      delete hash['providers_names'];
      delete hash['service_categories_names'];
      // handle external/internal contact information
      let contact_external = {};
      let contact_internal = {};
      Object.entries(hash).forEach(([key, value]) => {
        if (key.startsWith('contact_external')) {
          let new_key_ext = key.split('contact_external_')[1];
          contact_external[new_key_ext] = value;
          delete hash[key];
        } else if (key.startsWith('contact_internal')) {
          let new_key_int = key.split('contact_internal_')[1];
          contact_internal[new_key_int] = value;
          delete hash[key];
        }
      })
      hash['contact_information_external'] = contact_external;
      hash['contact_information_internal'] = contact_internal;
      return hash;
    },
    normalize: function(json) {
      if (json['contact_information_external']) {
        Object.entries(json['contact_information_external']).forEach(([key, value]) => {
          let new_key = `contact_external_${key}`;
          json[new_key] = value;
        });
        delete json['contact_information_external'];
      }
      if (json['contact_information_internal']) {
        Object.entries(json['contact_information_internal']).forEach(([key, value]) => {
          let new_key = `contact_internal_${key}`;
          json[new_key] = value;
        });
        delete json['contact_information_internal'];
      }
      return json;
    }
  },


  // contact information fields
  contact_external_first_name: DS.attr({
    label: 'service_item.fields.contact.first_name',
  }),
  contact_external_last_name: DS.attr({
    label: 'service_item.fields.contact.last_name',
  }),
  contact_external_email: DS.attr({
    label: 'service_item.fields.contact.email',
  }),
  contact_external_phone: DS.attr({
    label: 'service_item.fields.contact.phone',
  }),
  contact_external_full_name: DS.attr({
    label: 'service_item.fields.contact.full_name',
  }),
  contact_external_url: DS.attr({
    label: 'service_item.fields.contact.url',
  }),
  contact_internal_first_name: DS.attr({
    label: 'service_item.fields.contact.first_name',
  }),
  contact_internal_last_name: DS.attr({
    label: 'service_item.fields.contact.last_name',
  }),
  contact_internal_email: DS.attr({
    label: 'service_item.fields.contact.email',
  }),
  contact_internal_phone: DS.attr({
    label: 'service_item.fields.contact.phone',
  }),
  contact_internal_full_name: DS.attr({
    label: 'service_item.fields.contact.full_name',
  }),
  contact_internal_url: DS.attr({
    label: 'service_item.fields.contact.url',
  }),


});

model.reopenClass({ apimasResourceName: 'api/v2/services' })

export default model;
