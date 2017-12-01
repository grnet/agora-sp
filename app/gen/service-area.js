import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';

const COMMON_FIELDSETS = [{
  label: 'service_area.cards.basic_information',
  text: 'service_area.cards.basic_hint',
  layout: {
    flex: [100, 100]
  },
  fields: [
    field(
      'name', {
        'label': 'service_area.fields.name',
        'hint': 'service_area.hints.name'
      }
    ),
    field(
      'icon', {
        'label': 'service_area.fields.icon',
      }
    )
  ]
}]


export default AgoraGen.extend({
  modelName: 'service-area',
  order: 100,
  path: 'service-areas',
  resourceName: 'api/v2/service-areas',
  common: {
    fieldsets: COMMON_FIELDSETS,
  },
  list: {
    page: {
      title: 'service_area.menu'
    },
    menu: {
      label: 'service_area.menu',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'name',
        'icon'
      ]
    },
    sort: {
      serverside: false,
      active: true,
      fields: ['name']
    },


  }
});
