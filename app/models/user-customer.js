import Ember from 'ember';
import DS from 'ember-data';
import { strip } from '../utils/common/common';

export default DS.Model.extend({
  name: DS.belongsTo('user-role', {
    label: 'user_role.belongs.name',
    displayAttr: 'name',
    hint: 'user_role.belongs.hint',
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  service_id: DS.belongsTo('service-item', {
    label: 'service_item.belongs.name',
    displayAttr: 'name',
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  role: DS.attr({
    label: 'user_customer.fields.role',
    hint: 'user_customer.hints.role',
    type: 'text',
    formComponent: 'text-editor',
    htmlSafe: true
  }),
  //computed
  __role: Ember.computed('role', function() {
    return strip(Ember.get(this, 'role'));
  })
});
