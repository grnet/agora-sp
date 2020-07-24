import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/merilsubdomain';

export default AgoraGen.extend({
  modelName: 'merilsubdomain',
  path: 'merilsubdomains',
  resourceName: 'api/v2/merilsubdomains',
  common: {
    validators: {
      id: [validate.presence(true)],
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'merilsubdomain.menu',
    },
    menu: {
      label: 'merilsubdomain.menu',
      icon: 'style',
      group: 'provider_settings',
      order: 94,
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },

    filter: {
      active: true,
      serverSide: true,
      search: false,
      searchPlaceholder: 'merilsubdomain.placeholders.search',
      meta: {
        fields: [
          field(
            'domain', {
              modelName:'merildomain',
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
    fieldsets: DETAILS_FIELDSETS,
  },
  edit: {
    fieldsets: EDIT_FIELDSETS,
  },
  create: {
    fieldsets: CREATE_FIELDSETS,
    onSubmit(model) {
      this.transitionTo('merilsubdomain.record.edit', model);
    },
  },
});
