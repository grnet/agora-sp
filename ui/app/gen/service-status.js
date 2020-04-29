// UNUSED
import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';

const COMMON_FIELDSETS = [{
  label: 'service_status.cards.basic_information',
  text: 'service_status.cards.basic_hint',
  layout: {
    flex: [100, 100]
  },
  fields: [
    field(
      'value', {
        'label': 'service_status.fields.value'
      }
    ),
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
        label: 'service_status.fields.description',
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
      display: false,
      label: 'service_status.menu',
      group: {
        name: 'settings',
        label: 'Settings',
        icon: 'settings',
        order: 500
      }
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'value',
      ],
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['value']
    },

  }
});
