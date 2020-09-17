import DS from 'ember-data';
import moment from 'moment';
import ENV from '../config/environment';
import { computeI18NChoice  } from '../lib/common';
const { computed, get } = Ember;

const DATE_FORMAT = ENV.APP.date_format,
    CHOICES = ENV.APP.resources;

export default DS.Model.extend({
  i18n: Ember.inject.service(),
  username: DS.attr({
    label: 'custom_user.fields.username',
    hint: 'custom_user.hints.username',
  }),
  first_name: DS.attr({
    label: 'custom_user.fields.first_name',
    hint: 'custom_user.hints.first_name',
  }),
  last_name: DS.attr({
    label: 'custom_user.fields.last_name',
    hint: 'custom_user.hints.last_name',
  }),
  is_active: DS.attr({
    type: 'boolean',
    defaultValue: true,
    label: 'custom_user.fields.is_active',
    hint: 'custom_user.hints.is_active',
  }),
  is_staff: DS.attr({
    type: 'boolean',
    defaultValue: false,
    label: 'custom_user.fields.is_staff',
    hint: 'custom_user.hints.is_staff',
  }),
  email: DS.attr({
    label: 'custom_user.fields.email',
    hint: 'custom_user.hints.email',
  }),
  date_joined: DS.attr({
    label: 'custom_user.fields.date_joined',
    hint: 'custom_user.hints.date_joined',
  }),
  shibboleth_id: DS.attr({
    label: 'custom_user.fields.shibboleth_id',
    hint: 'custom_user.hint.shibboleth_id',
  }),
  organisation_id: DS.attr(),
  date_joined_format: computed('date_joined', function(){
    const date = this.get('date_joined');

    return date ? moment(date).format(DATE_FORMAT) : '-';
  }),
  full_name: Ember.computed('first_name', 'last_name', function() {
    const first_name = this.get('first_name');
    const last_name = this.get('last_name');

    return `${first_name} ${last_name}`;
  }),
  role: DS.attr({
    type: 'select',
    choices: CHOICES.USER_ROLES,
    defaultValue: 'observer',
  }),
  role_verbose: computeI18NChoice('role', CHOICES.USER_ROLES),
  providers: DS.hasMany('provider'),
  organisation: DS.belongsTo('provider', {
    label: 'custom_user.fields.organisation',
    displayAttr: 'epp_bai_1_name',
    formAttrs: {
      optionLabelAttr: 'epp_bai_1_name',
    },
  }),
  __api__: {
    serialize: function(hash, serializer) {
      // do not send readonly keys to backend
      delete hash['shibboleth_id'];
      delete hash['date_joined'];
      delete hash['organisation_id'];

      return hash;
    },
  },
});
