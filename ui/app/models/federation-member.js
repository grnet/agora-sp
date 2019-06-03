import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'federation_member.fields.name',
    hint: 'federation_member.hints.name',
  }),
  webpage: DS.attr({
    label: 'federation_member.fields.webpage',
    hint: 'federation_member.hints.webpage',
  }),
  logo: DS.attr({
    label: 'federation_member.fields.logo',
    hint: 'federation_member.hints.logo',
  }),
  country: DS.attr({
    label: 'federation_member.fields.country',
    hint: 'federation_member.hints.country',
  }),
});
