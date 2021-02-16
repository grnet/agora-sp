import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'domain',
  path: 'domains',
  resourceName: 'api/v2/domains',
  common,
  list: {
    page: {
      title: 'domain.menu',
    },
    menu: {
      label: 'domain.menu',
      icon: 'local_offer',
      group: 'class_settings',
      order: 40,
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
