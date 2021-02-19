import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/subcategory';

export default AgoraGen.extend({
  modelName: 'subcategory',
  path: 'subcategories',
  resourceName: 'api/v2/subcategories',
  common: {
    validators: {
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'subcategory.menu',
    },
    menu: {
      label: 'subcategory.menu',
      icon: 'style',
      group: 'class_settings',
      order: 52,
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },
    filter: {
      active: true,
      serverSide: true,
      search: true,
      searchPlaceholder: 'subcategory.placeholders.search',
      meta: {
        fields: [
          field(
            'category', {
              modelName:'category',
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
  },
});
