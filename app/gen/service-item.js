import Ember from 'ember';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import { AgoraGen } from '../lib/common';
import {
  applyServiceAdminship,
  revokeServiceAdminship,
  informAdminshipRejected,
} from '../utils/common/actions';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
} from '../utils/common/service-item';

const {
  get,
  computed,
} = Ember;

export default AgoraGen.extend({
  modelName: 'service-item',
  resourceName: 'api/v2/services',
  path: 'services',
  order: 1,
  abilityStates: {
    owned: computed('model.service_admins_ids', 'user.id', function(){
      let ids = get(this, 'model.service_admins_ids');
      let user_id = get(this, 'user.id').toString();

      if (!ids) { return false; }
      let ids_arr = ids.split(',');

      return ids_arr.includes(user_id);
    }),
  },
  common: {
    validators: {
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'service_item.menu',
    },
    menu: {
      label: 'service_item.menu',
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },
    filter: {
      active: true,
      serverSide: true,
      search: true,
      searchPlaceholder: 'service_item.placeholders.search',
      meta: {
        fields: [
          field(
            'service_trl', {
              modelName:'service_trl',
              label: 'service_trl.belongs.value',
              type: 'model',
              displayAttr: 'value',
            }
          ),
          field('internal', {type: 'boolean'}),
          field('customer_facing', {type: 'boolean'}),
          field(
            'service_area', {
              modelName:'service_area',
              type: 'model',
              displayAttr: 'name',
            }
          ),
        ],
      },
    },
    sort: {
      serverSide: true,
      active: true,
      fields: SORT_FIELDS,
    },
  },
  details: {
    actions: [
      'gen:details',
      'gen:edit',
      'remove',
      'applyServiceAdminship',
      'revokeServiceAdminship',
      'informAdminshipRejected',
    ],
    actionsMap: {
      applyServiceAdminship,
      revokeServiceAdminship,
      informAdminshipRejected,
    },
    fieldsets: DETAILS_FIELDSETS,
    page: {
      title: Ember.computed('model.name', function() {
        return Ember.get(this, 'model.name');
      }),
    },
  },
  edit: {
    fieldsets: EDIT_FIELDSETS,
  },
  create: {
    fieldsets: CREATE_FIELDSETS,
  },
});
