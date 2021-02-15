import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'affiliation',
  path: 'affiliations',
  resourceName: 'api/v2/affiliations',
  common,
  list: {
    page: {
      title: 'affiliation.menu',
    },
    menu: {
      label: 'affiliation.menu',
      icon: 'flag',
      group: {
        name: 'provider_settings',
        label: 'group_menu.provider_settings',
        icon: 'settings',
        order: 510,
      },
      order: 30,
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
