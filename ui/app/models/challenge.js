import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'challenge.fields.name',
    hint: 'challenge.hints.name'
  }),
  eosc_id: DS.attr(),
});
