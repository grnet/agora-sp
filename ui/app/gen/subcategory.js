import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
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
      id: [validate.presence(true)],
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
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'subcategory.placeholders.search',
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
      this.transitionTo('subcategory.record.edit', model);
    },
  },
});
