import DS from 'ember-data';

export default DS.Model.extend({
  first_name: DS.attr({
    label: 'contact_information.fields.first_name',
    hint: 'contact_information.hints.first_name',
  }),
  last_name: DS.attr({
    label: 'contact_information.fields.last_name',
    hint: 'contact_information.hints.last_name',
  }),
  email: DS.attr({
    label: 'contact_information.fields.email',
    hint: 'contact_information.hints.email',
  }),
  phone: DS.attr({
    label: 'contact_information.fields.phone',
    hint: 'contact_information.hints.phone',
  }),
  position: DS.attr({
    label: 'contact_information.fields.position',
    hint: 'contact_information.hints.position',
  }),
  organisation: DS.belongsTo('provider', {
    label: 'contact_information.fields.organisation',
    hint: 'contact_information.hints.organisation',
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  full_name: Ember.computed('first_name', 'last_name', function() {
    const first_name = this.get('first_name');
    const last_name = this.get('last_name');

    return `${first_name} ${last_name}`;
  }),

  displayInfo: Ember.computed('full_name', 'organisation.name', function() {
    const full_name = this.get('full_name');
    const org = this.get('organisation.name');

    return `${full_name} (${org})`;
  }),
});
