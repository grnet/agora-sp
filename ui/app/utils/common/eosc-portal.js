import Ember from 'ember';
import fetch from 'ember-network/fetch';
import ENV from 'agora-admin/config/environment';

const { computed, get } = Ember;

const DISABLED = !ENV.APP.eosc_portal.enabled;
const HIDE_ACTIONS_RESOURCE = !ENV.APP.eosc_portal.show_actions_resource;
const HIDE_ACTIONS_PROVIDER = !ENV.APP.eosc_portal.show_actions_provider;

function promptResource(self, method) {
  const erp_bai_1_name = get(self, 'model.erp_bai_1_name');
  const erp_bai_2_service_organisation = get(
    self,
    'model.erp_bai_2_service_organisation.id'
  );
  const erp_bai_4_webpage = get(self, 'model.erp_bai_4_webpage');
  const erp_mri_1_description = get(self, 'model.erp_mri_1_description');
  const erp_mri_2_tagline = get(self, 'model.erp_mri_2_tagline');
  const erp_mri_3_logo = get(self, 'model.erp_mri_3_logo');
  const erp_cli_1_scientific_domain = get(
    self,
    'model.erp_cli_1_scientific_domain'
  );
  const erp_cli_2_scientific_subdomain = get(
    self,
    'model.erp_cli_2_scientific_subdomain'
  );
  const erp_cli_3_category = get(self, 'model.erp_cli_3_category');
  const erp_cli_4_subcategory = get(self, 'model.erp_cli_4_subcategory');
  const erp_cli_5_target_users =
    get(self, 'model.erp_cli_5_target_users').content.length > 0;
  const erp_gla_1_geographical_availability = get(
    self,
    'model.erp_gla_1_geographical_availability'
  );
  const erp_gla_2_language = get(self, 'model.erp_gla_2_language');
  const main_contact = get(self, 'model.main_contact.id');
  const public_contact = get(self, 'model.public_contact.id');
  const erp_coi_13_helpdesk_email = get(
    self,
    'model.erp_coi_13_helpdesk_email'
  );
  const erp_coi_14_security_contact_email = get(
    self,
    'model.erp_coi_14_security_contact_email'
  );
  const erp_mti_1_technology_readiness_level = get(
    self,
    'model.erp_mti_1_technology_readiness_level.id'
  );
  const erp_mgi_2_user_manual = get(self, 'model.erp_mgi_2_user_manual');
  const erp_mgi_3_terms_of_use = get(self, 'model.erp_mgi_3_terms_of_use');
  const erp_mgi_4_privacy_policy = get(self, 'model.erp_mgi_4_privacy_policy');
  const erp_aoi_1_order_type = get(self, 'model.erp_aoi_1_order_type.id');

  let missing = [];
  let missing_str = '';

  let noControls = false;
  let message = `eosc.resource.${method}.message`;

  if (!erp_bai_1_name) {
    missing.push('erp_bai_1_name');
  }
  if (!erp_bai_2_service_organisation) {
    missing.push('erp_bai_2_service_organisation');
  }
  if (!erp_bai_4_webpage) {
    missing.push('erp_bai_4_webpage');
  }
  if (!erp_mri_1_description) {
    missing.push('erp_mri_1_description');
  }
  if (!erp_mri_2_tagline) {
    missing.push('erp_mri_2_tagline');
  }
  if (!erp_mri_3_logo) {
    missing.push('erp_mri_3_logo');
  }
  if (!erp_cli_1_scientific_domain) {
    missing.push('erp_cli_1_scientific_domain');
  }
  if (!erp_cli_2_scientific_subdomain) {
    missing.push('erp_cli_2_scientific_subdomain');
  }
  if (!erp_cli_3_category) {
    missing.push('erp_cli_3_category');
  }
  if (!erp_cli_4_subcategory) {
    missing.push('erp_cli_4_subcategory');
  }
  if (!erp_cli_5_target_users) {
    missing.push('erp_cli_5_target_users');
  }
  if (!erp_gla_1_geographical_availability) {
    missing.push('erp_gla_1_geographical_availability');
  }
  if (!erp_gla_2_language) {
    missing.push('erp_gla_2_language');
  }
  if (!main_contact) {
    missing.push('main_contact');
  }
  if (!public_contact) {
    missing.push('public_contact');
  }
  if (!erp_coi_13_helpdesk_email) {
    missing.push('erp_coi_13_helpdesk_email');
  }
  if (!erp_coi_14_security_contact_email) {
    missing.push('erp_coi_14_security_contact_email');
  }
  if (!erp_mti_1_technology_readiness_level) {
    missing.push('erp_mti_1_technology_readiness_level');
  }
  if (!erp_mgi_2_user_manual) {
    missing.push('erp_mgi_2_user_manual');
  }
  if (!erp_mgi_3_terms_of_use) {
    missing.push('erp_mgi_3_terms_of_use');
  }
  if (!erp_mgi_4_privacy_policy) {
    missing.push('erp_mgi_4_privacy_policy');
  }
  if (!erp_aoi_1_order_type) {
    missing.push('erp_aoi_1_order_type');
  }

  const i18n = get(self, 'i18n');

  if (missing.length > 0) {
    missing.forEach(function (el) {
      let field = `resource.fields.${el}`;
      let trans = i18n.t(field);
      missing_str += `<li>${trans}</li>`;
    });
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
  };
}

