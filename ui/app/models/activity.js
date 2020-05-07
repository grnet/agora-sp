import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'activity.fields.name',
    hint: 'activity.hints.name'
  }),
});
