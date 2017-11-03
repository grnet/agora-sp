import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'component-implementation',
  resourceName: 'api/v2/component-implementations',
  path: 'component-implementations',
  order: 4,
  list: {
    layout: 'table',
    page: {
      title: 'Component Implementations'
    },
    menu: {
      label: 'Component Implementations'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'name',
        'description',
        'component_id.name'
      ]
    },
  }
});
