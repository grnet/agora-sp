import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'esfridomain.fields.name',
    hint: 'esfridomain.hints.name'
  }),
});
