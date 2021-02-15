import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'structure.fields.name',
    hint: 'structure.hints.name'
  }),
  description: DS.attr({
    label: 'structure.fields.description',
    hint: 'structure.hints.description'
  }),
  eosc_id: DS.attr(),
});
