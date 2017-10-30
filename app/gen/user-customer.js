import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'user-customer',
  order: 2,
  path: 'user-customers',
  resourceName: 'api/v2/user-customers',
  list: {
    layout: 'table',
    page: {
      title: 'User Customers'
    },
    menu: {
      label: 'User Customers',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'name.name',
        'role',
        'service_id.name'
      ]
    }
  }
});
