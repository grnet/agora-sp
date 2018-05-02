import Ember from 'ember';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import { AgoraGen } from '../lib/common';
import { applyServiceAdminship } from '../utils/common/actions';
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
      search: false,
      meta: {
        fields: [
          field(
            'service_trl', {
              modelName:'service_trl',
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
      serverSide: false,
      active: true,
      fields: SORT_FIELDS,
    },
  },
  details: {
    actions: ['gen:details', 'gen:edit', 'remove', 'applyServiceAdminship'],
    actionsMap: {
      applyServiceAdminship,
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
    // tmp until updated apimas
    // Service membership creating will be normally handled by backend
    onSubmit(model) {
      let user_id = get(this, 'session.session.authenticated.id');
      let service = model;
      let store = get(model, 'store');
      let admin = store.findRecord('custom-user', user_id);

      return admin.then(admin => {
        let so = store.createRecord('service-admin', {
          service,
          admin,
          state: 'approved',
        })

        so.save();
      })
    },
    // end tmp
  },
});
