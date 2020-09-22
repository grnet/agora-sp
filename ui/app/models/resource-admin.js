import DS from 'ember-data';
import ENV from '../config/environment';

const CHOICES = ENV.APP.resources;

const {
  get,
  computed
}  = Ember;

let model = DS.Model.extend({
  admin: DS.belongsTo('custom-user', {
    formAttrs: {
      optionLabelAttr: 'username',
    },
  }),
  resource: DS.belongsTo('resource', {
    formComponent: 'select-onchange',
    formAttrs: {
      optionLabelAttr: 'erp_bai_1_name',

      lookupField: 'admin',
      changedChoices: function(store, model) {
        let organisation_id = model.get('organisation_id')
        if (!organisation_id) {
          return [];
        }
        const params = {
          erp_bai_2_service_organisation: organisation_id
        };

        return store.query('resource', params);
      },
    },
  }),
  resource_name: DS.attr({
    label: 'resource_admin.fields.resource_name',
  }),
  admin_email: DS.attr({
    label: 'resource_admin.fields.admin_email',
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
    label: 'resource_admin.fields.created_at',
  }),
  updated_at: DS.attr('date', {
    label: 'resource_admin.fields.updated_at',
  }),
  state: DS.attr({
    type: 'select',
    choices: CHOICES.SERVICE_ADMINSHIP_STATES,
    label: 'resource_admin.fields.state',
  }),

});

model.reopenClass({ apimasResourceName: 'api/v2/resource-admins' })

export default model;
