import { AgoraGen, basic_model } from '../lib/common';

const {
  get,
  computed,
} = Ember;

const {common, row, sort} = basic_model();

export default AgoraGen.extend({
  modelName: 'funding-body',
  path: 'funding-bodies',
  resourceName: 'api/v2/funding-bodies',
  common,
  list: {
    page: {
      title: 'funding_body.menu',
    },
    menu: {
      display: computed('role', function(){
        let role = get(this, 'session.session.authenticated.role');
        return role !== 'serviceadmin';
      }),
      label: 'funding_body.menu',
      icon: 'attach_money',
      group: 'resource_settings',
    },
    row,
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'Search by name',
    },
    sort,
  },
});
