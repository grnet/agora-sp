import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'target-user',
  order: 200,
  path: 'target-users',
  resourceName: 'api/v2/target-users',
  list: {
    page: {
      title: 'target_user.menu'
    },
    menu: {
      label: 'target_user.menu',
      icon: 'person-pin',
      group: {
        name: 'user_settings',
        label: 'group_menu.user_settings',
        icon: 'settings',
        order: 900,
      },
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'common.placeholders.search',
    },
    sort: {
      serverSide: true,
      active: true,
      sortBy: 'user',
      fields: ['user'],
    },
  },
});
