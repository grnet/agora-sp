import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'user-customer',
  order: 2,
  path: 'user-customers',
  resourceName: 'api/v2/user-customers',
  list: {
    page: {
      title: 'User Customers'
    },
    menu: {
      label: 'User Customers',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'name.name',
        'role',
        'service_id.name'
      ]
    }
  }
});
