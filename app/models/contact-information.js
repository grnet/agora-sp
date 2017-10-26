import Ember from 'ember';
import DS from 'ember-data';

export default DS.Model.extend({
  first_name: DS.attr(),
  last_name: DS.attr(),
  url: DS.attr(),
  phone: DS.attr(),
  email: DS.attr(),
  full_name: Ember.computed('first_name', 'last_name', function() {
    const first_name = this.get('first_name');
    const last_name = this.get('last_name');
    return `${first_name} ${last_name}`;
  }),
  __api__: {
    path: 'contact-information'
  }
});
