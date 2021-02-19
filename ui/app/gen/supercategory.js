import { AgoraGen, basic_model } from '../lib/common';

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'supercategory',
  path: 'supercategories',
  resourceName: 'api/v2/supercategories',
  common,
  list: {
    page: {
      title: 'supercategory.menu',
    },
    menu: {
      label: 'supercategory.menu',
      icon: 'local_offer',
      group: 'class_settings',
      order: 50,
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
