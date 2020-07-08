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
    inverse: null,
  }),
  organisation: DS.belongsTo('provider', {
    type: 'select',
    autocomplete: true,
    label: 'contact_information.fields.organisation',
    hint: 'contact_information.hints.organisation',
    inverse: null,
    formAttrs: {
      optionLabelAttr: 'epp_bai_1_name',
    },
  }),
  organisation_id: DS.attr(),
  full_name: Ember.computed('first_name', 'last_name', function() {
    const first_name = this.get('first_name');
    const last_name = this.get('last_name');

    return `${first_name} ${last_name}`;
  }),

  displayInfo: Ember.computed('full_name', 'organisation.epp_bai_1_name', function() {

    const full_name = this.get('full_name');
    const org = this.get('organisation.epp_bai_1_name');

    return `${full_name} (${org})`;
  }),

  __api__: {
    serialize: function(hash) {
      // do not send readonly keys to backend
      delete hash['organisation_id'];
      return hash;
    },
  },
});
