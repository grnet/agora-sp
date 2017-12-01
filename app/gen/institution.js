import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'institution',
  path: 'institutions',
  resourceName: 'api/v2/institutions',
  list: {
    page: {
      title: 'Institutions'
    },
    menu: {
      label: 'Institutions',
      group: 'user-information'
    },
  }
});
