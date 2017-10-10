import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'service-status',
  order: 100,
  path: 'service-status',
  resourceName: 'api/v2/service-status',
  list: {
    layout: 'table',
    page: {
      title: 'Service Status'
    },
    menu: {
      label: 'Service Status'
    },
    row: {
      fields: [
        //'id',
        'value',
        'order',
      ],
    }
  }
});
