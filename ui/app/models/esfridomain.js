import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'esfridomain.fields.name',
    hint: 'esfridomain.hints.name'
  }),
  description: DS.attr({
    label: 'esfridomain.fields.description',
    hint: 'esfridomain.hints.description'
  }),
});
