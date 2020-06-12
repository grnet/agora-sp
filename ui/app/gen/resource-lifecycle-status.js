import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';

const {
  get,
  computed,
} = Ember;

export default AgoraGen.extend({
  modelName: 'resource-lifecycle-status',
  path: 'resource-lifecycle-statuses',
  resourceName: 'api/v2/resource-lifecycle-statuses',
  common: {
    fieldsets: [
      {
        label: 'resource_trl.cards.basic',
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
      title: 'resource_lcs.menu',
    },
    menu: {
      label: 'resource_lcs.menu',
      icon: 'restore',
      group: 'resource_settings',
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
    },
    sort: {
      serverSide: true,
      active: true,
      sortBy: 'name',
      fields: ['name'],
    },
  },
});
