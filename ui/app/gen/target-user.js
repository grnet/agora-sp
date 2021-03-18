import { AgoraGen, basic_model_fields } from '../lib/common';

const {common, row, sort} = basic_model_fields(['user', 'description', 'eosc_id'], 'user');

export default AgoraGen.extend({
  modelName: 'target-user',
  order: 200,
  path: 'target-users',
  resourceName: 'api/v2/target-users',
  common,
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
    row,
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'common.placeholders.search',
    },
    sort,
  },
});
