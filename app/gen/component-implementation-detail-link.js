import gen from 'ember-gen/lib/gen';
import { field } from 'ember-gen';
import {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  TABLE_FILTERS
} from '../utils/common/component-implementation-detail-link';

export default gen.CRUDGen.extend({
  modelName: 'component-implementation-detail-link',
  resourceName: 'api/v2/component-implementation-detail-links',
  path: 'component-implementation-detail-links',
  order: 4,
  list: {
    layout: 'table',
    page: {
      title: 'Component Implementation Detail Links'
    },
    menu: {
      label: 'Component Implementation Detail Links',
      group: 'components'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS
    },
    filter: {
      active: true,
      serverSide: true,
      search: false,
      meta: {
        fields: TABLE_FILTERS
      }
    },
  },
  details: {
    fieldsets: DETAILS_FIELDSETS
  },
  edit: {
    routeMixins: {
      queryParams: {'service_version': { refreshModel: true }}
    },
    preloadModels: [
      'component',
      'component-implementation',
      'component-implementation-detail',
      'component-implementation-detail-link'
    ],
    getModel: function(params, model) {
      /*
       * In order to preload all 3 selects with the defaul values, we need to chain
       * a few api calls. First we get the first reversed level of
       * `service_component_implementation_detail_id` in order to have
       * the other two previous values, `component_id` and
       * `component_implementation_id`, and then set the default values to each
       * field of the model. Lastly, we return the model.
      */

      if(params && 'service_version' in params) {
        model.set('param_service_version', params.service_version);
      }

      return model.get('service_component_implementation_detail_id').then(function(resp) {
        let promises = [
          resp.get('component_id'),
          resp.get('component_implementation_id')
        ];

        var promise = Ember.RSVP.all(promises).then((res) => {
          model.set('service_component', res[0]);
          model.set('service_component_implementation', res[1]);
        });

        return promise.then(function() {
          return model;
        });
      });
    },
    fieldsets: EDIT_FIELDSETS,
    onSubmit(model) {
      //const params = Ember.getOwner(this).lookup('router:main').get('currentState.routerJsState.fullQueryParams');
      const param = model.get('param_service_version');
      if(param) {
        this.transitionTo(`/service-versions/${param}`);
      }
    },
  },
  create: {
    //provide url params with this magic trick
    routeMixins: {
      queryParams: {
        'service': {
          refreshModel: true
        },
        'service_version': {
          refreshModel: true
        }
      }
    },
    //prepopulate a field from a query param
    getModel(params) {
      const store = Ember.get(this, 'store');
      //prepopulate field only if query param exists
      if(params.service_version && params.service) {
        //get the service & service version from the id provided from query param
        let data = {};

        //save the service version in order to redirect onsubmit
        data.param_service_version = params.service_version;

        let promises = [
          store.findRecord('service-item', params.service),
          store.findRecord('service-version', params.service_version)
        ];

        var promise = Ember.RSVP.all(promises).then((res) => {
          data.service_id = res[0];
          data.service_details_id = res[1];
        });

        return promise.then(function() {
          return store.createRecord('component_implementation_detail_link', data);
        });
      }

      return store.createRecord('service-version', {});
    },
    onSubmit(model) {
      const param = model.get('param_service_version');
      if(param) {
        this.transitionTo(`/service-versions/${param}`);
      }
    },
    fieldsets: CREATE_FIELDSETS
  }
});
