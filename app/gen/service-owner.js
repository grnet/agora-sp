import { AgoraGen } from '../lib/common';
import validate from 'ember-gen/validate';
import { field } from 'ember-gen';

const COMMON_FIELDSETS = [{
  label: 'service_owner.cards.basic_information',
  text: 'service_owner.cards.basic_hint',
  layout: {
    flex: [50, 50, 50, 50, 100]
  },
  fields: [
    'first_name',
    'last_name',
    'email',
    'phone',
    'id_service_owner',
  ]
}]



export default AgoraGen.extend({
  modelName: 'service-owner',
  order: 100,
  path: 'service-owners',
  resourceName: 'api/v2/service-owners',
  common: {
    fieldsets: COMMON_FIELDSETS,
    validators: {
      first_name: [validate.presence(true)],
      last_name: [validate.presence(true)],
      id_service_owner: [validate.presence(true)],
      email: [validate.format({type: 'email'})],
    },
  },
  list: {
    page: {
      title: 'service_owner.menu'
    },
    menu: {
      label: 'service_owner.menu',
      group: {
        name: 'user-information',
        label: 'group_menu.user_information',
        order: 400
      }
    },
    row: {
      fields: [
        'first_name',
        'last_name',
        'email',
        'phone',
        field('id_service_owner.name', { label: 'institution.belongs.name' })
      ],
      actions: ['gen:details', 'gen:edit', 'remove'],
    },
    sort: {
      serverside: false,
      active: true,
      fields: ['last_name', 'email', 'id_service_owner.name']
    },

  }
});
