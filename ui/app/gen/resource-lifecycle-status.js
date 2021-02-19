import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model(true);

export default AgoraGen.extend({
  modelName: 'resource-lifecycle-status',
  path: 'resource-lifecycle-statuses',
  resourceName: 'api/v2/resource-lifecycle-statuses',
  common,
  list: {
    page: {
      title: 'resource_lcs.menu',
    },
    menu: {
      label: 'resource_lcs.menu',
      icon: 'restore',
      group: 'resource_settings',
    },
    row,
    filter: {
      active: false,
      serverSide: true,
      search: true,
    },
    sort,
  },
});
