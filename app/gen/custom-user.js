import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'custom-user',
  order: 100,
  path: 'custom-users',
  resourceName: 'api/v2/custom-users',
  list: {
    page: {
      title: 'Users'
    },
    menu: {
      label: 'Users',
      group: 'user-information'
    },
  }
});
