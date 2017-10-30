import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'user-role',
  order: 2,
  path: 'user-roles',
  resourceName: 'api/v2/user-roles',
  list: {
    layout: 'table',
    page: {
      title: 'User Roles'
    },
    menu: {
      label: 'User Roles',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
    }
  }
});
