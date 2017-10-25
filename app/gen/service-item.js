import Ember from 'ember';
import { AgoraGen } from '../lib/common';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';
import { TABLE_FIELDS, SORT_FIELDS, DETAILS_FIELDSETS, BASIC_INFO_FIELDS } from '../utils/common/service-item';

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
    layout: 'table',
    page: {
      title: 'Services'
    },
    menu: {
      label: 'Services'
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
            'name', {
              type: 'text',
              label: 'Name'
            }
          ),
          field(
            'service_trl', {
              modelName:'service_trl',
              type: 'model',
              displayAttr: 'value'
            }
          )
        ]
      }
    },
    sort: {
      serverSide: true,
      active: true,
      fields: SORT_FIELDS
    },
    paginate: {
      limits: [ 10, 50, 100 ],
      serverSide: true,
      active: true
    }
  },
  details: {
    fieldsets: DETAILS_FIELDSETS,
    page: {
      title: Ember.computed('model.name', function() {
        return Ember.get(this, 'model.name');
      })
    }
  }
});
