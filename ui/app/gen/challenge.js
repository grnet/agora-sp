import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'challenge',
  path: 'challenges',
  resourceName: 'api/v2/challenges',
  common,
  list: {
    page: {
      title: 'challenge.menu',
    },
    menu: {
      label: 'challenge.menu',
      icon: 'eco',
      group: 'provider_settings',
      order: 38,
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
