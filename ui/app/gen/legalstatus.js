import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'legalstatus',
  path: 'legalstatuses',
  resourceName: 'api/v2/legalstatuses',
  common,
  list: {
    page: {
      title: 'legalstatus.menu',
    },
    menu: {
      label: 'legalstatus.menu',
      icon: 'gavel',
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
