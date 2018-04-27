import Ember from 'ember';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import ENV from '../config/environment';
import { AgoraGen } from '../lib/common';
import { approveServiceOwnership, rejectServiceOwnership } from '../utils/common/actions';

const CHOICES = ENV.APP.resources;

const {
  get,
} = Ember;

export default AgoraGen.extend({
  modelName: 'service-owner',
  order: 100,
  path: 'service-owners',
  resourceName: 'api/v2/service-owners',
  common: {
    validators: {
      service: [validate.presence(true)],
      owner: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'service_owner.menu',
    },
    menu: {
      label: 'service_owner.menu',
      group: {
        name: 'user-information',
        label: 'group_menu.user_information',
        order: 400,
      },
    },
    row: {
      fields: [
        'service_name',
        'owner_full_name',
        'owner_email',
        'state'
      ],
      actions: ['gen:details', 'remove', 'approveServiceOwnership', 'rejectServiceOwnership'],
      actionsMap: {
        rejectServiceOwnership,
        approveServiceOwnership,
      },
    },
    sort: {
      serverside: false,
      active: true,
      fields: ['service.name', 'owner.username', 'owner.email', 'state'],
    },
    filter: {
      active: true,
      serverSide: true,
      search: false,
      meta: {
        fields: [
          field('state', {
            type: 'select',
            choices: CHOICES.SERVICE_OWNERSHIP_STATES,
          }),
          field(
            'owner', {
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

      return store.createRecord('service-owner', {
        state: 'approved',
      })
    },
    fields : ['owner', 'service'],
  },
});
