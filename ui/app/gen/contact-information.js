import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'contact-information',
  order: 600,
  path: 'contact-information',
  resourceName: 'api/v2/contact-information',
  common: {
    fieldsets: [ {
      label: 'contact_information.cards.basic_info',
      fields: [
        'first_name',
        'last_name',
        'email',
        'phone',
        'position',
        'organisation',
      ],
      layout: {
        flex: [50, 50, 50, 50, 50, 50],
      },
    }],
  },
  list: {
    page: {
      title: 'contact_information.menu'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'full_name',
        'email',
        'position',
        'organisation.name',
      ]
    },
    menu: {
      label: 'contact_information.menu',
      group: {
        name: 'user-information',
        order: 100,
      },
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['email', 'position']
    },
  },
  details: {

    fieldsets: [ {
      label: 'contact_information.cards.basic_info',
      fields: [
        'first_name',
        'last_name',
        'email',
        'phone',
        'position',
        'organisation.name',
      ],
      layout: {
        flex: [50, 50, 50, 50, 50, 50],
      },
    }],
  }
});
