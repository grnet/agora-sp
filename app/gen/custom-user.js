import { AgoraGen } from '../lib/common';
import validate from 'ember-gen/validate';
import {
  CREATE_OR_EDIT_FIELDSETS,
  DETAILS_FIELDSETS
} from '../utils/common/custom-user';


export default AgoraGen.extend({
  modelName: 'custom-user',
  order: 600,
  path: 'custom-users',
  resourceName: 'api/v2/custom-users',
  common: {
    fieldsets: CREATE_OR_EDIT_FIELDSETS,
    validators: {
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
        'is_staff',
        'is_active',
        'role',
      ]
    },
    menu: {
      label: 'custom_user.menu',
    },
    sort: {
      serverside: false,
      active: true,
      fields: ['username', 'email', 'is_active', 'is_staff']
    },
  },
  details: {
    fieldsets: DETAILS_FIELDSETS
  }
});
