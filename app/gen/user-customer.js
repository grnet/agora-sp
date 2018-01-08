import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import validate from 'ember-gen/validate';

export default AgoraGen.extend({
  modelName: 'user-customer',
  order: 500,
  path: 'user-customers',
  resourceName: 'api/v2/user-customers',
  common: {
    fieldsets: [
      {
        label: 'user_customer.cards.basic_information',
        text: 'user_customer.cards.basic_hint',
        layout: {
          flex: [100, 100, 100]
        },
        fields: [
          'name',
          'service_id',
          'role',
        ]
      }
    ],
    validators: {
      name: [validate.presence(true)],
      service_id: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'user_customer.menu'
    },
    menu: {
      label: 'user_customer.menu',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        field('name.name', {
          label: 'user_role.belongs.name'
        }),
        field('service_id.name', {
          label: 'service_item.belongs.name'
        })
      ]
    },
    sort: {
      serverside: false,
      active: true,
      fields: ['name.name', 'service_id.name']
    },

  }
});
