import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'supercategory.fields.name',
    hint: 'supercategory.hints.name'
  }),
});
