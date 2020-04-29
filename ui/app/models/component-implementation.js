// UNUSED
import Ember from 'ember';
import DS from 'ember-data';
import { shorten } from '../utils/common/common';

export default DS.Model.extend({
  name: DS.attr(),
  description: DS.attr(),
  component_id: DS.belongsTo('component', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  // computed fields
  desc: Ember.computed('description', function() {
    return shorten(Ember.get(this, 'description'));
  })
});
