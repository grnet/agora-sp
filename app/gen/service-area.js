import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS
} from '../utils/common/service-area';


export default AgoraGen.extend({
  modelName: 'service-area',
  order: 100,
  path: 'service-areas',
  resourceName: 'api/v2/service-areas',
  list: {
    page: {
      title: 'service_area.menu'
    },
    menu: {
      label: 'service_area.menu',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'name',
        'icon'
      ]
    },
    sort: {
      serverside: false,
      active: true,
      fields: ['name']
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
      this.transitionTo('service-area.record.edit', model);
    },

  }

});
