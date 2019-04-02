import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import { AgoraGen } from '../lib/common';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS,
} from '../utils/common/service-provider';

export default AgoraGen.extend({
  modelName: 'service_provider',
  path: 'service-providers',
  resourceName: 'api/v2/service-providers',
  common: {
    validators: {
      name: [validate.presence(true)],
      webpage: [validate.format({ type: 'url', allowBlank: true })],
      country: [validate.length({ is: 2, allowBlank: true })],
    },
  },
  list: {
    page: {
      title: 'service_provider.menu',
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: ['name', 'webpage', 'country'],
    },
    menu: {
      label: 'service_provider.menu',
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
      this.transitionTo('service-provider.record.edit', model);
    },
  },
});
