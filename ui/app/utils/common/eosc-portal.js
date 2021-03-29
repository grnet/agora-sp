import Ember from 'ember';
import fetch from 'ember-network/fetch';
import ENV from 'agora-admin/config/environment';

const {
  computed,
  get,
} = Ember;

const DISABLED = !ENV.APP.eosc_portal.enabled;
const HIDE_ACTIONS = !ENV.APP.eosc_portal.show_actions;

function prompt(self, method) {
  const erp_bai_1_name = get(self, 'model.erp_bai_1_name');
  const erp_bai_2_service_organisation = get(self, 'model.erp_bai_2_service_organisation.id');
  const erp_bai_4_webpage = get(self, 'model.erp_bai_4_webpage');
  const erp_mri_1_description = get(self, 'model.erp_mri_1_description');
  const erp_mri_2_tagline = get(self, 'model.erp_mri_2_tagline');
  const erp_mri_3_logo = get(self, 'model.erp_mri_3_logo');
  const erp_cli_1_scientific_domain = get(self, 'model.erp_cli_1_scientific_domain');
  const erp_cli_2_scientific_subdomain = get(self, 'model.erp_cli_2_scientific_subdomain');
  const erp_cli_3_category = get(self, 'model.erp_cli_3_category');
  const erp_cli_4_subcategory = get(self, 'model.erp_cli_4_subcategory');
  const erp_cli_5_target_users = get(self, 'model.erp_cli_5_target_users').content.length > 0;
  const erp_gla_1_geographical_availability = get(self, 'model.erp_gla_1_geographical_availability');
  const erp_gla_2_language = get(self, 'model.erp_gla_2_language');
  const main_contact = get(self, 'model.main_contact.id');
  const public_contact = get(self, 'model.public_contact.id');
  const erp_coi_13_helpdesk_email = get(self, 'model.erp_coi_13_helpdesk_email');
  const erp_coi_14_security_contact_email = get(self, 'model.erp_coi_14_security_contact_email');
  const erp_mti_1_technology_readiness_level = get(self, 'model.erp_mti_1_technology_readiness_level.id');
  const erp_mgi_2_user_manual = get(self, 'model.erp_mgi_2_user_manual');
  const erp_mgi_3_terms_of_use = get(self, 'model.erp_mgi_3_terms_of_use');
  const erp_aoi_1_order_type = get(self, 'model.erp_aoi_1_order_type.id');

  let missing = [];
  let missing_str = '';

  let noControls = false;
  let message = `eosc.resource.${method}.message`;

  if (!erp_bai_1_name) { missing.push('erp_bai_1_name') }
  if (!erp_bai_2_service_organisation) { missing.push('erp_bai_2_service_organisation') }
  if (!erp_bai_4_webpage) { missing.push('erp_bai_4_webpage') }
  if (!erp_mri_1_description) { missing.push('erp_mri_1_description') }
  if (!erp_mri_2_tagline) { missing.push('erp_mri_2_tagline') }
  if (!erp_mri_3_logo) { missing.push('erp_mri_3_logo') }
  if (!erp_cli_1_scientific_domain) { missing.push('erp_cli_1_scientific_domain') };
  if (!erp_cli_2_scientific_subdomain) { missing.push('erp_cli_2_scientific_subdomain')};
  if (!erp_cli_3_category) { missing.push('erp_cli_3_category')};
  if (!erp_cli_4_subcategory) { missing.push('erp_cli_4_subcategory')};
  if (!erp_cli_5_target_users) { missing.push('erp_cli_5_target_users')};
  if (!erp_gla_1_geographical_availability) { missing.push('erp_gla_1_geographical_availability')};
  if (!erp_gla_2_language) { missing.push('erp_gla_2_language')};
  if (!main_contact) { missing.push('main_contact')};
  if (!public_contact) { missing.push('public_contact')};
  if (!erp_coi_13_helpdesk_email) { missing.push('erp_coi_13_helpdesk_email')};
  if (!erp_coi_14_security_contact_email) { missing.push('erp_coi_14_security_contact_email')};
  if (!erp_mti_1_technology_readiness_level) { missing.push('erp_mti_1_technology_readiness_level')};
  if (!erp_mgi_2_user_manual) { missing.push('erp_mgi_2_user_manual')};
  if (!erp_mgi_3_terms_of_use) { missing.push('erp_mgi_3_terms_of_use')};
  if (!erp_aoi_1_order_type) { missing.push('erp_aoi_1_order_type')};

  const i18n = get(self, 'i18n');

  if (missing.length > 0) {
    missing.forEach(function(el) {
      let field = `resource.fields.${el}`;
      let trans = i18n.t(field);
      missing_str += `<li>${trans}</li>`;
    })
    noControls = true;
    message = get(self, 'i18n').t(`eosc.resource.${method}.message_missing`, {
      list_missing: `<ul>${missing_str}</ul>`,
    });
  }

  return {
    ok: `eosc.resource.${method}.ok`,
    cancel: 'cancel',
    title: `eosc.resource.${method}.title`,
    message,
    noControls,
  }

}


