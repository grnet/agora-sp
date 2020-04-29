// UNUSED
import Ember from 'ember';
import DS from 'ember-data';
import { strip, shorten } from '../utils/common/common';

export default DS.Model.extend({
  name: DS.attr(),
  description: DS.attr(),
  logo: DS.attr(),
  //computed
  desc: Ember.computed('description', function() {
    return shorten(Ember.get(this, 'description'));
  })
});
