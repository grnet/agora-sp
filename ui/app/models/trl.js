import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'trl.fields.name',
  }),
  description: DS.attr(),
  menu: 'Technology Readiness Levels',
});
