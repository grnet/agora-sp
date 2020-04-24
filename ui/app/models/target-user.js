import DS from 'ember-data';

export default DS.Model.extend({
  user: DS.attr({
    label: 'target_user.fields.user',
  }),
  description: DS.attr({
    label: 'target_user.fields.description',
  }),
});
