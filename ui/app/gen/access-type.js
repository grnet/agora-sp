import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model(true);

export default AgoraGen.extend({
  modelName: 'access-type',
  path: 'access-types',
  resourceName: 'api/v2/access-types',
  common,
  list: {
    page: {
      title: 'access_type.menu',
    },
    menu: {
      label: 'access_type.menu',
      icon: 'login',
      group: {
        name: 'resource_settings',
        label: 'group_menu.resource_settings',
        icon: 'settings',
        order: 500,
      },
    },
    row,
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'Search by access mode or description',
    },
    sort,
  },
});
