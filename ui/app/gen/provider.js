import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import { AgoraGen } from '../lib/common';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS
} from '../utils/common/provider';


export default AgoraGen.extend({
  modelName: 'provider',
  path: 'providers',
  resourceName: 'api/v2/providers',
  common: {
    validators: {
      pd_bai_0_id: [validate.presence(true)],
      pd_bai_1_name: [validate.presence(true)],
      pd_bai_2_abbreviation: [validate.presence(true)],
      pd_bai_4_website: [validate.format({ type: 'url', allowBlank: true })],
      pd__1_geographical_availability: [validate.presence(true)],
      pd_loi_1_street_name_and_number: [validate.presence(true)],
      pd_loi_2_postal_code: [validate.presence(true)],
      pd_loi_3_city: [validate.presence(true)],
      pd_loi_5_country_or_territory: [validate.presence(true)],
      pd_mri_1_description : [validate.presence(true)],
      pd_mri_2_logo : [validate.format({ type: 'url', allowBlank: false })],
      pd_mri_3_multimedia: [validate.format({ type: 'url', allowBlank: true })],
    },
  },
  list: {
    page: {
      title: 'provider.menu'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'name',
        'contact',
        field('short_desc', {
          label: 'provider.fields.description',
        }),
      ]
    },
    menu: {
      label: 'provider.menu',
      order: 50,
      icon: 'account_balance'

    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'service_item.placeholders.search',
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['name']
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
    onSubmit(model) {
      this.transitionTo('provider.record.edit', model);
    },

  }


});
