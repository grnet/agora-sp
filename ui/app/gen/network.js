import { AgoraGen, basic_model_fields } from '../lib/common';

const {common, row} = basic_model_fields(['abbreviation', 'name', 'eosc_id'] );

export default AgoraGen.extend({
  modelName: 'network',
  path: 'networks',
  resourceName: 'api/v2/networks',
  common,
  list: {
    page: {
      title: 'network.menu',
    },
    menu: {
      label: 'network.menu',
      icon: 'device_hub',
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
    sort: {
      serverSide: true,
      active: true,
      sortBy: 'abbreviation',
      fields: ['name', 'abbreviation',],
    },
  },
});