function promptProvider(self, method) {
  const epp_bai_id = get(self, 'model.epp_bai_id');
  const epp_bai_name = get(self, 'model.epp_bai_name');
  const epp_bai_abbreviation = get(self, 'model.epp_bai_abbreviation');
  const epp_bai_website = get(self, 'model.epp_bai_website');
  const epp_loi_1_street_name_and_number = get(
    self,
    'model.epp_loi_1_street_name_and_number'
  );
  const epp_loi_2_postal_code = get(self, 'model.epp_loi_2_postal_code');
  const epp_loi_3_city = get(self, 'model.epp_loi_3_city');
  const epp_loi_5_country_or_territory = get(
    self,
    'model.epp_loi_5_country_or_territory'
  );
  const epp_mri_1_description = get(self, 'model.epp_mri_1_description');
  const epp_mri_2_logo = get(self, 'model.epp_mri_2_logo');
  const main_contact = get(self, 'model.main_contact.id');
  const public_contact = get(self, 'model.public_contact.id');

  let missing = [];
  let missing_str = '';

  let noControls = false;
  let message = `eosc.provider.${method}.message`;

  if (!epp_bai_id) {
    missing.push('epp_bai_id');
  }
  if (!epp_bai_name) {
    missing.push('epp_bai_name');
  }
  if (!epp_bai_abbreviation) {
    missing.push('epp_bai_abbreviation');
  }
  if (!epp_bai_website) {
    missing.push('epp_bai_website');
  }
  if (!epp_loi_1_street_name_and_number) {
    missing.push('epp_loi_1_street_name_and_number');
  }
  if (!epp_loi_2_postal_code) {
    missing.push('epp_loi_2_postal_code');
  }
  if (!epp_loi_3_city) {
    missing.push('epp_loi_3_city');
  }
  if (!epp_loi_5_country_or_territory) {
    missing.push('epp_loi_5_country_or_territory');
  }
  if (!epp_mri_1_description) {
    missing.push('epp_mri_1_description');
  }
  if (!epp_mri_2_logo) {
    missing.push('epp_mri_2_logo');
  }
  if (!main_contact) {
    missing.push('main_contact');
  }
  if (!public_contact) {
    missing.push('public_contact');
  }

  const i18n = get(self, 'i18n');

  if (missing.length > 0) {
    missing.forEach(function (el) {
      let field = `provider.fields.${el}`;
      let trans = i18n.t(field);
      missing_str += `<li>${trans}</li>`;
    });
    noControls = true;
    message = get(self, 'i18n').t(`eosc.provider.${method}.message_missing`, {
      list_missing: `<ul>${missing_str}</ul>`,
    });
  }

  return {
    ok: `eosc.provider.${method}.ok`,
    cancel: 'cancel',
    title: `eosc.provider.${method}.title`,
    message,
    noControls,
  };
}
const postResourceEOSC = {
  label: 'eosc.resource.post.label',
  icon: 'backup',
  i18n: Ember.inject.service(),
  action: function (route, model) {
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
          resp.json().then(data => {
            let err_msg = (data && data.details) || 'eosc.resource.post.error';
            messages.setError(err_msg);
          });
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
    function () {
      if (DISABLED) {
        return true;
      }
      if (HIDE_ACTIONS_RESOURCE) {
        return true;
      }
      let role = get(this, 'role');
      let user_org = get(this, 'session.session.authenticated.organisation');
      let state = get(this, 'model.state');
      let resource_org = get(this, 'model.erp_bai_2_service_organisation.id');
      let portal_id = get(this, 'model.eosc_id');

      let user_is_provideradmin = role === 'provideradmin';
      let user_is_portfolioadmin = role === 'portfolioadmin';
      let user_owns_organisation = user_org === resource_org;
      let resource_is_published = state === 'published';
      let resource_has_eosc_id = portal_id;

      let permissible_role = ( user_is_provideradmin && user_owns_organisation) || user_is_portfolioadmin;

      if (
        permissible_role &&
        resource_is_published &&
        !resource_has_eosc_id
      ) {
        return false;
      } else {
        return true;
      }
    }
  ),
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
    'model.erp_mgi_4_privacy_policy',
    'model.erp_aoi_1_order_type.id',
    function () {
      return promptResource(this, 'post');
    }
  ),
};

