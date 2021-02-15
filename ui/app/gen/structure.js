import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model(true);

export default AgoraGen.extend({
  modelName: 'structure',
  path: 'structures',
  resourceName: 'api/v2/structures',
  common,
  list: {
    page: {
      title: 'structure.menu',
    },
    menu: {
      label: 'structure.menu',
      icon: 'apartment',
      group: 'provider_settings',
      order: 32,
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
