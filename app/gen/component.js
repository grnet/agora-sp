import gen from 'ember-gen/lib/gen';
import {
  CREATE_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS
} from '../utils/common/component';

export default gen.CRUDGen.extend({
  modelName: 'component',
  resourceName: 'api/v2/components',
  path: 'components',
  order: 1,
  list: {
    layout: 'table',
    page: {
      title: 'Components'
    },
    menu: {
      label: 'Components',
      group: {
        name: 'components',
        label: 'Service Components',
        order: 3
      }
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
