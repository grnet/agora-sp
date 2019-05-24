import DS from 'ember-data';

export default DS.Model.extend({
  username: DS.attr(),
  password: DS.attr({formAttrs: {type: 'password'}}),
  email: DS.attr()
});
