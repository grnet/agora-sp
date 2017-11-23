import Ember from 'ember';
import DS from 'ember-data';
import { strip } from '../utils/common/common';

export default DS.Model.extend({
  name: DS.attr(),
  description: DS.attr(),
  logo: DS.attr(),
  //computed
  desc: Ember.computed('description', function() {
    return strip(Ember.get(this, 'description'));
  })
});
