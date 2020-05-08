import validate from 'ember-gen/validate';
import { AgoraGen } from '../lib/common';
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
      searchPlaceholder: 'subdomain.placeholders.search',
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
      this.transitionTo('subdomain.record.edit', model);
    },
  },
});
