import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'service-version',
  auth: true,
  order: 100,
  path: 'service-versions',
  resourceName: 'service-versions',
  list: {
    layout: 'table',
    page: {
      title: 'Service Versions'
    },
    menu: {
      label: 'Service Versions'
    },
    row: {
      fields: [
        //'id',
        'version',
        'status.value',
        'is_in_catalogue',
        'id_service.name'
      ],
    }
  }
});
