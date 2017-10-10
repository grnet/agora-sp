import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'service-item',
  resourceName: 'api/v2/services',
  path: 'services',
  list: {
    layout: 'table',
    page: {
      title: 'Services'
    },
    menu: {
      label: 'Services'
    },
    row: {
      fields: [
        'name',
        'service_area',
        'short_description',
        'service_trl.value'
      ]
    }
  }
});
