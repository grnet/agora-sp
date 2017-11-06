import gen from 'ember-gen/lib/gen';
import {
  CREATE_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS
} from '../utils/common/component-implementation-detail';

export default gen.CRUDGen.extend({
  modelName: 'component-implementation-detail',
  resourceName: 'api/v2/component-implementation-details',
  path: 'component-implementation-details',
  order: 3,
  list: {
    layout: 'table',
    page: {
      title: 'Component Implementation Details'
    },
    menu: {
      label: 'Component Implementation Details',
      group: 'components'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS
    },
    sort: {
      serverSide: false,
      active: true,
      fields: SORT_FIELDS
    },
    paginate: {
      limits: [ 10, 50, 100 ],
      serverSide: false,
      active: true
    }
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
