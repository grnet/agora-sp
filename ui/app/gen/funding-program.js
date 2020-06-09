import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';

const {
  get,
  computed,
} = Ember;

export default AgoraGen.extend({
  modelName: 'funding-program',
  path: 'funding-programs',
  resourceName: 'api/v2/funding-programs',
  common: {
    validators: {
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'funding_program.menu',
    },
    menu: {
      display: computed('role', function(){
        let role = get(this, 'session.session.authenticated.role');
        return role !== 'serviceadmin';
      }),
      label: 'funding_program.menu',
      icon: 'attach_money',
      group: {
        name: 'resource_settings',
        label: 'group_menu.resource_settings',
        order: 200,
      },
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
