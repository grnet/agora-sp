import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import { AgoraGen, httpValidator } from '../lib/common';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/resources';

import {
  postResourceEOSC,
  putResourceEOSC,
  approveResourceEOSC,
  rejectResourceEOSC,
} from '../utils/common/eosc-portal';

import {
  applyResourceAdminship,
  revokeResourceAdminship,
  informAdminshipRejected,
  publishResource,
  unpublishResource,
} from '../utils/common/actions';
import ENV from '../config/environment';

const { get, set, computed } = Ember;

const CHOICES = ENV.APP.resources;

export default AgoraGen.extend({
  modelName: 'resource',
  path: 'resources',
  resourceName: 'api/v2/resources',
  abilityStates: {
    // a servicedmin can create a resource if he belongs to an organisation
    create_organisation_owned: computed('role', 'user.organisation', function() {
      let role = get(this, 'role');
      if (role === 'serviceadmin') {
        return get(this, 'user.organisation');
      }
      return true;
    }),

    // a provideradmin can update a resource if he belongs to an organisation
    update_organisation_owned: computed('role', 'user.organisation', 'model.erp_bai_service_organisation',  function() {
      let role = get(this, 'role');
      let resource_org = get(this, 'model.erp_bai_service_organisation.id');
      let user_org = get(this, 'user.organisation');
      if (role === 'provideradmin') {
        return resource_org === user_org;
      }
    }),
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
      erp_bai_id: [validate.presence(true)],
      erp_bai_abbreviation: [validate.presence(true)],
      erp_bai_name: [validate.presence(true)],
      erp_bai_service_organisation: [validate.presence(true)],
      erp_bai_webpage: [validate.format({ type: 'url', allowBlank:true }), httpValidator],
      erp_cli_scientific_domain: [validate.presence(true)],
      erp_cli_scientific_subdomain: [validate.presence(true)],
      erp_cli_category: [validate.presence(true)],
      erp_cli_subcategory: [validate.presence(true)],
      erp_gla_geographical_availability: [validate.presence(true)],
      erp_gla_language: [validate.presence(true)],
      erp_coi_helpdesk_email: [validate.format({type: 'email', allowBlank: true})],
      erp_coi_security_contact_email: [validate.format({type: 'email', allowBlank: true})],
      erp_mgi_helpdesk_webpage: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
      erp_mgi_user_manual: [validate.format({type: 'url', allowBlank: true}), httpValidator],
      erp_mgi_terms_of_use: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
      erp_mgi_privacy_policy: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
      erp_mgi_access_policy: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
      erp_mgi_sla_specification: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
      erp_mgi_training_information: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
      erp_mgi_status_monitoring: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
      erp_mgi_maintenance: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
      erp_mri_logo: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
      erp_fni_payment_model: [validate.format({ type: 'url', allowBlank:true }), httpValidator],
      erp_fni_pricing: [validate.format({ type: 'url', allowBlank:true }), httpValidator],
      erp_aoi_order: [validate.format({ type: 'url', allowBlank:true }), httpValidator],
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
      actions: [
        'gen:details',
        'gen:edit',
        'publishResource',
        'unpublishResource',
        //'approveResourceEOSC',
        'rejectResourceEOSC',
        'remove'
      ],
      actionsMap: {
        unpublishResource,
        publishResource,
        //approveResourceEOSC,
        rejectResourceEOSC
      },
      fields: TABLE_FIELDS,
    },
    sort: {
      serverSide: true,
      active: true,
      fields: SORT_FIELDS,
    },
    filter: {
      active: true,
      search: true,
      searchPlaceholder: 'resource.placeholders.search',
      serverSide: true,
      meta: {
        fields: [
          field('erp_bai_service_organisation', {
            modelName:'provider',
            label: 'resource.table.erp_bai_service_organisation',
            type: 'model',
            displayAttr: 'epp_bai_name',
          }),
          field('erp_mti_technology_readiness_level', {
            modelName:'trl',
            label: 'resource.table.erp_mti_technology_readiness_level',
            type: 'model',
            displayAttr: 'name',
          }),
          field('state', {
            type: 'select',
            choices: CHOICES.RESOURCE_STATES,
          })
        ],
      },
    },
  },
  details: {
    fieldsets: DETAILS_FIELDSETS,
    actions: [
      'gen:edit',
      'applyResourceAdminship',
      'revokeResourceAdminship',
      'informAdminshipRejected',
      'postResourceEOSC',
      'putResourceEOSC',
    ],
    actionsMap: {
      applyResourceAdminship,
      revokeResourceAdminship,
      informAdminshipRejected,
      postResourceEOSC,
      putResourceEOSC,
    },
  },
  edit: {
    fieldsets: EDIT_FIELDSETS,
  },
  create: {
    fieldsets: CREATE_FIELDSETS,

    // If the user creating the Resource is a serviceadmin or
    // a provideradmin, erp_bai_service_organisation should
    // be prefilled with user's organisation
    getModel(params) {
      const store = get(this, 'store');
      const role = get(this, 'session.session.authenticated.role')
      const org_id = get(this, 'session.session.authenticated.organisation')
      if (role === 'serviceadmin' || role === 'provideradmin') {

        let org = store.findRecord('provider', org_id);
        return org.then(function(organisation) {
          return store.createRecord('resource', {
            erp_bai_service_organisation: organisation
          })
        })

      }
      return store.createRecord('resource');
    },
  },
});
