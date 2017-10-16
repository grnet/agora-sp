import DS from 'ember-data';

export default DS.Model.extend({
  username: DS.attr(),
  first_name: DS.attr(),
  last_name: DS.attr(),
  is_active: DS.attr({ type: 'boolean' }),
  is_staff: DS.attr({ type: 'boolean' }),
  email: DS.attr(),
  date_joined: DS.attr()
});
