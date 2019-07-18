import Ember from 'ember';
import ServiceItemGen from '../gen/service-item';
import { get_my_services } from '../utils/common/common';

const {
  get,
  computed,
} = Ember;

export default ServiceItemGen.extend({
  name: 'my-services',
  path: 'my-services',
  order: 3,
  list: {
    getModel: function(params) {
      let user_id = get(this, 'session.session.authenticated.id');

      params = params || {};
      params.adminships__user_id = user_id;

      return this.store.query('service-item', params).then(function(services) {
        return get_my_services(services, user_id);
      });
    },
    page: {
      title: 'service_item.my_menu',
    },
    menu: {
      display: computed('role', function(){
        let role = get(this, 'session.session.authenticated.role');

        return role === 'serviceadmin';
      }),
      label: 'service_item.my_menu',
      icon: 'book',
    },
  },
});
