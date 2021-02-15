import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'merildomain',
  path: 'merildomains',
  resourceName: 'api/v2/merildomains',
  common,
  list: {
    page: {
      title: 'merildomain.menu',
    },
    menu: {
      label: 'merildomain.menu',
      icon: 'local_offer',
      group: 'provider_settings',
      order: 93,
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
