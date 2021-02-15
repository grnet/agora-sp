import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'esfridomain',
  path: 'esfridomains',
  resourceName: 'api/v2/esfridomains',
  common,
  list: {
    page: {
      title: 'esfridomain.menu',
    },
    menu: {
      label: 'esfridomain.menu',
      icon: 'group_work',
      group: 'provider_settings',
      order: 91,
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
