import Ember from 'ember';
import fetch from 'ember-network/fetch';
import ENV from 'agora-admin/config/environment';

const {
  computed,
  get,
} = Ember;


const postResourceEOSC = {
  label: 'eosc.resource.post.label',
  icon: 'backup',
  accent: true,
	action: function(route, model) {
		let messages = get(route, 'messageService');
		let adapter = get(route, 'store').adapterFor('resource');
		let token = get(route, 'user.auth_token');
		let url = adapter.buildURL('resource', get(model, 'id'), 'findRecord');
		return fetch(url + 'post-eosc/', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				Authorization: `Token ${token}`,
			},
		})
		.then(resp => {
			if (resp.status === 200) {
				model.reload().then(() => {
					messages.setSuccess('eosc.resource.post.success');
				});
			} else {
				messages.setSuccess('eosc.resource.post.error');
			}
		})
		.catch(err => {
			messages.setError('eosc.resource.post.error');
		});
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
		let messages = get(route, 'messageService');
		let adapter = get(route, 'store').adapterFor('resource');
		let token = get(route, 'user.auth_token');
		let url = adapter.buildURL('resource', get(model, 'id'), 'findRecord');
		return fetch(url + 'put-eosc/', {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				Authorization: `Token ${token}`,
			},
		})
		.then(resp => {
			if (resp.status === 200) {
				model.reload().then(() => {
					messages.setSuccess('eosc.resource.put.success');
				});
			} else {
				messages.setSuccess('eosc.resource.put.error');
			}
		})
		.catch(err => {
			messages.setError('eosc.resource.put.error');
		});
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
