import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'service_version',
  order: 100,
  path: 'service-versions',
  resourceName: 'api/v2/service-versions',
  list: {
    layout: 'table',
    page: {
      title: 'Service Versions'
    },
    menu: {
      label: 'Service Versions'
    },
    row: {
      fields: [
        //'id',
        'version',
        'status.value',
        'is_in_catalogue',
        'id_service.name'
      ],
    }
  }
});
