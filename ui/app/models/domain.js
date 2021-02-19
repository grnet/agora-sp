import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'domain.fields.name',
    hint: 'domain.hints.name'
  }),
  eosc_id: DS.attr(),
});
