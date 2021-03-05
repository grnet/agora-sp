import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'merildomain.fields.name',
    hint: 'merildomain.hints.name'
  }),
  eosc_id: DS.attr(),
});
