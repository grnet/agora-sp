import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'order_type.fields.name',
  }),
  description: DS.attr({
    label: 'order_type.fields.description',
  }),
});
