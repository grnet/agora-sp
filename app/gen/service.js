import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'service',
  resourceName: 'service',
  auth: true,
  path: 'services',
  list: {
    layout: 'table',
    page: {
      title: 'Services'
    },
    menu: {
      title: 'Services'
    },
    row: {
      fields: [
        'name',
        'service_area',
        'short_description',
        'service_trl'
      ]
    }
  }
});
