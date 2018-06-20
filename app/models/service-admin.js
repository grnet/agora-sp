import DS from 'ember-data';
import ENV from '../config/environment';

const CHOICES = ENV.APP.resources;

let model = DS.Model.extend({
  admin: DS.belongsTo('custom-user', {
    formAttrs: {
      optionLabelAttr: 'username',
    },
  }),
  service: DS.belongsTo('service-item', {
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  service_name: DS.attr({
    label: 'service_admin.fields.service_name',
  }),
  admin_email: DS.attr({
    label: 'service_admin.fields.admin_email',
  }),
  admin_first_name: DS.attr(),
  admin_last_name: DS.attr(),
  admin_full_name: Ember.computed('admin_first_name', 'admin_last_name', function() {
    const first_name = this.get('admin_first_name');
    const last_name = this.get('admin_last_name');

    return `${first_name} ${last_name}`;
  }),
  admin_id: DS.attr(),
  created_at: DS.attr('date', {
    label: 'service_admin.fields.created_at',
  }),
  updated_at: DS.attr('date', {
    label: 'service_admin.fields.updated_at',
  }),
  state: DS.attr({
    type: 'select',
    choices: CHOICES.SERVICE_ADMINSHIP_STATES,
    label: 'service_admin.fields.state',
  }),

});

model.reopenClass({ apimasResourceName: 'api/v2/service-admins' })

export default model;
