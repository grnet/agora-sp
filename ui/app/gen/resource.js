import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/resources';

const { get, set, computed } = Ember;

export default AgoraGen.extend({
  modelName: 'resource',
  path: 'resources',
  resourceName: 'api/v2/resources',
  abilityStates: {
    organisation_owned: true,

    owned: computed('model.resource_admins_ids', 'user.id', function() {
      let ids = get(this, 'model.resource_admins_ids');
      let user_id = get(this, 'user.id') && get(this, 'user.id').toString();

      if (!ids) {
        return false;
      }
      let ids_arr = ids.split(',');

      return ids_arr.includes(user_id);
    }),
  },
  common: {
    validators: {
      rd_bai_0_id: [validate.presence(true)],
      rd_bai_1_name: [validate.presence(true)],
      rd_bai_2_service_organisation: [validate.presence(true)],
      rd_bai_4_webpage: [validate.format({ type: 'url' })],
      rd_mri_4_mulitimedia: [validate.format({ type: 'url', allowBlank: true })],
      rd_mri_3_logo: [validate.format({ type: 'url', allowBlank: true })],
      rd_gla_1_geographical_availability: [validate.presence(true)],
      rd_gla_2_language: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'resource.menu',
    },
    menu: {
      label: 'resource.menu',
      icon: 'bookmark',
      order: 1,
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'resource.placeholders.search',
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
    fieldsets: EDIT_FIELDSETS,
  },
  create: {
    fieldsets: CREATE_FIELDSETS,

    // If the user creating the Resource is a serviceadmin, the
    // rd_bai_2_service_organisation should be prefilled with
    // user's organisation
    getModel(params) {
      const store = get(this, 'store');
      const role = get(this, 'session.session.authenticated.role')
      const org_id = get(this, 'session.session.authenticated.organisation')
      if (role === 'serviceadmin') {

        let org = store.findRecord('provider', org_id);
        return org.then(function(organisation) {
          return store.createRecord('resource', {
            rd_bai_2_service_organisation: organisation
          })
        })

      }
      return store.createRecord('resource');
    },
    onSubmit(model) {
      this.transitionTo('resource.record.edit', model);
    },
  },
});
