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

      params = params || {};
      params.adminships__admin_id = user_id;
      params.adminships__state = 'approved';

      return this.store.query('resource', params)
    },
    page: {
      title: 'resource.my_menu',
    },
    menu: {
      display: computed('role', function(){
        let role = get(this, 'session.session.authenticated.role');

        return role === 'serviceadmin';
      }),
      label: 'resource.my_menu',
      icon: 'book',
    },
  },
});
