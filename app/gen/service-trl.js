import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';

const COMMON_FIELDSETS = [{
  label: 'service_trl.cards.basic_information',
  text: 'service_trl.cards.basic_hint',
  layout: {
    flex: [50, 50]
  },
  fields: [
    field(
      'value', {
        'label': 'service_trl.fields.value'
      }
    ),
    field(
      'order', {
        'label': 'service_trl.fields.order',
        'hint': 'service_trl.hints.order'
      }
    )
  ]
}]


export default AgoraGen.extend({
  modelName: 'service-trl',
  order: 200,
  path: 'service-trls',
  resourceName: 'api/v2/service-trls',
  common: {
    fieldsets: COMMON_FIELDSETS,
  },
  list: {
    layout: 'table',
    page: {
      title: 'service_trl.menu'
    },
    menu: {
      label: 'service_trl.menu',
      group: 'settings'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'value',
        'order'
      ]
    },
    sort: {
      serverSide: true,
      active: true,
      fields: [
        'value',
        'order'
      ]
    },
    paginate: {
      limits: [ 10, 50, 100 ],
      serverSide: true,
      active: true
    }
  }
});
