import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import { AgoraGen } from '../lib/common';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
} from '../utils/common/federation-member';

export default AgoraGen.extend({
  modelName: 'federation_member',
  path: 'federation-members',
  resourceName: 'api/v2/federation-members',
  common: {
    validators: {
      name: [validate.presence(true)],
      webpage: [validate.format({ type: 'url', allowBlank: true })],
      country: [validate.length({ is: 2, allowBlank: true })],
    },
  },
  list: {
    page: {
      title: 'federation_member.menu',
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: ['name', 'webpage', 'country'],
    },
    menu: {
      label: 'federation_member.menu',
      order: 500,
      group: {
        name: 'user-information',
      }
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'service_item.placeholders.search',
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['name', 'country'],
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
      this.transitionTo('federation-member.record.edit', model);
    },
  },
});
