import DS from 'ember-data';

export default DS.Model.extend({
  domain: DS.belongsTo('domain', {
    label: 'subdomain.fields.domain',
    hint: 'subdomain.hints.domain',
    inverse: null,
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  name: DS.attr({
    label: 'subdomain.fields.name',
    hint: 'subdomain.hints.name'
  }),
  eosc_id: DS.attr(),
});