const putResourceEOSC = {
  label: 'eosc.resource.put.label',
  icon: 'backup',
  action: function (route, model) {
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
          resp.json().then(data => {
            let err_msg = (data && data.details) || 'eosc.resource.put.error';
            messages.setError(err_msg);
          });
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
    function () {
      if (DISABLED) {
        return true;
      }
      if (HIDE_ACTIONS_RESOURCE) {
        return true;
      }
      let resource_org = get(this, 'model.erp_bai_2_service_organisation.id');
      let user_org = get(this, 'session.session.authenticated.organisation');
      let role = get(this, 'role');
      let state = get(this, 'model.state');
      let portal_id = get(this, 'model.eosc_id');

      let user_is_provideradmin = role === 'provideradmin';
      let user_is_portfolioadmin = role === 'portfolioadmin';
      let user_owns_organisation = user_org === resource_org;
      let resource_is_published = state === 'published';
      let resource_has_eosc_id = portal_id;

      let permissible_role = ( user_is_provideradmin && user_owns_organisation) || user_is_portfolioadmin;

      if (
        permissible_role &&
        resource_is_published &&
        resource_has_eosc_id
      ) {
        return false;
      } else {
        return true;
      }
    }
  ),
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
    'model.erp_mgi_4_privacy_policy',
    'model.erp_aoi_1_order_type.id',
    function () {
      return promptResource(this, 'put');
    }
  ),
};

