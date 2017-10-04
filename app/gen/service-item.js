import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'service-item',
  resourceName: 'service',
  auth: true,
  path: 'services',
  list: {
    layout: 'table',
    page: {
      title: 'Services'
    },
    menu: {
      label: 'Services'
    },
    row: {
      fields: [
        'name',
        'service_area',
        'short_description',
        'service_trl.value'
      ]
    }
  }
});