const postResourceEOSC = {
  label: 'eosc.resource.post.label',
  icon: 'backup',
  i18n: Ember.inject.service(),
	action: function(route, model) {
		let messages = get(route, 'messageService');
		let adapter = get(route, 'store').adapterFor('resource');
		let token = get(route, 'user.auth_token');
		let url = adapter.buildURL('resource', get(model, 'id'), 'findRecord');
		return fetch(url + 'publish-eosc/', {
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
        resp.json().then((data)=> {
          let err_msg = data && data.details || 'eosc.resource.post.error';
				  messages.setError(err_msg);
        })
			}
		})
		.catch(err => {
			messages.setError('eosc.resource.post.error');
		});
  },
  hidden: computed(
    'role',
    'model.state',
    'model.eosc_id',
    'model.erp_bai_2_service_organisation',
    function(){
      if ( DISABLED ) { return true }
      if ( HIDE_ACTIONS ) { return true }
      let role = get(this, 'role');
      let user_org = get(this, 'session.session.authenticated.organisation');
      let state = get(this, 'model.state');
      let resource_org = get(this, 'model.erp_bai_2_service_organisation.id');
      let portal_id = get(this, 'model.eosc_id');

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
  prompt: computed(
    'model.erp_bai_0_id',
    'model.erp_bai_2_service_organisation.id',
    'model.erp_bai_4_webpage',
    'model.erp_mri_1_description',
    'model.erp_mri_2_tagline',
    'model.erp_cli_2_scientific_subdomain',
    'model.erp_cli_3_category',
    'model.erp_cli_4_subcategory',
    'model.erp_cli_5_target_users.[]',
    'model.erp_gla_1_geographical_availability',
    'model.erp_gla_2_language',
    'model.main_contact.id',
    'model.public_contact.id',
    'model.erp_coi_13_helpdesk_email',
    'model.erp_coi_14_security_contact_email',
    'model.erp_mti_1_technology_readiness_level.id',
    'model.erp_mgi_2_user_manual',
    'model.erp_mgi_3_terms_of_use',
    'model.erp_aoi_1_order_type.id',
    function(){
      return prompt(this, 'post');
    }
  ),
};


const putResourceEOSC = {
  label: 'eosc.resource.put.label',
  icon: 'backup',
	action: function(route, model) {
		let messages = get(route, 'messageService');
		let adapter = get(route, 'store').adapterFor('resource');
		let token = get(route, 'user.auth_token');
		let url = adapter.buildURL('resource', get(model, 'id'), 'findRecord');
		return fetch(url + 'update-eosc/', {
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
        resp.json().then((data)=> {
          let err_msg = data && data.details || 'eosc.resource.put.error';
				  messages.setError(err_msg);
        })
			}
		})
		.catch(err => {
			messages.setError('eosc.resource.put.error');
		});
  },
  hidden: computed(
    'role',
    'model.state',
    'model.eosc_id',
    'model.erp_bai_2_service_organisation',
    function(){
      if ( DISABLED ) { return true }
      if ( HIDE_ACTIONS ) { return true }
      let resource_org = get(this, 'model.erp_bai_2_service_organisation.id');
      let user_org = get(this, 'session.session.authenticated.organisation');
      let role = get(this, 'role');
      let state = get(this, 'model.state');
      let portal_id = get(this, 'model.eosc_id');

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
  prompt: computed(
    'model.erp_bai_0_id',
    'model.erp_bai_2_service_organisation.id',
    'model.erp_bai_4_webpage',
    'model.erp_mri_1_description',
    'model.erp_mri_2_tagline',
    'model.erp_cli_2_scientific_subdomain',
    'model.erp_cli_3_category',
    'model.erp_cli_4_subcategory',
    'model.erp_cli_5_target_users.[]',
    'model.erp_gla_1_geographical_availability',
    'model.erp_gla_2_language',
    'model.main_contact.id',
    'model.public_contact.id',
    'model.erp_coi_13_helpdesk_email',
    'model.erp_coi_14_security_contact_email',
    'model.erp_mti_1_technology_readiness_level.id',
    'model.erp_mgi_2_user_manual',
    'model.erp_mgi_3_terms_of_use',
    'model.erp_aoi_1_order_type.id',
    function(){
      return prompt(this, 'put');
    }
  ),
};

export {
  postResourceEOSC,
  putResourceEOSC,
}
