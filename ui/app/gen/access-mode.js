import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';

const {
  get,
  computed,
} = Ember;

export default AgoraGen.extend({
  modelName: 'access-mode',
  path: 'access-modes',
  resourceName: 'api/v2/access-modes',
  common: {
    fieldsets: [
      {
        label: 'access_mode.cards.basic',
        fields: [
          'name',
          'description'
        ],
        layout: {
          flex: [100, 100],
        },
      }
    ],
    validators: {
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'access_mode.menu',
    },
    menu: {
      label: 'access_mode.menu',
      icon: 'lock_open',
      group: {
        name: 'resource_settings',
        label: 'group_menu.resource_settings',
        order: 300,
      },
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'Search by Access Mode or Description',
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['name'],
    },
  },
});
