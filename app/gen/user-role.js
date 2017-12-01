import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'user-role',
  order: 2,
  path: 'user-roles',
  resourceName: 'api/v2/user-roles',
  list: {
    page: {
      title: 'User Roles'
    },
    menu: {
      label: 'User Roles',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    }
  }
});
