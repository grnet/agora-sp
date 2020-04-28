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
      name: [validate.presence(true)],
      contact: [validate.format({type: 'email', allowBlank: true})],
      pd__1_geographical_availability: [validate.presence(true)],
      pd_loi_1_street_name_and_number: [validate.presence(true)],
      pd_loi_2_postal_code: [validate.presence(true)],
      pd_loi_3_city: [validate.presence(true)],
      pd_loi_5_country_or_territory: [validate.presence(true)],

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
      group: {
        name: 'user-information',
        order: 100,
        label: 'search',
      },

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
