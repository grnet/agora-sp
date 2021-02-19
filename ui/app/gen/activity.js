import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'activity',
  path: 'activities',
  resourceName: 'api/v2/activities',
  common,
  list: {
    page: {
      title: 'activity.menu',
    },
    menu: {
      label: 'activity.menu',
      icon: 'landscape',
      group: 'provider_settings',
      order: 37,
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
