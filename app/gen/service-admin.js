import Ember from 'ember';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import ENV from '../config/environment';
import { AgoraGen } from '../lib/common';
import { approveServiceAdminship, rejectServiceAdminship } from '../utils/common/actions';

const CHOICES = ENV.APP.resources;

const {
  get,
} = Ember;

export default AgoraGen.extend({
  modelName: 'service-admin',
  order: 100,
  path: 'service-admins',
  resourceName: 'api/v2/service-admins',
  common: {
    validators: {
      service: [validate.presence(true)],
      admin: [validate.presence(true)],
    },
  },
  list: {
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
        'admin_full_name',
        'admin_email',
        'state'
      ],
      actions: ['gen:details', 'remove', 'approveServiceAdminship', 'rejectServiceAdminship'],
      actionsMap: {
        rejectServiceAdminship,
        approveServiceAdminship,
      },
    },
    sort: {
      serverside: false,
      active: true,
      fields: ['service.name', 'admin.username', 'admin.email', 'state'],
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
            'admin', {
              modelName:'custom_user',
              type: 'model',
              displayAttr: 'username',
            }
          ),
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
    fields : ['admin', 'service'],
  },
});
