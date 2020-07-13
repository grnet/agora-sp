import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/subdomain';

export default AgoraGen.extend({
  modelName: 'subdomain',
  path: 'subdomains',
  resourceName: 'api/v2/subdomains',
  common: {
    validators: {
      id: [validate.presence(true)],
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'subdomain.menu',
    },
    menu: {
      label: 'subdomain.menu',
      icon: 'style',
      group: 'class_settings',
      order: 41,
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },

    filter: {
      active: true,
      serverSide: true,
      search: false,
      searchPlaceholder: 'subdomain.placeholders.search',
      meta: {
        fields: [
          field(
            'domain', {
              modelName:'domain',
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
      sortBy: 'name',
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
      this.transitionTo('subdomain.record.edit', model);
    },
  },
});
