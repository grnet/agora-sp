import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'resource_lcs.fields.name',
  }),
  description: DS.attr(),
  eosc_id: DS.attr(),
});
