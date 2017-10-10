import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'institution',
  path: 'institutions',
  resourceName: 'api/v2/institutions',
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
