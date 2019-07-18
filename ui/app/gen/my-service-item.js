import Ember from 'ember';
import ServiceItemGen from '../gen/service-item';

const {
  get,
  computed,
} = Ember;

export default ServiceItemGen.extend({
  name: 'my-services',
  path: 'my-services',
  order: 2,
  list: {
    getModel: function(params) {
      let user_id = get(this, 'session.session.authenticated.id');

      params = params || {};
      params.adminships__user_id = user_id;

      return this.store.query('service-item', params).then(function(services) {
        return services.filter(function(service){
          let rejected = get(service, 'rejected_service_admins_ids').split(',');
          let pending = get(service, 'pending_service_admins_ids').split(',');
          let not = rejected.concat(pending);

          return !not.includes(user_id.toString());
        })
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
    },
  },
});
