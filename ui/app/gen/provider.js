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
