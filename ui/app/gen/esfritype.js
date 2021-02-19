import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'esfritype',
  path: 'esfritypes',
  resourceName: 'api/v2/esfritypes',
  common,
  list: {
    page: {
      title: 'esfritype.menu',
    },
    menu: {
      label: 'esfritype.menu',
      icon: 'label',
      group: 'provider_settings',
      order: 90,
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
