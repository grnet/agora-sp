import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
} from '../utils/common/network';

export default AgoraGen.extend({
  modelName: 'network',
  path: 'networks',
  resourceName: 'api/v2/networks',
  common: {
    validators: {
      id: [validate.presence(true)],
      name: [validate.presence(true)],
      abbreviation: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'network.menu',
    },
    menu: {
      label: 'network.menu',
      icon: 'device_hub',
      group: 'provider_settings',
      order: 32,
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
      sortBy: 'abbreviation',
      fields: ['name', 'abbreviation',],
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
