import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'access_mode.fields.name',
  }),
  description: DS.attr(),
  eosc_id: DS.attr(),
});
