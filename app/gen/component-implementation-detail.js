import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import validate from 'ember-gen/validate';
import {
  CREATE_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS
} from '../utils/common/component-implementation-detail';

export default AgoraGen.extend({
  modelName: 'component-implementation-detail',
  resourceName: 'api/v2/component-implementation-details',
  path: 'component-implementation-details',
  order: 3,
  common: {
    validators: {
      version: [validate.presence(true)],
      component_id: [validate.presence(true)],
      component_implementation_id: [validate.presence(true)],
    },
  },
  list: {
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
    filter: {
      active: true,
      serverSide: true,
      search: false,
      meta: {
        fields: [
          field(
            'component_id', {
              modelName:'component',
              type: 'model',
              label: 'component.belongs.name',
              displayAttr: 'name'
            }
          ),
          field(
            'component_implementation_id', {
              disabled: Ember.computed('model.changeset.component_id.id', function() {
                return !Ember.get(this, 'model.changeset.component_id');
              }),
              label: 'component_implementation.belongs.name',
              modelName:'component-implementation',
              type: 'model',
              displayAttr: 'name',
              query: Ember.computed('model.changeset.component_id.id', function() {
                let comp = Ember.get(this, 'model.changeset.component_id.id');
                return function(select, store, field, params) {
                  params = params || {};
                  params.component_id = comp;
                  return store.query('component-implementation', params);
                }
              })
            }
          ),
        ]
      }
    },
  },
  details: {
    fieldsets: DETAILS_FIELDSETS,
  },
  edit: {
    fieldsets: CREATE_FIELDSETS
  },
  create: {
    fieldsets: CREATE_FIELDSETS
  }
});
