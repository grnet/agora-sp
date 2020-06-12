import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';

const {
  get,
  computed,
} = Ember;

export default AgoraGen.extend({
  modelName: 'funding-body',
  path: 'funding-bodies',
  resourceName: 'api/v2/funding-bodies',
  common: {
    validators: {
      name: [validate.presence(true)],
    },
  },
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
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'Search by name',
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['name'],
    },
  },
});
