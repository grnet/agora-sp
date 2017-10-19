import Ember from 'ember';
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
  },
  create: {
    //provide url params with this magic trick
    routeMixins: {
      queryParams: {'service': { refreshModel: true }}
    },
    //prepopulate a field from a query param
    getModel(params) {
      const store = Ember.get(this, 'store');
      //prepopulate field only if query param exists
      if(params.service) {
        //get the service item from the id provided from query param
        let service = store.findRecord('service-item', params.service);
        return service.then(function(service){
          //create a record with the model field prepopulated
          return store.createRecord('service-version', {
            id_service: service
          });
        })
      }
    }
  }
});
