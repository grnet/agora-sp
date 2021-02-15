import DS from 'ember-data';

export default DS.Model.extend({
  supercategory: DS.belongsTo('supercategory', {
    label: 'category.fields.supercategory',
    hint: 'category.hints.supercategory',
    inverse: null,
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  name: DS.attr({
    label: 'category.fields.name',
    hint: 'category.hints.name'
  }),
  eosc_id: DS.attr(),
});
