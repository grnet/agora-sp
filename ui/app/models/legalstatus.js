import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'legalstatus.fields.name',
    hint: 'legalstatus.hints.name'
  })
});
