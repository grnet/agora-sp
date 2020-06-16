import DS from 'ember-data';

export default DS.Model.extend({
  domain: DS.belongsTo('merildomain', {
    label: 'merilsubdomain.fields.domain',
    hint: 'merilsubdomain.hints.domain',
    inverse: null,
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  name: DS.attr({
    label: 'merilsubdomain.fields.name',
    hint: 'merilsubdomain.hints.name'
  }),
  description: DS.attr({
    label: 'merilsubdomain.fields.description',
    hint: 'merilsubdomain.hints.description'
  }),
});
