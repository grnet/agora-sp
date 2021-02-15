import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'esfritype.fields.name',
    hint: 'esfritype.hints.name'
  }),
  eosc_id: DS.attr(),
});
