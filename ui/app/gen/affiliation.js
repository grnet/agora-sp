import { AgoraGen } from '../lib/common';
import validate from 'ember-gen/validate';

export default AgoraGen.extend({
  modelName: 'affiliation',
  path: 'affiliations',
  resourceName: 'api/v2/affiliations',
  common: {
    validators: {
      'name': [validate.presence(true)]
    },
    fieldsets: [
      {
        label: 'common.cards.basic',
        fields: ['name'],
        layout: {
          flex: [100]
        },
      }
    ],
  },
  list: {
    page: {
      title: 'affiliation.menu',
    },
    menu: {
      label: 'affiliation.menu',
      icon: 'flag',
      group: {
        name: 'provider_settings',
        label: 'group_menu.provider_settings',
        icon: 'settings',
        order: 510,
      },
      order: 30,
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'common.placeholders.search',
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['name'],
    }
  },
});
