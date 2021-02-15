import { AgoraGen, basic_model } from '../lib/common';

const {
  get,
  computed,
} = Ember;

const {common, row, sort} = basic_model(true);

export default AgoraGen.extend({
  modelName: 'order-type',
  path: 'order-types',
  resourceName: 'api/v2/order-types',
  common,
  list: {
    page: {
      title: 'order_type.menu',
    },
    menu: {
      display: computed('role', function(){
        let role = get(this, 'session.session.authenticated.role');
        return role !== 'serviceadmin';
      }),
      label: 'order_type.menu',
      icon: 'attach_money',
      group: 'resource_settings',
    },
    row,
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'Search by type or description',
    },
    sort,
  },
});
