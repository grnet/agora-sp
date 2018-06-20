import { AgoraGen } from '../lib/common';
import validate from 'ember-gen/validate';

export default AgoraGen.extend({
  modelName: 'institution',
  path: 'institutions',
  resourceName: 'api/v2/institutions',
  common: {
    fieldsets: [
      {
        label: 'institution.cards.basic_information',
        text: 'institution.cards.basic_hint',
        layout: {
          flex: [100, 50, 50, 100]
        },
        fields: [
          'name',
          'department',
          'country',
          'address',
        ]
      }
    ],
    validators: {
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'institution.menu'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    },
    menu: {
      label: 'institution.menu',
      group: 'user-information'
    },
    sort: {
      serverSide: false,
      active: true,
      fields: ['name', 'department', 'country']
    },
  }
});
