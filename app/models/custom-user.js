import DS from 'ember-data';

export default DS.Model.extend({
  username: DS.attr({
    label: 'custom_user.fields.username',
    hint: 'custom_user.hints.username'
  }),
  first_name: DS.attr({
    label: 'custom_user.fields.first_name',
    hint: 'custom_user.hints.first_name'
  }),
  last_name: DS.attr({
    label: 'custom_user.fields.last_name',
    hint: 'custom_user.hints.last_name'
  }),
  is_active: DS.attr({
    type: 'boolean',
    label: 'custom_user.fields.is_active',
    hint: 'custom_user.hints.is_active'
  }),
  is_staff: DS.attr({
    type: 'boolean',
    label: 'custom_user.fields.is_staff',
    hint: 'custom_user.hints.is_staff'
  }),
  email: DS.attr({
    label: 'custom_user.fields.email',
    hint: 'custom_user.hints.email'
  }),
  date_joined: DS.attr({
    label: 'custom_user.fields.date_joined',
    hint: 'custom_user.hints.date_joined'
  }),
  shibboleth_id: DS.attr({
    label: 'custom_user.fields.shibboleth_id',
    hint: 'custom_user.hint.shibboleth_id'
  }),
  full_name: Ember.computed('first_name', 'last_name', function() {
    const first_name = this.get('first_name');
    const last_name = this.get('last_name');
    return `${first_name} ${last_name}`;
  }),

});
