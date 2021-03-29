import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model(true);

export default AgoraGen.extend({
  modelName: 'access-mode',
  path: 'access-modes',
  resourceName: 'api/v2/access-modes',
  common,
  list: {
    page: {
      title: 'access_mode.menu',
    },
    menu: {
      label: 'access_mode.menu',
      icon: 'lock_open',
      group: 'resource_settings',
      order: 10,
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
