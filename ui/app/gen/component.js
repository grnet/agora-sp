// UNUSED
import { AgoraGen } from '../lib/common';
import {
  CREATE_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS
} from '../utils/common/component';

export default AgoraGen.extend({
  modelName: 'component',
  resourceName: 'api/v2/components',
  path: 'components',
  order: 1,
  list: {
    page: {
      title: 'component.menu'
    },
    menu: {
      display: false,
      label: 'component.menu',
      group: {
        name: 'components',
        label: 'Service Components',
        order: 3,
        icon: 'view_list',
      }
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS
    },
    sort: {
      serverSide: true,
      active: true,
      fields: SORT_FIELDS
    },
  },
  details: {
    page: {
      title: Ember.computed('model.name', function() {
        return Ember.get(this, 'model.name');
      })
    },
    fieldsets: DETAILS_FIELDSETS,
  },
  edit: {
    fieldsets: CREATE_FIELDSETS
  },
  create: {
    fieldsets: CREATE_FIELDSETS
  }
});
