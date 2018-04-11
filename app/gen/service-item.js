import Ember from 'ember';
import { AgoraGen } from '../lib/common';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS
} from '../utils/common/service-item';

export default AgoraGen.extend({
  modelName: 'service-item',
  resourceName: 'api/v2/services',
  path: 'services',
  order: 1,
  common: {
    validators: {
      name: [validate.presence(true)]
    }
  },
  list: {
    page: {
      title: 'service_item.menu'
    },
    menu: {
      label: 'service_item.menu'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS
    },
    filter: {
      active: true,
      serverSide: true,
      search: false,
      meta: {
        fields: [
          field(
            'service_trl', {
              modelName:'service_trl',
              type: 'model',
              displayAttr: 'value'
            }
          ),
          field(
            'service_area', {
              modelName:'service_area',
              type: 'model',
              displayAttr: 'name'
            }
          )
        ]
      }
    },
    sort: {
      serverSide: false,
      active: true,
      fields: SORT_FIELDS
    },
  },
  details: {
    fieldsets: DETAILS_FIELDSETS,
    page: {
      title: Ember.computed('model.name', function() {
        return Ember.get(this, 'model.name');
      })
    }
  },
  edit: {
    fieldsets: EDIT_FIELDSETS
  },
  create: {
    fieldsets: CREATE_FIELDSETS
  }
});
