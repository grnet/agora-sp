import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'user',
  auth: true,
  path: 'users',
  resourceName: 'users',
  list: {
    layout: 'table',
  }
});
