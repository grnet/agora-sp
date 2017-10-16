import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';

export default AgoraGen.extend({
  modelName: 'service_version',
  order: 2,
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
    filter: {
      active: true,
      serverSide: true,
      search: false,
      meta: {
        fields: [
          field(
            'id_service', {
              modelName:'service_item',
              type: 'model',
              displayAttr: 'name'
            }
          ),
          field(
            'status', {
              modelName:'service_status',
              type: 'model',
              displayAttr: 'value'
            }
          ),
        ]
      }
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
