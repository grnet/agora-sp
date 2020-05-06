import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'network.fields.name',
    hint: 'network.hints.name'
  }),
});
