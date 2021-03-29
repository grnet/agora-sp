import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import { AgoraGen, httpValidator } from '../lib/common';
import ENV from '../config/environment';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  PROVIDER_TABLE_FIELDS
} from '../utils/common/provider';
import { publishProvider, unpublishProvider } from '../utils/common/actions';

const {
  computed,
  get,
}  = Ember;

const CHOICES = ENV.APP.resources;


export default AgoraGen.extend({
  modelName: 'provider',
  path: 'providers',
  resourceName: 'api/v2/providers',
  abilityStates: {
    // a provideradmin can edit the provider he belongs to
    update_organisation_owned: computed('role', 'user.organisation', 'model.id', function() {
      let role = get(this, 'role');
      if (role === 'provideradmin') {
        return get(this, 'user.organisation') === get(this, 'model.id');
      }
      return false;
    }),
  },
  common: {
    validators: computed('role', function() {
      let role = get(this, 'role');
      if ( role === 'superadmin') {
        return {
          epp_bai_0_id: [validate.presence(true)],
          epp_bai_1_name: [validate.presence(true)],
          epp_bai_3_website: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
          epp_mri_2_logo : [validate.format({ type: 'url', allowBlank: true }), httpValidator],
          epp_mri_3_multimedia: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
        }
      } else {
        return {
          epp_bai_0_id: [validate.presence(true)],
          epp_bai_1_name: [validate.presence(true)],
          epp_bai_2_abbreviation: [validate.presence(true)],
          epp_bai_3_website: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
          epp_loi_1_street_name_and_number: [validate.presence(true)],
          epp_loi_2_postal_code: [validate.presence(true)],
          epp_loi_3_city: [validate.presence(true)],
          epp_loi_5_country_or_territory: [validate.presence(true)],
          epp_mri_1_description : [validate.presence(true)],
          epp_mri_2_logo : [validate.format({ type: 'url', allowBlank: false }), httpValidator],
          epp_mri_3_multimedia: [validate.format({ type: 'url', allowBlank: true }), httpValidator],
          epp_cli_1_scientific_domain: [validate.presence(true)],
          epp_cli_2_scientific_subdomain: [validate.presence(true)],
        }
      }
    }),
  },
  list: {
    page: {
      title: 'provider.menu'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'publishProvider', 'unpublishProvider', 'remove'],
      actionsMap: {
        publishProvider,
        unpublishProvider,
      },
      fields: PROVIDER_TABLE_FIELDS,
    },
    menu: {
      label: 'provider.menu',
      order: 50,
      icon: 'account_balance'

    },
    filter: {
      active: true,
      meta: {
        fields: [
          field('state', {
            type: 'select',
            choices: CHOICES.PROVIDER_STATES,
          })
        ],
      },
      serverSide: true,
      search: true,
      searchPlaceholder: 'provider.placeholders.search',
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['epp_bai_1_name', 'epp_bai_0_id', 'epp_bai_2_abbreviation']
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
  }
});
