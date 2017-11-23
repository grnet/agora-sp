import Ember from 'ember';
import DS from 'ember-data';
import { strip } from '../utils/common/common';

export default DS.Model.extend({
  name: DS.belongsTo('user-role', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  role: DS.attr(),
  service_id: DS.belongsTo('service-item', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  //computed
  __role: Ember.computed('role', function() {
    return strip(Ember.get(this, 'role'));
  })
});
