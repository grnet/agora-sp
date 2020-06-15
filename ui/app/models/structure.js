import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'structure.fields.name',
    hint: 'structure.hints.name'
  }),
  description: DS.attr({
    label: 'esfridomain.fields.description',
    hint: 'esfridomain.hints.description'
  }),
});
