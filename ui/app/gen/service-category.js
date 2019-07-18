import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  DETAILS_FIELDSETS
} from '../utils/common/service-category';


export default AgoraGen.extend({
  modelName: 'service-category',
  order: 100,
  path: 'service-categories',
  resourceName: 'api/v2/service-categories',
  list: {
    page: {
      title: 'service_category.menu'
    },
    menu: {
      label: 'service_category.menu',
      group: {
        name: 'settings',
        icon: 'settings',
      },
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'name',
        field('icon_filename', {label: 'service_category.fields.icon'})
      ]
    },
    sort: {
      serverSide: true,
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
      this.transitionTo('service-category.record.edit', model);
    },

  }

});
