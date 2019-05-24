import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import validate from 'ember-gen/validate';

import {
  CREATE_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS
} from '../utils/common/component-implementation';

export default AgoraGen.extend({
  modelName: 'component-implementation',
  resourceName: 'api/v2/component-implementations',
  path: 'component-implementations',
  order: 2,
  common: {
    validators: {
      name: [validate.presence(true)],
      component_id: [validate.presence(true)],
    }
  },
  list: {
    page: {
      title: 'component_implementation.menu',
    },
    menu: {
      label: 'component_implementation.menu',
      group: 'components'
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
    filter: {
      active: true,
      serverSide: true,
      search: true,
      searchPlaceholder: 'component_implementation.placeholders.search',
      meta: {
        fields: [
          field(
            'component_id', {
              modelName:'component',
              label: 'component.belongs.name',
              type: 'model',
              displayAttr: 'name'
            }
          ),
        ]
      }
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
