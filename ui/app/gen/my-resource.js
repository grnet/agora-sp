import Ember from 'ember';
import ResourceGen from '../gen/resource';

const {
  get,
  computed,
} = Ember;

export default ResourceGen.extend({
  name: 'my-resources',
  path: 'my-resources',
  order: 3,
  list: {
    getModel: function(params) {
      let user_id = get(this, 'session.session.authenticated.id');
      let user_org_id = get(this, 'session.session.authenticated.organisation');
      let role = get(this, 'session.session.authenticated.role');

      params = params || {};
      if (role === 'serviceadmin') {
        params.adminships__admin_id = user_id;
        params.adminships__state = 'approved';
      }

      if (role === 'provideradmin') {
        params.erp_bai_service_organisation = user_org_id;
      }

      return this.store.query('resource', params)
    },
    page: {
      title: 'resource.my_menu',
    },
    menu: {
      display: computed('role', function(){
        let role = get(this, 'session.session.authenticated.role');
        return role === 'serviceadmin' || role === 'provideradmin';
      }),
      label: 'resource.my_menu',
      icon: 'book',
    },
  },
});
