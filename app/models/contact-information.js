import Ember from 'ember';
import DS from 'ember-data';

export default DS.Model.extend({
  first_name: DS.attr({
    label: 'contact_information.fields.first_name',
    hint: 'contact_information.hint.first_name'
  }),
  last_name: DS.attr({
    label: 'contact_information.fields.last_name',
    hint: 'contact_information.hints.last_name'
  }),
  url: DS.attr({
    label: 'contact_information.fields.url',
    hint: 'contact_information.hints.url'

  }),
  phone: DS.attr({
    label: 'contact_information.fields.phone',
    hint: 'contact_information.hints.phone',
  }),
  email: DS.attr({
    label: 'contact_information.fields.email',
    hint: 'contact_information.hints.email',
  }),
  full_name: Ember.computed('first_name', 'last_name', function() {
    const first_name = this.get('first_name');
    const last_name = this.get('last_name');
    return `${first_name} ${last_name}`;
  }),
  __api__: {
    path: 'contact-information'
  }
});
