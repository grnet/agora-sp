import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'institution',
  auth: true,
  path: 'institutions',
  resourceName: 'institutions',
  list: {
    layout: 'table',
    page: {
      title: 'Institutions'
    },
    menu: {
      label: 'Institutions'
    },
  }
});
