import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
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
      group: 'settings',
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'category.placeholders.search',
    },
    // Turned client-side sorting due to issues with sorting by domain foreign key. 
    // TODO: Mitigate the issue and re-enable server side sorting     
    sort: {
      serverSide: false,
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
      this.transitionTo('category.record.edit', model);
    },
  },
});
