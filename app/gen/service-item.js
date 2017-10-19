import Ember from 'ember';
import { AgoraGen } from '../lib/common';
import validate from 'ember-gen/validate';
import { DETAILS_FIELDSETS } from '../utils/common/service-item';

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
      fields: [
        'name',
        'service_area.name',
        'short_description',
        'service_trl.value',
        'id_service_owner.full_name'
      ]
    }
  },
  details: {
    fieldsets: DETAILS_FIELDSETS,
  }
});
