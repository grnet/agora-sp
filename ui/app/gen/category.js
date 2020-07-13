import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/category';

export default AgoraGen.extend({
  modelName: 'category',
  path: 'categories',
  resourceName: 'api/v2/categories',
  common: {
    validators: {
      id: [validate.presence(true)],
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'category.menu',
    },
    menu: {
      label: 'category.menu',
      icon: 'style',
      group: {
        name: 'class_settings',
        label: 'group_menu.class_settings',
        icon: 'settings',
        order: 520,
      },
      order: 511,
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },
    filter: {
      active: true,
      serverSide: true,
      search: true,
      searchPlaceholder: 'category.placeholders.search',
      meta: {
        fields: [
          field(
            'supercategory', {
              modelName:'supercategory',
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
      this.transitionTo('category.record.edit', model);
    },
  },
});
