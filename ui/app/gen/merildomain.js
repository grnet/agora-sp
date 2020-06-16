import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/merildomain';

export default AgoraGen.extend({
  modelName: 'merildomain',
  path: 'merildomains',
  resourceName: 'api/v2/merildomains',
  common: {
    validators: {
      id: [validate.presence(true)],
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'merildomain.menu',
    },
    menu: {
      label: 'merildomain.menu',
      icon: 'local_offer',
      group: 'settings',
      order: 950,
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'merildomain.placeholders.search',
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
      this.transitionTo('merildomain.record.edit', model);
    },
  },
});
