import { AgoraGen } from '../lib/common';
import validate from 'ember-gen/validate';


export default AgoraGen.extend({
  modelName: 'access-policy',
  order: 120,
  path: 'access-policies',
  resourceName: 'api/v2/access-policies',
  common: {
    fieldsets: [{
      label: 'access_policy.cards.basic_information',
      fields: [
        'name',
        'access_mode',
        'payment_model',
        'pricing',
        'conditions',
        'geo_availability',
        'access_policy_url',
      ],
      layout: {
        flex: [100, 100, 100, 100, 100, 100, 100]
      },
    }],
    validators: {
      name: [validate.presence(true)],
    },
  },
  list: {
    page: {
      title: 'access_policy.menu',
    },
    menu: {
      label: 'access_policy.menu',
    },
    row: {
      fields: [
        'name',
        'geo_availability',
        'access_policy_url',
      ],
    },
    filter: {
      active: false,
      serverSide: true,
      search: true,
      searchPlaceholder: 'common.placeholders.search',
    },
    sort: {
      serverSide: true,
      active: true,
      fields: [
        'name',
        'geo_availability',
        'access_policy_url',
      ],
    },
  }
});
