import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import ENV from '../config/environment';
import validate from 'ember-gen/validate';
import {
  CREATE_OR_EDIT_FIELDSETS,
  DETAILS_FIELDSETS
} from '../utils/common/custom-user';

const CHOICES = ENV.APP.resources;


export default AgoraGen.extend({
  modelName: 'custom-user',
  order: 600,
  path: 'custom-users',
  resourceName: 'api/v2/custom-users',
  abilityStates: {
    'me': true,
  },
  common: {
    fieldsets: CREATE_OR_EDIT_FIELDSETS,
    validators: {
      role: [validate.presence(true)],
      username: [validate.presence(true)],
      email: [validate.format({type: 'email'})],
    },
  },
  list: {
    page: {
      title: 'custom_user.menu'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'username',
        'full_name',
        'email',
        field('organisation.epp_bai_1_name', {
          label: 'custom_user.fields.organisation',
        }) ,
        field('role_verbose', {
          label: 'custom_user.fields.role',
        }),
      ]
    },
    menu: {
      label: 'custom_user.menu',
      icon : 'face',
      order: '500',
    },
    filter: {
      active: true,
      serverSide: true,
      search: true,
      searchPlaceholder: 'custom_user.placeholders.search',
      meta: {
        fields: [
          field('organisation', {
            modelName:'provider',
            label: 'custom_user.fields.organisation',
            type: 'model',
            displayAttr: 'epp_bai_1_name',
          }),
          field('role', {

    type: 'select',
    choices: CHOICES.USER_ROLES,
          })
        ],
      },
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['username', 'email', 'is_active', 'role']
    },
  },
  details: {
    fieldsets: DETAILS_FIELDSETS
  }
});
