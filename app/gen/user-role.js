import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'user-role',
  order: 200,
  path: 'user-roles',
  resourceName: 'api/v2/user-roles',
  list: {
    page: {
      title: 'user_role.menu'
    },
    menu: {
      label: 'user_role.menu',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    },
    sort: {
      serverside: false,
      active: true,
      fields: ['name']
    },

  }
});
