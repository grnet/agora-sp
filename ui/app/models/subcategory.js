import DS from 'ember-data';

export default DS.Model.extend({
  category: DS.belongsTo('category', {
    label: 'subcategory.fields.category',
    hint: 'subcategory.hints.category',
    inverse: null,
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  name: DS.attr({
    label: 'subcategory.fields.name',
    hint: 'subcategory.hints.name'
  }),
  eosc_id: DS.attr(),
});
