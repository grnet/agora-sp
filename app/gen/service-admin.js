import Ember from 'ember';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import ENV from '../config/environment';
import { AgoraGen } from '../lib/common';
import {
  approveServiceAdminship,
  rejectServiceAdminship,
  undoServiceAdminship,
} from '../utils/common/actions';

const CHOICES = ENV.APP.resources;

const {
  get,
} = Ember;

export default AgoraGen.extend({
  modelName: 'service-admin',
  order: 100,
  path: 'service-admins',
  resourceName: 'api/v2/service-admins',
  abilityStates: {
    check_create_other: true,
  },
  common: {
    validators: {
      service: [validate.presence(true)],
      admin: [validate.presence(true)],
    },
  },
  list: {
    getModel(params) {
      params = params || {};
      return this.store.query('service-admin', params).then( (sa) => {
        let user_id = get(this, 'session.session.authenticated.id');
        let res = sa.filter(el => get(el, 'admin_id') != user_id);
        return res;
      });
    },
    page: {
      title: 'service_admin.menu',
    },
    menu: {
      label: 'service_admin.menu',
      group: {
        name: 'user-information',
        label: 'group_menu.user_information',
        order: 400,
      },
    },
    row: {
      fields: [
        'service_name',
        field('admin_full_name', {label: 'service_admin.fields.admin_full_name'}),
        'admin_email',
        'state'
      ],
      actions: ['gen:details', 'remove', 'approveServiceAdminship', 'rejectServiceAdminship', 'undoServiceAdminship'],
      actionsMap: {
        rejectServiceAdminship,
        approveServiceAdminship,
        undoServiceAdminship,
      },
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['service_name', 'admin_email', 'state'],
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
            'service', {
              modelName:'service_item',
              type: 'model',
              displayAttr: 'name',
            }
          ),
        ],
      },
    },
  },
  create: {
    getModel(params) {
      let store = get(this, 'store');
      return store.createRecord('service-admin', {
        state: 'approved',
      })
    },
    fields : [
      field('admin', {
        query: (table, store, field, params) => {
          return store.query('custom-user', { role: 'serviceadmin' });
        },
      }),
      'service',
    ],
  },
});
