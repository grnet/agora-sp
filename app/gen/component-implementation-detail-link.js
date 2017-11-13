import gen from 'ember-gen/lib/gen';
import { field } from 'ember-gen';
import {
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  BASIC_INFO_FIELDS
} from '../utils/common/component-implementation-detail-link';

export default gen.CRUDGen.extend({
  modelName: 'component-implementation-detail-link',
  resourceName: 'api/v2/component-implementation-detail-links',
  path: 'component-implementation-detail-links',
  order: 4,
  list: {
    layout: 'table',
    page: {
      title: 'Component Implementation Detail Links'
    },
    menu: {
      label: 'Component Implementation Detail Links',
      group: 'components'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: TABLE_FIELDS
    },
  },
  details: {
    fieldsets: DETAILS_FIELDSETS
  },
  edit: {
    preloadModels: [
      'component',
      'component-implementation',
      'component-implementation-detail',
      'component-implementation-detail-link'
    ],
    getModel: function(params, model) {
      /*
       * In order to preload all 3 selects with the defaul values, we need to chain
       * a few api calls. First we get the first reversed level of
       * `service_component_implementation_detail_id` in order to have
       * the other two previous values, `component_id` and
       * `component_implementation_id`, and then set the default values to each
       * field of the model. Lastly, we return the model.
      */
      return model.get('service_component_implementation_detail_id').then(function(resp) {
        let promises = [
          resp.get('component_id'),
          resp.get('component_implementation_id')
        ];

        var promise = Ember.RSVP.all(promises).then((res) => {
          model.set('service_component', res[0]);
          model.set('service_component_implementation', res[1]);
        });

        return promise.then(function() {
          return model;
        });
      });
    },
    fieldsets: EDIT_FIELDSETS
  },
  create: {
    fieldsets: CREATE_FIELDSETS
  }
});