const approveResourceEOSC = {
  label: 'eosc.resource.approve.label',
  icon: 'verified',
  classNames: 'md-icon-success',
  i18n: Ember.inject.service(),
  action: function (route, model) {
    let messages = get(route, 'messageService');
    let adapter = get(route, 'store').adapterFor('resource');
    let token = get(route, 'user.auth_token');
    let url = adapter.buildURL('resource', get(model, 'id'), 'findRecord');
    let APPROVE_PATH = 'approve-eosc/';
    return fetch(url + APPROVE_PATH, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        Authorization: `Token ${token}`,
      },
    })
      .then(resp => {
        if (resp.status === 200) {
          model.reload().then(() => {
            messages.setSuccess('eosc.resource.approve.success');
          });
        } else {
          resp.json().then(data => {
            let err_msg =
              (data && data.details) || 'eosc.resource.approve.error';
            messages.setError(err_msg);
          });
        }
      })
      .catch(err => {
        messages.setError('eosc.resource.approve.error');
      });
  },
  hidden: computed('role', 'model.eosc_state', function () {
    if (DISABLED) {
      return true;
    }
    if (HIDE_ACTIONS_PROVIDER) {
      return true;
    }
    let role = get(this, 'role');
    let eosc_state = get(this, 'model.eosc_state');
    let eosc_id = get(this, 'model.eosc_id');

    let user_is_portfolioadmin = role === 'portfolioadmin';
    let initial_states = ['pending resource', 'rejected resource', 'approved resource'];
    let resource_in_initial_states = initial_states.includes(eosc_state);

    if (user_is_portfolioadmin && resource_in_initial_states && !!eosc_id) {
      return false;
    } else {
      return true;
    }
  }),
  confirm: true,
  prompt: {
    ok: 'eosc.resource.approve.ok',
    cancel: 'cancel',
    title: 'eosc.resource.approve.title',
    message: 'eosc.resource.approve.message',
  },
};

const rejectResourceEOSC = {
  label: 'eosc.resource.reject.label',
  icon: 'cancel',
  accent: true,
  i18n: Ember.inject.service(),
  action: function (route, model) {
    let messages = get(route, 'messageService');
    let adapter = get(route, 'store').adapterFor('resource');
    let token = get(route, 'user.auth_token');
    let url = adapter.buildURL('resource', get(model, 'id'), 'findRecord');
    return fetch(url + 'reject-eosc/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        Authorization: `Token ${token}`,
      },
    })
      .then(resp => {
        if (resp.status === 200) {
          model.reload().then(() => {
            messages.setSuccess('eosc.resource.reject.success');
          });
        } else {
          resp.json().then(data => {
            let err_msg =
              (data && data.details) || 'eosc.resource.reject.error';
            messages.setError(err_msg);
          });
        }
      })
      .catch(err => {
        messages.setError('eosc.resource.reject.error');
      });
  },
  hidden: computed('role', 'model.eosc_state', function () {
    if (DISABLED) {
      return true;
    }
    if (HIDE_ACTIONS_PROVIDER) {
      return true;
    }
    let role = get(this, 'role');
    let eosc_state = get(this, 'model.eosc_state');
    let eosc_id = get(this, 'model.eosc_id');

    let user_is_portfolioadmin = role === 'portfolioadmin';
    let initial_states = [
      'pending resource',
      'approved resource',
    ];
    let resource_in_initial_states = initial_states.includes(eosc_state);

    if (user_is_portfolioadmin && resource_in_initial_states && !!eosc_id) {
      return false;
    } else {
      return true;
    }
  }),
  confirm: true,
  prompt: {
    ok: 'eosc.resource.reject.ok',
    cancel: 'cancel',
    message: 'eosc.resource.reject.message',
    title: 'eosc.resource.reject.title',
  },
};

