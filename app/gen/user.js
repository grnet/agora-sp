import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'user',
  path: 'users',
  resourceName: 'users',
  list: {
    menu: {
      label: 'Users',
    }
  }
});
