import Ember from 'ember';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import ENV from '../config/environment';
import { AgoraGen } from '../lib/common';
import {
  approveResourceAdminship,
  rejectResourceAdminship,
  undoResourceAdminship,
} from '../utils/common/actions';

const CHOICES = ENV.APP.resources;

const {
  computed,
  get,
} = Ember;

export default AgoraGen.extend({
  modelName: 'resource-admin',
  order: 100,
  path: 'resource-admins',
  resourceName: 'api/v2/resource-admins',
  abilityStates: {
    check_create_other: true,
    check_create_other_own_organisation: true,
 },
  common: {
    validators: {
      resource: [validate.presence(true)],
      admin: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'resource_admin.menu',
    },
    menu: {
      label: 'resource_admin.menu',
      order: 400,
      icon: 'people',
    },
    row: {
      fields: [
        'resource_name',
        field('admin_full_name', { label: 'resource_admin.fields.admin_full_name' }),
        'admin_email',
        'state',
      ],
      actions: ['gen:details', 'remove', 'approveResourceAdminship', 'rejectResourceAdminship', 'undoResourceAdminship'],
      actionsMap: {
        rejectResourceAdminship,
        approveResourceAdminship,
        undoResourceAdminship,
      },
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['resource_name', 'admin_email', 'state'],
    },
    filter: {
      active: true,
      serverSide: true,
      search: false,
      meta: {
        fields: [
          field('state', {
            type: 'select',
            choices: CHOICES.SERVICE_ADMINSHIP_STATES,
          }),
          field(
            'resource', {
              modelName:'resource',
              type: 'model',
              displayAttr: 'erp_bai_name',
            }
          ),
        ],
      },
    },
  },
  create: {
    getModel(params) {
      let store = get(this, 'store');

      return store.createRecord('resource-admin', {
        state: 'approved',
      });
    },
    fields : computed('user.role', function() {
      let user_org_id = get(this, 'session.session.authenticated.organisation');
      let role = get(this, 'session.session.authenticated.role');
      let resource = 'resource';

      if (role === 'provideradmin') {
        resource = field('resource', {
          query: (table, store, field, params) => {
            return store.query('resource', { erp_bai_service_organisation: user_org_id });
          },
       })
      }

      return [
        field('admin', {
          query: (table, store, field, params) => {
            return store.query('custom-user', { role: 'serviceadmin' });
          },
        }),
        resource,
      ];
    }),
  },
  details: {
    fieldsets: [{
      label: 'resource_admin.cards.basic_information',
      fields: [
        'state',
        'created_at',
        'updated_at',
      ],
    }, {
      label: 'resource_admin.cards.admin_info',
      fields: [
        'admin_full_name',
        'admin_email',
        'admin_id',
      ],
    }, {
      label: 'resource_admin.cards.resource_info',
      fields: [
        'resource_name',
        'resource.id',
      ],
    }],
  },
});
