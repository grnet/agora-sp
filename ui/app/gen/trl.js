import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model(true);

export default AgoraGen.extend({
  modelName: 'trl',
  path: 'trls',
  resourceName: 'api/v2/trls',
  common,
  list: {
    page: {
      title: 'trl.menu',
    },
    menu: {
      label: 'trl.menu',
      icon: 'verified',
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
