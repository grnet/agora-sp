import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  CREATE_FIELDSETS_LIMITED,
  EDIT_FIELDSETS,
  EDIT_FIELDSETS_LIMITED,
  TABLE_FILTERS,
} from '../utils/common/component-implementation-detail-link';

const {
  get,
  computed,
} = Ember;


export default AgoraGen.extend({
  modelName: 'component-implementation-detail-link',
  resourceName: 'api/v2/component-implementation-detail-links',
  path: 'component-implementation-detail-links',
  order: 4,
  abilityStates: {
    unique: true,
    update_unique: true,
    create_owns_service_unique: computed('role', 'session.session.authenticated.admins_services', function(){
        if (get(this, 'role') === 'serviceadmin') {
          return  get(this, 'session.session.authenticated.admins_services');
        }
        return true;
    }),
    update_owns_service_unique: computed('model.service_admins_ids', 'user.id', function(){
      let ids = get(this, 'model.service_admins_ids');
      let user_id = get(this, 'user.id').toString();

      if (!ids) { return false; }
      let ids_arr = ids.split(',');

      return ids_arr.includes(user_id);
    }),
  },
  common: {
    validators: {
      service_component_implementation_detail_id: [validate.presence(true)],
      service_details_id: [validate.presence(true)],
      service_id: [validate.presence(true)],
      my_service: [validate.presence(true)],
      my_service_version: [validate.presence(true)],
      service_type: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'cidl.menu',
    },
    menu: {
      label: 'cidl.menu',
      group: 'components',
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },
    filter: {
      active: true,
      serverSide: true,
      search: true,
      searchPlaceholder: 'cidl.placeholders.search',
      meta: {
        fields: TABLE_FILTERS,
      },
    },
    sort: {
      serverSide: true,
      active: true,
      fields: SORT_FIELDS,
    },
  },
  details: {
    fieldsets: DETAILS_FIELDSETS,
  },
  edit: {
    routeMixins: {
      queryParams: { 'service_version': { refreshModel: true } },
    },
    preloadModels: [
      'component',
      'component-implementation',
      'component-implementation-detail',
      'component-implementation-detail-link',
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
          resp.get('component_implementation_id'),
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
    fieldsets: computed('', function() {
      if (get(this, 'role') === 'serviceadmin') {
        return EDIT_FIELDSETS_LIMITED;
      } else {
        return EDIT_FIELDSETS;
      }
    }),

    onSubmit(model) {
      // const params = Ember.getOwner(this).lookup('router:main').get('currentState.routerJsState.fullQueryParams');
      const param = model.get('param_service_version');

      if(param) {
        this.transitionTo(`/service-versions/${param}`);
      }
    },
  },
  create: {
    // provide url params with this magic trick
    routeMixins: {
      queryParams: {
        'service': {
          refreshModel: true,
        },
        'service_version': {
          refreshModel: true,
        },
      },
    },
    // prepopulate a field from a query param
    getModel(params) {
      const store = Ember.get(this, 'store');

      let role =  get(this, 'session.session.authenticated.role'),
        is_serviceadmin = role === 'serviceadmin';

      // prepopulate field only if query param exists
      if(params.service_version && params.service) {
        // get the service & service version from the id provided from query param
        let data = {};

        // save the service version in order to redirect onsubmit
        data.param_service_version = params.service_version;

        let promises = [
          store.findRecord('service-item', params.service),
          store.findRecord('service-version', params.service_version),
        ];

        // my-service is needed for serviceadmins
        if (is_serviceadmin) {
          promises.push(store.findRecord('my-service', params.service));
        }

        var promise = Ember.RSVP.all(promises).then((res) => {
          data.service_id = res[0];
          data.service_details_id = res[1];
          // my_service_version is populated by service-version promise, while
          // my_service from my-service promise
          if (is_serviceadmin) {
            data.my_service = res[2];
            data.my_service_version = res[1];
          }
        });

        return promise.then(function() {
          return store.createRecord('component_implementation_detail_link', data);
        });
      }

      return store.createRecord('component_implementation_detail_link', {});
    },
    onSubmit(model) {
      const param = model.get('param_service_version');

      if(param) {
        this.transitionTo(`/service-versions/${param}`);
      } else {
        this.transitionTo('component-implementation-detail-link.record.index', model);
      }
    },
    fieldsets: computed('', function() {
      if (get(this, 'role') === 'serviceadmin') {
        return CREATE_FIELDSETS_LIMITED;
      } else {
        return CREATE_FIELDSETS;
      }
    }),
  },
});
