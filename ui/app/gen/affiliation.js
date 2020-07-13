import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/affiliation';

export default AgoraGen.extend({
  modelName: 'affiliation',
  path: 'affiliations',
  resourceName: 'api/v2/affiliations',
  common: {
    validators: {
      id: [validate.presence(true)],
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'affiliation.menu',
    },
    menu: {
      label: 'affiliation.menu',
      icon: 'flag',
      group: {
        name: 'provider_settings',
        label: 'group_menu.provider_settings',
        icon: 'settings',
        order: 510,
      },
      order: 30,
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS,
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'common.placeholders.search',
    },
    sort: {
      serverSide: true,
      active: true,
      sortBy: 'name',
      fields: ['name'],
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
      this.transitionTo('affiliation.record.edit', model);
    },
  },
});
