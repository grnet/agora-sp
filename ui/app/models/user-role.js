import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'user_role.fields.name',
    hint: 'user_role.hints.name'
  })
});