const postProviderEOSC = {
  label: 'eosc.provider.post.label',
  icon: 'backup',
  i18n: Ember.inject.service(),
  action: function (route, model) {
    let messages = get(route, 'messageService');
    let adapter = get(route, 'store').adapterFor('provider');
    let token = get(route, 'user.auth_token');
    let url = adapter.buildURL('provider', get(model, 'id'), 'findRecord');
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
            messages.setSuccess('eosc.provider.post.success');
          });
        } else {
          resp.json().then(data => {
            let err_msg = (data && data.details) || 'eosc.provider.post.error';
            messages.setError(err_msg);
          });
        }
      })
      .catch(err => {
        messages.setError('eosc.provider.post.error');
      });
  },
  hidden: computed(
    'role',
    'model.state',
    'model.eosc_id',
    'model.id',
    function () {
      if (DISABLED) {
        return true;
      }
      if (HIDE_ACTIONS_PROVIDER) {
        return true;
      }
      let role = get(this, 'role');
      let user_org = get(this, 'session.session.authenticated.organisation');
      let state = get(this, 'model.state');
      let org_id = get(this, 'model.id');
      let portal_id = get(this, 'model.eosc_id');

      let user_is_provideradmin = role === 'provideradmin';
      let user_is_portfolioadmin = role === 'portfolioadmin';
      let user_owns_organisation = user_org === org_id;
      let resource_is_published = state === 'published';
      let resource_has_eosc_id = portal_id;

      let permissible_role = ( user_is_provideradmin && user_owns_organisation) || user_is_portfolioadmin;

      if (
        permissible_role &&
        resource_is_published &&
        !resource_has_eosc_id
      ) {
        return false;
      } else {
        return true;
      }
    }
  ),
  confirm: true,
  prompt: computed(
    'model.epp_bai_id',
    'model.epp_bai_name',
    'model.epp_bai_abbreviation',
    'model.epp_bai_website',
    'model.epp_loi_1_street_name_and_number',
    'model.epp_loi_2_postal_code',
    'model.epp_loi_3_city',
    'model.epp_loi_5_country_or_territory',
    'model.epp_mri_1_description',
    'model.epp_mri_2_logo',
    'model.main_contact.id',
    'model.public_contact.id',
    function () {
      return promptProvider(this, 'post');
    }
  ),
};

const putProviderEOSC = {
  label: 'eosc.provider.put.label',
  icon: 'backup',
  i18n: Ember.inject.service(),
  action: function (route, model) {
    let messages = get(route, 'messageService');
    let adapter = get(route, 'store').adapterFor('provider');
    let token = get(route, 'user.auth_token');
    let url = adapter.buildURL('provider', get(model, 'id'), 'findRecord');
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
            messages.setSuccess('eosc.provider.put.success');
          });
        } else {
          resp.json().then(data => {
            let err_msg = (data && data.details) || 'eosc.provider.put.error';
            messages.setError(err_msg);
          });
        }
      })
      .catch(err => {
        messages.setError('eosc.provider.put.error');
      });
  },
  hidden: computed(
    'role',
    'model.state',
    'model.eosc_id',
    'model.id',
    function () {
      if (DISABLED) {
        return true;
      }
      if (HIDE_ACTIONS_PROVIDER) {
        return true;
      }
      let role = get(this, 'role');
      let user_org = get(this, 'session.session.authenticated.organisation');
      let state = get(this, 'model.state');
      let org_id = get(this, 'model.id');
      let portal_id = get(this, 'model.eosc_id');

      let user_is_provideradmin = role === 'provideradmin';
      let user_is_portfolioadmin = role === 'portfolioadmin';
      let user_owns_organisation = user_org === org_id;
      let resource_is_published = state === 'published';
      let resource_has_eosc_id = portal_id;

      let permissible_role = ( user_is_provideradmin && user_owns_organisation) || user_is_portfolioadmin;

      if (
        permissible_role &&
        resource_is_published &&
        resource_has_eosc_id
      ) {
        return false;
      } else {
        return true;
      }
    }
  ),
  confirm: true,
  prompt: computed(
    'model.epp_bai_id',
    'model.epp_bai_name',
    'model.epp_bai_abbreviation',
    'model.epp_bai_website',
    'model.epp_loi_1_street_name_and_number',
    'model.epp_loi_2_postal_code',
    'model.epp_loi_3_city',
    'model.epp_loi_5_country_or_territory',
    'model.epp_mri_1_description',
    'model.epp_mri_2_logo',
    'model.main_contact.id',
    'model.public_contact.id',
    function () {
      return promptProvider(this, 'put');
    }
  ),
};

