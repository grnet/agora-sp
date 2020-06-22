import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'affiliation.fields.name',
    hint: 'affiliation.hints.name'
  }),
});
