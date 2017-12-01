import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';

const COMMON_FIELDSETS = [{
  label: 'service_status.cards.basic_information',
  text: 'service_status.cards.basic_hint',
  layout: {
    flex: [50, 50]
  },
  fields: [
    field(
      'value', {
        'label': 'service_status.fields.value'
      }
    ),
    field(
      'order', {
        'label': 'service_status.fields.order',
        'hint': 'service_status.hints.order'
      }
    )
  ]
}]

export default AgoraGen.extend({
  modelName: 'service-status',
  order: 300,
  path: 'service-status',
  resourceName: 'api/v2/service-status',
  common: {
    fieldsets: COMMON_FIELDSETS,
  },
  list: {
    page: {
      title: 'service_status.menu'
    },
    menu: {
      label: 'service_status.menu',
      group: {
        name: 'settings',
        label: 'Settings',
        order: 999
      }
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'value',
        'order',
      ],
    },
    sort: {
      serverSide: false,
      active: true,
      fields: ['order', 'value']
    },

  }
});
