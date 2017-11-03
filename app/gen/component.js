import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'component',
  resourceName: 'api/v2/components',
  path: 'components',
  order: 3,
  list: {
    layout: 'table',
    page: {
      title: 'Components'
    },
    menu: {
      label: 'Components'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'name',
        'description',
        'logo'
      ]
    },
  }
});
