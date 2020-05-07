import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/structure';

export default AgoraGen.extend({
  modelName: 'structure',
  path: 'structures',
  resourceName: 'api/v2/structures',
  common: {
    validators: {
      id: [validate.presence(true)],
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'structure.menu',
    },
    menu: {
      label: 'structure.menu',
      icon: 'apartment',
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
      searchPlaceholder: 'structure.placeholders.search',
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
      this.transitionTo('structure.record.edit', model);
    },
  },
});
