import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'component-implementation-detail-link',
  resourceName: 'api/v2/component-implementation-detail-links',
  path: 'component-implementation-detail-links',
  order: 6,
  list: {
    layout: 'table',
    page: {
      title: 'Component Implementation Detail Links'
    },
    menu: {
      label: 'Component Implementation Detail Links'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'configuration_parameters',
        'service_component_implementation_detail_id.version',
        'service_id.name',
        'service_details_id.version'
      ]
    },
  }
});
