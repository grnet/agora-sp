import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'network.fields.name',
    hint: 'network.hints.name'
  }),
  abbreviation: DS.attr({
    label: 'network.fields.abbreviation',
    hint: 'network.hints.abbreviation'
  }),
  eosc_id: DS.attr(),
});
