import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'service-owner',
  auth: true,
  order: 100,
  path: 'service-owners',
  resourceName: 'api/v2/service-owners',
  list: {
    layout: 'table',
    page: {
      title: 'Service Owners'
    },
    menu: {
      label: 'Service Owners',
      group: {
        name: 'user-information',
        label: 'User Information',
        order: 1000
      }
    },
    row: {
      fields: [
        'first_name',
        'last_name',
        'email',
        'phone',
        'id_service_owner.name'
      ],
    }
  }
});
