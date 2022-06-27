import DS from 'ember-data';
import { countries, language_codes, locations } from '../resources';
import ENV from '../config/environment';
import { capitalize } from '../lib/common';

const {
  get,
  computed,
} = Ember;

const CHOICES = ENV.APP.resources;
const RELATED_PLATFORMS = ENV.APP.related_platforms;

let model = DS.Model.extend({
  session: Ember.inject.service(),

  // Basic Information
  erp_bai_id: DS.attr({
    label: 'resource.fields.erp_bai_id',
    hint: 'resource.hints.erp_bai_id',
  }),
  erp_bai_abbreviation: DS.attr({
    label: 'resource.fields.erp_bai_abbreviation',
    hint: 'resource.hints.erp_bai_abbreviation',
  }),
  erp_bai_name: DS.attr({
    label: 'resource.fields.erp_bai_name',
    hint: 'resource.hints.erp_bai_name',
  }),
  erp_bai_service_organisation: DS.belongsTo('provider', {
    autocomplete: true,
    type: 'select',
    label: 'resource.fields.erp_bai_service_organisation',
    hint: 'resource.hints.erp_bai_service_organisation',
    formAttrs: {
      optionLabelAttr: 'epp_bai_name',
    },
  }),
  erp_bai_service_providers: DS.hasMany('provider', {
    label: 'resource.fields.erp_bai_service_providers',
    hint: 'resource.hints.erp_bai_service_providers',
  }),
  erp_bai_providers_verbose: DS.attr({
    label: 'resource.fields.providers_names',
  }),
  erp_bai_webpage: DS.attr({
    label: 'resource.fields.erp_bai_webpage',
    hint: 'resource.hints.erp_bai_webpage',
  }),

  // Marketing fields
  erp_mri_description: DS.attr({
    label: 'resource.fields.erp_mri_description',
    hint: 'resource.hints.erp_mri_description',
    type: 'text',
    formComponent: 'text-editor',
    htmlSafe: true
  }),
  erp_mri_tagline: DS.attr({
    label: 'resource.fields.erp_mri_tagline',
    hint: 'resource.hints.erp_mri_tagline',
  }),
  erp_mri_logo: DS.attr({
    label: 'resource.fields.erp_mri_logo',
    hint: 'resource.hints.erp_mri_logo',
  }),
  erp_mri_multimedia: DS.attr({
    label: 'resource.fields.erp_mri_multimedia',
    formComponent: 'multiple-pairs',
    displayComponent: 'multiple-pairs-display',
    hint: 'resource.hints.erp_mri_multimedia',
    formAttrs: {
      actionTitle: 'add_multimedia',
      item1: 'multimedia_name',
      item2: 'multimedia_url',
    }
  }),
  erp_mri_use_cases: DS.attr({
    label: 'resource.fields.erp_mri_use_cases',
    formComponent: 'multiple-pairs',
    displayComponent: 'multiple-pairs-display',
    hint: 'resource.hints.erp_mri_use_cases',
    formAttrs: {
      actionTitle: 'add_usecase',
      item1: 'usecase_name',
      item2: 'usecase_url',
    }
  }),
  // classification information
  erp_cli_scientific_domain: DS.hasMany('domain', {
    label: 'resource.fields.erp_cli_scientific_domain',
    hint: 'resource.hints.erp_cli_scientific_domain',
  }),
  erp_cli_scientific_domain_verbose: DS.attr({
    label: 'resource.fields.erp_cli_scientific_domain',
  }),
  // TODO: Filter subdomain's ManyArray results according to domain selections
  erp_cli_scientific_subdomain: DS.hasMany('subdomain', {
    label: 'resource.fields.erp_cli_scientific_subdomain',
    hint: 'resource.hints.erp_cli_scientific_subdomain',
  }),
  erp_cli_scientific_subdomain_verbose: DS.attr({
    label: 'resource.fields.erp_cli_scientific_subdomain',
  }),
  erp_cli_category: DS.hasMany('category', {
    label: 'resource.fields.erp_cli_category',
    hint: 'resource.hints.erp_cli_category',
  }),
  erp_cli_category_verbose: DS.attr({
    label: 'resource.fields.erp_cli_category',
  }),
  // TODO: Filter subcategory's ManyArray results according to category selections
  erp_cli_subcategory: DS.hasMany('subcategory', {
      label: 'resource.fields.erp_cli_subcategory',
      hint: 'resource.hints.erp_cli_subcategory',
    }),
  erp_cli_subcategory_verbose: DS.attr({
      label: 'resource.fields.erp_cli_subcategory',
    }),
  erp_cli_target_users: DS.hasMany('target-user', {
    label: 'resource.fields.erp_cli_target_users',
    hint: 'resource.hints.erp_cli_target_users',
  }),
  erp_cli_target_users_verbose: DS.attr({
    label: 'resource.fields.erp_cli_target_users'
  }),
  erp_cli_access_type: DS.hasMany('access_type', {
    label: 'resource.fields.erp_cli_access_type',
    hint: 'resource.hints.erp_cli_access_type',
  }),
  erp_cli_access_mode: DS.hasMany('access_mode', {
    label: 'resource.fields.erp_cli_access_mode',
    hint: 'resource.hints.erp_cli_access_mode',
  }),
  erp_cli_tags: DS.attr({
    label: 'resource.fields.erp_cli_tags',
    hint: 'resource.hints.erp_cli_tags',
  }),
  // Management Information
  erp_mgi_helpdesk_webpage: DS.attr({
    label: 'resource.fields.erp_mgi_helpdesk_webpage',
    hint: 'resource.hints.erp_mgi_helpdesk_webpage',
  }),
  erp_mgi_user_manual: DS.attr({
    label: 'resource.fields.erp_mgi_user_manual',
    hint: 'resource.hints.erp_mgi_user_manual',
  }),
  erp_mgi_terms_of_use: DS.attr({
    label: 'resource.fields.erp_mgi_terms_of_use',
    hint: 'resource.hints.erp_mgi_terms_of_use',
  }),
  erp_mgi_privacy_policy: DS.attr({
    label: 'resource.fields.erp_mgi_privacy_policy',
    hint: 'resource.hints.erp_mgi_privacy_policy',
  }),
  erp_mgi_access_policy: DS.attr({
    label: 'resource.fields.erp_mgi_access_policy',
    hint: 'resource.hints.erp_mgi_access_policy',
  }),
  erp_mgi_sla_specification: DS.attr({
    label: 'resource.fields.erp_mgi_sla_specification',
    hint: 'resource.hints.erp_mgi_sla_specification',
  }),
  erp_mgi_training_information: DS.attr({
    label: 'resource.fields.erp_mgi_training_information',
    hint: 'resource.hints.erp_mgi_training_information',
  }),
  erp_mgi_status_monitoring: DS.attr({
    label: 'resource.fields.erp_mgi_status_monitoring',
    hint: 'resource.hints.erp_mgi_status_monitoring',
  }),
  erp_mgi_maintenance: DS.attr({
    label: 'resource.fields.erp_mgi_maintenance',
    hint: 'resource.hints.erp_mgi_maintenance',
  }),
  // Geographical and Language availability fields
  erp_gla_geographical_availability: DS.attr({
    defaultValue: 'Europe (EO)',
    label: 'resource.fields.erp_gla_geographical_availability',
    hint: 'resource.hints.erp_gla_geographical_availability',
    formComponent: 'agora-chips',
    formAttrs: {
      options: locations,
      exactMatch: true,
    }
  }),
  erp_gla_language: DS.attr({
    defaultValue: 'en',
    formComponent: 'agora-chips',
    label: 'resource.fields.erp_gla_language',
    hint: 'resource.hints.erp_gla_language',
    formAttrs: {
      options: language_codes,
      exactMatch: true,
    },
  }),
  erp_rli_geographic_location: DS.attr({
    defaultValue: 'Other',
    label: 'resource.fields.erp_rli_geographic_location',
    hint: 'resource.hints.erp_rli_geographic_location',
    formComponent: 'agora-chips',
    formAttrs: {
      options: countries,
      exactMatch: true,
    }
  }),

  main_contact: DS.belongsTo('contact-information', {
    autocomplete: true,
    type: 'select',
    label: 'resource.fields.main_contact',
    hint: 'resource.hints.main_contact',
  }),
  public_contact: DS.belongsTo('contact-information', {
    autocomplete: true,
    type: 'select',
    label: 'resource.fields.public_contact',
    hint: 'resource.hints.public_contact',
  }),
  erp_coi_helpdesk_email: DS.attr({
    label: 'resource.fields.erp_coi_helpdesk_email',
    hint: 'resource.hints.erp_coi_helpdesk_email',
  }),
  erp_coi_security_contact_email: DS.attr({
    label: 'resource.fields.erp_coi_security_contact_email',
    hint: 'resource.hints.erp_coi_security_contact_email',
  }),
  erp_mti_technology_readiness_level: DS.belongsTo('trl', {
    autocomplete: true,
    type: 'select',
    displayAttr: 'name',
    label: 'resource.fields.erp_mti_technology_readiness_level',
    hint: 'resource.hints.erp_mti_technology_readiness_level',
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  erp_mti_life_cycle_status: DS.belongsTo('resource-lifecycle-status', {
    autocomplete: true,
    type: 'select',
    displayAttr: 'name',
    label: 'resource.fields.erp_mti_life_cycle_status',
    hint: 'resource.hints.erp_mti_life_cycle_status',
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  erp_mti_certifications: DS.attr({
    label: 'resource.fields.erp_mti_certifications',
    hint: 'resource.hints.erp_mti_certifications',
    type: 'text',
  }),
  erp_mti_standards: DS.attr({
    label: 'resource.fields.erp_mti_standards',
    hint: 'resource.hints.erp_mti_standards',
    type: 'text',
  }),
  erp_mti_open_source_technologies: DS.attr({
    label: 'resource.fields.erp_mti_open_source_technologies',
    hint: 'resource.hints.erp_mti_open_source_technologies',
    type: 'text',
  }),
  erp_mti_version: DS.attr({
    label: 'resource.fields.erp_mti_version',
    hint: 'resource.hints.erp_mti_version',
  }),
  erp_mti_last_update: DS.attr('date', {
    label: 'resource.fields.erp_mti_last_update',
    hint: 'resource.hints.erp_mti_last_update',
  }),
  erp_mti_changelog: DS.attr({
    label: 'resource.fields.erp_mti_changelog',
    hint: 'resource.hints.erp_mti_changelog',
    type: 'text',
  }),

  // Dependencies Information
  required_resources: DS.hasMany('resource', {
    label: 'resource.fields.erp_dei_required_resources',
    hint: 'resource.hints.erp_dei_required_resources',
    inverse: null,
  }),
  related_resources: DS.hasMany('resource', {
    label: 'resource.fields.erp_dei_related_resources',
    hint: 'resource.hints.erp_dei_related_resources',
    inverse: null,
  }),
  erp_dei_related_platforms: DS.attr({
    label: 'resource.fields.erp_dei_related_platforms',
    hint: 'resource.hints.erp_dei_related_platforms',
    autocomplete: true,
    type: 'select',
    choices: RELATED_PLATFORMS,
  }),

  // Attribution Information
  erp_ati_funding_body: DS.hasMany('funding_body', {
    label: 'resource.fields.erp_ati_funding_body',
    hint: 'resource.hints.erp_ati_funding_body',
  }),
  erp_ati_funding_program: DS.hasMany('funding_program', {
    label: 'resource.fields.erp_ati_funding_program',
    hint: 'resource.hints.erp_ati_funding_program',
  }),
  erp_ati_grant_project_name: DS.attr({
    label: 'resource.fields.erp_ati_grant_project_name',
    hint: 'resource.hints.erp_ati_grant_project_name',
  }),

  // Access and Order Information
  erp_aoi_order_type: DS.belongsTo('order-type', {
    autocomplete: true,
    type: 'select',
    label: 'resource.fields.erp_aoi_order_type',
    hint: 'resource.hints.erp_aoi_order_type',
    displayAttr: 'name',
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  erp_aoi_order: DS.attr({
    label: 'resource.fields.erp_aoi_order',
    hint: 'resource.hints.erp_aoi_order',
  }),

  // Financial information
  erp_fni_payment_model: DS.attr({
    label: 'resource.fields.erp_fni_payment_model',
    hint: 'resource.hints.erp_fni_payment_model',
  }),
  erp_fni_pricing: DS.attr({
    label: 'resource.fields.erp_fni_pricing',
    hint: 'resource.hints.erp_fni_pricing',
  }),

  eosc_id: DS.attr(),
  eosc_state: DS.attr({
    autocomplete: true,
    type: 'select',
    choices: CHOICES.EOSC_STATE_RESOURCES,
  }),

  state: DS.attr({
    type: 'select',
    choices: CHOICES.RESOURCE_STATES,
    defaultValue: 'draft',
    label: 'resource.fields.state',
  }),

  state_verbose: computed('state', function(){
    return capitalize(get(this, 'state'));
  }),

  resource_admins_ids: DS.attr(),
  pending_resource_admins_ids: DS.attr(),
  rejected_resource_admins_ids: DS.attr(),

  can_apply_adminship: Ember.computed('resource_admins_ids', 'pending_resource_admins_ids', 'rejected_resource_admins_ids', 'erp_bai_service_organisation.id', function(){
    let role = get(this, 'session.session.authenticated.role');
    let user_org_id = get(this, 'session.session.authenticated.organisation');
    let resource_org_id = get(this, 'erp_bai_service_organisation.id');

    if (resource_org_id != user_org_id) {
      return false;
    }

    if (role !== 'serviceadmin') { return false; }
    let approved = get(this, 'resource_admins_ids').split(',');
    let pending = get(this, 'pending_resource_admins_ids').split(',');
    let rejected = get(this, 'rejected_resource_admins_ids').split(',');

    let all = [...approved, ...pending, ...rejected];
    let user_id = get(this, 'session.session.authenticated.id').toString();
    return !all.includes(user_id);
  }),
  can_revoke_adminship: Ember.computed('pending_resource_admins_ids', function(){
    let role = get(this, 'session.session.authenticated.role');

    if (role !== 'serviceadmin') { return false; }

    let pending = get(this, 'pending_resource_admins_ids').split(',');
    let user_id = get(this, 'session.session.authenticated.id').toString();
    return pending.includes(user_id);
  }),

  has_rejected_adminship: Ember.computed('rejected_resource_admins_ids', function(){
    let role = get(this, 'session.session.authenticated.role');

    if (role !== 'serviceadmin') { return false; }

    let rejected = get(this, 'rejected_resource_admins_ids').split(',');
    let user_id = get(this, 'session.session.authenticated.id').toString();
    return rejected.includes(user_id);
  }),

  __api__: {
    serialize: function(hash) {
      // do not send readonly keys to backend
      delete hash['erp_bai_providers_verbose'];
      delete hash['resource_admins_ids'];
      delete hash['pending_resource_admins_ids'];
      delete hash['rejected_resource_admins_ids'];
      delete hash['erp_cli_target_users_verbose'];
      delete hash['erp_cli_scientific_domain_verbose'];
      delete hash['erp_cli_scientific_subdomain_verbose'];
      delete hash['erp_cli_category_verbose'];
      delete hash['erp_cli_subcategory_verbose'];
      return hash;
    },
  },
});

model.reopenClass({ apimasResourceName: 'api/v2/resources' });

export default model;
