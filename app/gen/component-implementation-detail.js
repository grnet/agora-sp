import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'component-implementation-detail',
  resourceName: 'api/v2/component-implementation-details',
  path: 'component-implementation-details',
  order: 5,
  list: {
    layout: 'table',
    page: {
      title: 'Component Implementation Details'
    },
    menu: {
      label: 'Component Implementation Details'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'version',
        'component_implementation_id.name',
        'component_id.name'
      ]
    },
  }
});
