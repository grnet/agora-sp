import Ember from 'ember';
import { field } from 'ember-gen';
import { AgoraGen } from '../lib/common';


const {
  get,
} = Ember;

export default AgoraGen.extend({
  modelName: 'resource-admin',
  order: 100,
  path: 'resource-admins',
  resourceName: 'api/v2/resource-admins',
  list: {
    getModel(params) {
      params = params || {};

      return this.store.query('resource-admin', params).then((sa) => {
        let user_id = get(this, 'session.session.authenticated.id');
        let res = sa.filter(el => get(el, 'admin_id') != user_id);

        return res;
      });
    },
    page: {
      title: 'resource_admin.menu',
    },
    menu: {
      label: 'resource_admin.menu',
      group: {
        name: 'user-information',
        label: 'group_menu.user_information',
        order: 400,
          icon: 'people',
      },
    },
    row: {
      fields: [
        'resource_name',
        field('admin_full_name', { label: 'resource_admin.fields.admin_full_name' }),
        'admin_email',
        'state',
      ],
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['resource_name', 'admin_email', 'state'],
    },
    filter: {
      active: false,
      serverSide: true,
      search: false,
    },
  },
  details: {
    fieldsets: [{
      label: 'resource_admin.cards.basic_information',
      fields: [
        'state',
        'created_at',
        'updated_at',
      ],
    }, {
      label: 'resource_admin.cards.admin_info',
      fields: [
        'admin_full_name',
        'admin_email',
        'admin_id',
      ],
    }, {
      label: 'resource_admin.cards.resource_info',
      fields: [
        'resource_name',
        'resource.id',
      ],
    }],
  },
});
