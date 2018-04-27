import DS from 'ember-data';
import ENV from '../config/environment';

const CHOICES = ENV.APP.resources;

export default DS.Model.extend({
  owner: DS.belongsTo('custom-user', {
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
    label: 'service.name',
  }),
  owner_email: DS.attr({
    label: 'custom_user.email',
  }),
  owner_first_name: DS.attr(),
  owner_last_name: DS.attr(),
  owner_full_name: Ember.computed('owner_first_name', 'owner_last_name', function() {
    const first_name = this.get('owner_first_name');
    const last_name = this.get('owner_last_name');
    return `${first_name} ${last_name}`;
  }),

  state: DS.attr({ type: 'select', choices: CHOICES.SERVICE_OWNERSHIP_STATES }),

});