const approveProviderEOSC = {
  label: 'eosc.provider.approve.label',
  icon: 'verified',
  classNames: 'md-icon-success',
  i18n: Ember.inject.service(),
  action: function (route, model) {
    let messages = get(route, 'messageService');
    let adapter = get(route, 'store').adapterFor('provider');
    let token = get(route, 'user.auth_token');
    let url = adapter.buildURL('provider', get(model, 'id'), 'findRecord');
    return fetch(url + 'approve-eosc/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        Authorization: `Token ${token}`,
      },
    })
      .then(resp => {
        if (resp.status === 200) {
          model.reload().then(() => {
            messages.setSuccess('eosc.provider.approve.success');
          });
        } else {
          resp.json().then(data => {
            let err_msg =
              (data && data.details) || 'eosc.provider.approve.error';
            messages.setError(err_msg);
          });
        }
      })
      .catch(err => {
        messages.setError('eosc.provider.approve.error');
      });
  },
  hidden: computed('role', 'model.eosc_state', function () {
    if (DISABLED) {
      return true;
    }
    if (HIDE_ACTIONS_PROVIDER) {
      return true;
    }
    let role = get(this, 'role');
    let eosc_state = get(this, 'model.eosc_state');
    let eosc_id = get(this, 'model.eosc_id');

    let user_is_portfolioadmin = role === 'portfolioadmin';
    let initial_states = ['pending provider', 'rejected provider', 'approved provider'];
    let provider_in_initial_states = initial_states.includes(eosc_state);

    if (user_is_portfolioadmin && provider_in_initial_states && !!eosc_id) {
      return false;
    } else {
      return true;
    }
  }),
  confirm: true,
  prompt: {
    ok: 'eosc.provider.approve.ok',
    cancel: 'cancel',
    title: 'eosc.provider.approve.title',
    message: 'eosc.provider.approve.message',
  },
};

const rejectProviderEOSC = {
  label: 'eosc.provider.reject.label',
  icon: 'cancel',
  accent: true,
  i18n: Ember.inject.service(),
  action: function (route, model) {
    let messages = get(route, 'messageService');
    let adapter = get(route, 'store').adapterFor('provider');
    let token = get(route, 'user.auth_token');
    let url = adapter.buildURL('provider', get(model, 'id'), 'findRecord');
    return fetch(url + 'reject-eosc/', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        Authorization: `Token ${token}`,
      },
    })
      .then(resp => {
        if (resp.status === 200) {
          model.reload().then(() => {
            messages.setSuccess('eosc.provider.reject.success');
          });
        } else {
          resp.json().then(data => {
            let err_msg =
              (data && data.details) || 'eosc.provider.reject.error';
            messages.setError(err_msg);
          });
        }
      })
      .catch(err => {
        messages.setError('eosc.provider.reject.error');
      });
  },
  hidden: computed('role', 'model.eosc_state', function () {
    if (DISABLED) {
      return true;
    }
    if (HIDE_ACTIONS_PROVIDER) {
      return true;
    }
    let role = get(this, 'role');
    let eosc_state = get(this, 'model.eosc_state');
    let eosc_id = get(this, 'model.eosc_id');

    let user_is_portfolioadmin = role === 'portfolioadmin';
    let initial_states = [
      'pending provider',
      'approved provider',
    ];
    let provider_in_initial_states = initial_states.includes(eosc_state);

    if (user_is_portfolioadmin && provider_in_initial_states && !!eosc_id) {
      return false;
    } else {
      return true;
    }
  }),
  confirm: true,
  prompt: {
    ok: 'eosc.provider.reject.ok',
    cancel: 'cancel',
    message: 'eosc.provider.reject.message',
    title: 'eosc.provider.reject.title',
  },
};

export {
  postResourceEOSC,
  putResourceEOSC,
  approveResourceEOSC,
  rejectResourceEOSC,
  postProviderEOSC,
  putProviderEOSC,
  approveProviderEOSC,
  rejectProviderEOSC,
};
