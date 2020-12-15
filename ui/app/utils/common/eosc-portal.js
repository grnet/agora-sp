import Ember from 'ember';

const {
  computed,
  get,
} = Ember;

const postResourceEOSC = {
  label: 'eosc.resource.post.label',
  icon: 'backup',
  accent: true,
  action: function(route, model) {
    let m = route.get('messageService');
    alert('WIP');
  },
  hidden: computed(
    'role',
    'model.state',
    'model.eosc-portal-id',
    'model.erp_bai_2_service_organisation',
    function(){
      let role = get(this, 'role');
      let user_org = get(this, 'session.session.authenticated.organisation');
      let state = get(this, 'model.state');
      let resource_org = get(this, 'model.erp_bai_2_service_organisation.id');
      let portal_id = get(this, 'model.eosc-portal-id');

      let user_is_provideradmin = role === 'provideradmin';
      let user_owns_organisation = user_org === resource_org;
      let resource_is_published = state === 'published';
      let resource_has_eosc_id = portal_id;

      if (
        user_is_provideradmin &&
        user_owns_organisation &&
        resource_is_published &&
        !resource_has_eosc_id
      ) {
        return false;
      } else {
        return true;
      }
  }),
  confirm: true,
  prompt: {
    ok: 'eosc.resource.post.ok',
    cancel: 'cancel',
    message: 'eosc.resource.post.message',
    title: 'eosc.resource.post.title',
  },
};


const putResourceEOSC = {
  label: 'eosc.resource.put.label',
  icon: 'backup',
  action: function(route, model) {
    let m = route.get('messageService');
    alert('WIP');
  },
  hidden: computed(
    'role',
    'model.state',
    'model.eosc-portal-id',
    'model.erp_bai_2_service_organisation',
    function(){
      let resource_org = get(this, 'model.erp_bai_2_service_organisation.id');
      let user_org = get(this, 'session.session.authenticated.organisation');
      let role = get(this, 'role');
      let state = get(this, 'model.state');
      let portal_id = get(this, 'model.eosc-portal-id');

      let user_is_provideradmin = role === 'provideradmin';
      let user_owns_organisation = user_org === resource_org;
      let resource_is_published = state === 'published';
      let resource_has_eosc_id = portal_id;

      if (
        user_is_provideradmin &&
        user_owns_organisation &&
        resource_is_published &&
        resource_has_eosc_id
      ) {
        return false;
      } else {
        return true;
      }
  }),
  confirm: true,
  prompt: {
    ok: 'eosc.resource.put.ok',
    cancel: 'cancel',
    message: 'eosc.resource.put.message',
    title: 'eosc.resource.put.title',
  },
};
export {
  postResourceEOSC,
  putResourceEOSC,
}
