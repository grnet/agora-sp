import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import validate from 'ember-gen/validate';

const COMMON_FIELDSETS = [{
  label: 'contact_information.cards.basic_information',
  text: 'contact_information.cards.basic_hint',
  layout: {
    flex: [50, 50, 50, 50, 100]
  },
  fields: [
    'first_name',
    'last_name',
    'email',
    'phone',
    'url'
  ]
}]


export default AgoraGen.extend({
  modelName: 'contact-information',
  path: 'contact-information',
  resourceName: 'api/v2/contact-information',
  common: {
    fieldsets: COMMON_FIELDSETS,
    validators: {
      first_name: [validate.presence(true)],
      last_name: [validate.presence(true)],
      email: [validate.format({type: 'email', allowBlank: true})],
      url: [validate.format({type: 'url', allowBlank: true})]
    },
  },
  list: {
    page: {
      title: 'contact_information.menu'
    },
    menu: {
      label: 'contact_information.menu',
      group: 'user-information'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        field('full_name', {label: 'contact_information.fields.full_name'}),
        'email',
        'phone',
      ]
    },
    sort: {
      serverSide: false,
      active: true,
      fields: ['full_name', 'email']
    },
  }
});
