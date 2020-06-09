import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import {
  FIELDSETS,
  SORT_FIELDS,
} from '../utils/common/order-type';

const {
  get,
  computed,
} = Ember;

export default AgoraGen.extend({
  modelName: 'order-type',
  path: 'order-types',
  resourceName: 'api/v2/order-types',
  common: {
    fieldsets: FIELDSETS,
    validators: {
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'order_type.menu',
    },
    menu: {
      display: computed('role', function(){
        let role = get(this, 'session.session.authenticated.role');
        return role !== 'serviceadmin';
      }),
      label: 'order_type.menu',
      icon: 'attach_money',
      group: {
        name: 'resource_settings',
        label: 'group_menu.resource_settings',
        order: 100,
          icon: 'settings',
      },
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    },
    sort: {
      serverSide: true,
      active: true,
      fields: SORT_FIELDS,
    },
  },
});
