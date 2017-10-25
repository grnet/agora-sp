import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'service-area',
  auth: true,
  order: 100,
  path: 'service-areas',
  resourceName: 'api/v2/service-areas',
  list: {
    layout: 'table',
    page: {
      title: 'Service Areas'
    },
    menu: {
      label: 'Service Areas'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        //'id',
        'name',
        'icon'
      ]
    },
  }
});
