import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';

const {
  get,
  computed,
} = Ember;

export default AgoraGen.extend({
  modelName: 'trl',
  path: 'trls',
  resourceName: 'api/v2/trls',
  common: {
    fieldsets: [
      {
        label: 'trl.cards.basic',
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
      title: 'trl.menu',
    },
    menu: {
      label: 'trl.menu',
      icon: 'verified',
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
