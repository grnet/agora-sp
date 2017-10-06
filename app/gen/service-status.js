import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'service-status',
  auth: true,
  order: 100,
  path: 'service-status',
  resourceName: 'service-status',
  list: {
    layout: 'table',
    page: {
      title: 'Service Status'
    },
    menu: {
      label: 'Service Status'
    },
    row: {
      fields: [
        //'id',
        'value',
        'order',
      ],
    }
  }
});
