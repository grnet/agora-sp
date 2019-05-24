import Ember from 'ember';
import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import validate from 'ember-gen/validate';
import {
  CREATE_FIELDSETS,
  CREATE_FIELDSETS_LIMITED,
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
} from '../utils/common/service-version';

const {
  get,
  computed,
} = Ember;

export default AgoraGen.extend({
  modelName: 'service_version',
  order: 2,
  path: 'service-versions',
  resourceName: 'api/v2/service-versions',
  common: {
    validators: {
      id_service: [validate.presence(true)],
      version: [validate.presence(true)],
      status : [validate.presence(true)],
      sla_url: [validate.format({ type: 'url', allowBlank: true })],
      terms_of_use_url: [validate.format({ type: 'url', allowBlank: true })],
      privacy_policy_url: [validate.format({ type: 'url', allowBlank: true })],
      user_manual: [validate.format({ type: 'url', allowBlank: true })],
      admin_manual: [validate.format({ type: 'url', allowBlank: true })],
      monitoring_url: [validate.format({ type: 'url', allowBlank: true })],
      maintenance_url: [validate.format({ type: 'url', allowBlank: true })],
    },
  },
  abilityStates: {
    create_owns_service: computed('role', 'session.session.authenticated.admins_services', function(){
        if (get(this, 'role') === 'serviceadmin') {
          return  get(this, 'session.session.authenticated.admins_services');
        }
        return true;
    }),
    update_owns_service: computed('model.service_admins_ids', 'user.id', function(){
      let ids = get(this, 'model.service_admins_ids');
      let user_id = get(this, 'user.id').toString();

      if (!ids) { return false; }
      let ids_arr = ids.split(',');

      return ids_arr.includes(user_id);
    }),
  },
  list: {
    page: {
      title: 'service_version.menu'
    },
    menu: {
      label: 'service_version.menu'
    },
    sort: {
      serverSide: true,
      active: true,
      fields: SORT_FIELDS
    },
    filter: {
      active: true,
      serverSide: true,
      search: true,
      searchPlaceholder: 'service_version.placeholders.search',
      meta: {
        fields: [
          field(
            'id_service', {
              modelName:'service_item',
              type: 'model',
              label: 'Service Name',
              displayAttr: 'name'
            }
          ),
          field(
            'status', {
              modelName:'service_status',
              type: 'model',
              label: 'Service Status',
              displayAttr: 'value'
            }
          ),
          field('is_in_catalogue', {
            type: 'boolean',
            label: 'service_version.fields.in_catalogue',
          }),
          field('visible_to_marketplace', {
            type: 'boolean',
            label: 'service_version.fields.visible_to_marketplace',
          }),

        ]
      }
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
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
        //save the service id in order to use it in onSubmit
        //model.set('param_service', params.service);
        //get the service item from the id provided from query param
        let service = store.findRecord('service-item', params.service);
        return service.then(function(service){
          //create a record with the model field prepopulated
          return store.createRecord('service-version', {
            id_service: service,
            param_service: params.service
          });
        });
      }

      return store.createRecord('service-version', {});
    },
    fieldsets: computed('', function() {
      if (get(this, 'role') === 'serviceadmin') {
        return CREATE_FIELDSETS_LIMITED;
      } else {
        return CREATE_FIELDSETS;
      }
    }),
    onSubmit(model) {
      const param = model.get('param_service');
      if(param) {
        this.transitionTo(`/services/${param}`);
      } else {
        this.transitionTo('service-version.record.index', model);
      }
    }
  },
  edit: {
    fieldsets: computed('', function() {
      if (get(this, 'role') === 'serviceadmin') {
        return CREATE_FIELDSETS_LIMITED;
      } else {
        return CREATE_FIELDSETS;
      }
    }),
  },
  details: {
    preloadModels: ['service-item'],
    fieldsets: DETAILS_FIELDSETS,
  }
});
