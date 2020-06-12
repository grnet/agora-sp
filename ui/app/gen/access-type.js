import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';

const {
  get,
  computed,
} = Ember;

export default AgoraGen.extend({
  modelName: 'access-type',
  path: 'access-types',
  resourceName: 'api/v2/access-types',
  common: {
    fieldsets: [
      {
        label: 'access_type.cards.basic',
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
      title: 'access_type.menu',
    },
    menu: {
      label: 'access_type.menu',
      icon: 'login',
      group: {
        name: 'resource_settings',
        label: 'group_menu.resource_settings',
        icon: 'settings',
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
