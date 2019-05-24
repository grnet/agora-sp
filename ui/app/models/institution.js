import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'institution.fields.name',
    hint: 'institution.hints.name'
  }),
  department: DS.attr({
    label: 'institution.fields.department',
    hint: 'institution.hints.department'
  }),
  country: DS.attr({
    label: 'institution.fields.country',
    hint: 'institution.hints.country'
  }),
  address: DS.attr({
    label: 'institution.fields.address',
    hint: 'institution.hints.address'
  }),
});
