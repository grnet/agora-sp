import Ember from 'ember';
import DS from 'ember-data';

export default DS.Model.extend({
  first_name: DS.attr({
    label: 'service_owner.fields.first_name',
    hint: 'service_owner.hints.first_name'
  }),
  last_name: DS.attr({
    label: 'service_owner.fields.last_name',
    hint: 'service_owner.hints.last_name'
  }),
  email: DS.attr({
    label: 'service_owner.fields.email',
    hint: 'service_owner.hints.email'
  }),
  phone: DS.attr({
    label: 'service_owner.fields.phone',
    hint: 'service_owner.hints.phone'
  }),
  full_name: Ember.computed('first_name', 'last_name', function() {
    const first_name = this.get('first_name');
    const last_name = this.get('last_name');
    return `${first_name} ${last_name}`;
  }),
  id_service_owner: DS.belongsTo('institution', {
    label: 'institution.belongs.name',
    hint: 'institution.belongs.hint',
    displayAttr: 'name',
    formAttrs: {
      optionLabelAttr: 'name'
    },
  })
});
