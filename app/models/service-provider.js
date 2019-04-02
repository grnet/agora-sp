import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'service_provider.fields.name',
    hint: 'service_provider.hints.name',
  }),
  webpage: DS.attr({
    label: 'service_provider.fields.webpage',
    hint: 'service_provider.hints.webpage',
  }),
  logo: DS.attr({
    label: 'service_provider.fields.logo',
    hint: 'service_provider.hints.logo',
  }),
  country: DS.attr({
    label: 'service_provider.fields.country',
    hint: 'service_provider.hints.country',
  }),
});
