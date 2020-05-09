import DS from 'ember-data';
import { countries, language_codes } from '../resources';

export default DS.Model.extend({
  // Basic Inforamation
  rd_bai_0_id: DS.attr({
    label: 'resource.fields.rd_bai_0_id',
    hint: 'resource.hints.rd_bai_0_id',
  }),
  rd_bai_1_name: DS.attr({
    label: 'resource.fields.rd_bai_1_name',
    hint: 'resource.hints.rd_bai_1_name',
  }),
  rd_bai_2_service_organisation: DS.belongsTo('provider', {
    label: 'resource.fields.rd_bai_2_service_organisation',
    hint: 'resource.hints.rd_bai_2_service_organisation',
    formAttrs: {
      optionLabelAttr: 'pd_bai_1_name',
    },
  }),
  rd_bai_3_service_providers: DS.hasMany('provider', {
    label: 'resource.fields.rd_bai_3_service_providers',
    hint: 'resource.hints.rd_bai_2_service_organisation',
  }),
  rd_bai_4_webpage: DS.attr({
    label: 'resource.fields.rd_bai_4_webpage',
    hint: 'resource.hints.rd_bai_4_webpage',
  }),
  providers_names: DS.attr({
    label: 'resource.fields.providers_names',
  }),

  // Marketing fields
  rd_mri_1_description: DS.attr({
    label: 'resource.fields.rd_mri_1_description',
    hint: 'resource.hints.rd_mri_1_description',
    type: 'text',
    formComponent: 'text-editor',
    htmlSafe: true
  }),
  rd_mri_2_tagline: DS.attr({
    label: 'resource.fields.rd_mri_2_tagline',
    hint: 'resource.hints.rd_mri_2_tagline',
  }),
  rd_mri_3_logo: DS.attr({
    label: 'resource.fields.rd_mri_3_logo',
    hint: 'resource.hints.rd_mri_3_logo',
  }),
  rd_mri_4_mulitimedia: DS.attr({
    label: 'resource.fields.rd_mri_4_mulitimedia',
    hint: 'resource.hints.rd_mri_4_mulitimedia',
  }),
  rd_mri_5_target_users: DS.hasMany('target-user', {
    label: 'resource.fields.rd_mri_5_target_users',
    hint: 'resource.hints.rd_mri_5_target_users',
  }),
  rd_mri_6_target_customer_tags: DS.attr({
    label: 'resource.fields.rd_mri_6_target_customer_tags',
    hint: 'resource.hints.rd_mri_6_target_customer_tags',
    formComponent: 'agora-chips',
  }),
  rd_mri_7_use_cases: DS.attr({
    label: 'resource.fields.rd_mri_7_use_cases',
    hint: 'resource.hints.rd_mri_7_use_cases',
    type: 'text',
    formComponent: 'text-editor',
    htmlSafe: true
  }),
  rd_mri_5_target_users_verbose: DS.attr({
    label: 'resource.fields.rd_mri_5_target_users'
  }),
  // classification information
  rd_cli_1_scientific_domain: DS.hasMany('domain', {
    label: 'resource.fields.rd_cli_1_scientific_domain',
    hint: 'resource.hints.rd_cli_1_scientific_domain',
  }),
  domain_names: DS.attr({
    label: 'resource.fields.domain_names',
  }),
  // TODO: Filter subdomain's ManyArray results according to domain selections
  rd_cli_2_scientific_subdomain: DS.hasMany('subdomain', {
    label: 'resource.fields.rd_cli_2_scientific_subdomain',
    hint: 'resource.hints.rd_cli_2_scientific_subdomain',
  }),
  subdomain_names: DS.attr({
    label: 'resource.fields.subdomain_names',
  }),
  rd_cli_5_tags: DS.attr({
    label: 'resource.fields.rd_cli_5_tags',
    hint: 'resource.hints.rd_cli_5_tags',
    formComponent: 'agora-chips',
  }),
  // Management Information
  rd_mgi_1_helpdesk_webpage: DS.attr({
    label: 'resource.fields.rd_mgi_1_helpdesk_webpage',
    hint: 'resource.hints.rd_mgi_1_helpdesk_webpage',
  }),
  rd_mgi_2_helpdesk_email: DS.attr({
    label: 'resource.fields.rd_mgi_2_helpdesk_email',
    hint: 'resource.hints.rd_mgi_2_helpdesk_email',
  }),
  rd_mgi_3_user_manual: DS.attr({
    label: 'resource.fields.rd_mgi_3_user_manual',
    hint: 'resource.hints.rd_mgi_3_user_manual',
  }),
  rd_mgi_4_terms_of_use: DS.attr({
    label: 'resource.fields.rd_mgi_4_terms_of_use',
    hint: 'resource.hints.rd_mgi_4_terms_of_use',
  }),
  rd_mgi_5_privacy_policy: DS.attr({
    label: 'resource.fields.rd_mgi_5_privacy_policy',
    hint: 'resource.hints.rd_mgi_5_privacy_policy',
  }),
  rd_mgi_6_sla_specification: DS.attr({
    label: 'resource.fields.rd_mgi_6_sla_specification',
    hint: 'resource.hints.rd_mgi_6_sla_specification',
  }),
  rd_mgi_7_training_information: DS.attr({
    label: 'resource.fields.rd_mgi_7_training_information',
    hint: 'resource.hints.rd_mgi_7_training_information',
  }),
  rd_mgi_8_status_monitoring: DS.attr({
    label: 'resource.fields.rd_mgi_8_status_monitoring',
    hint: 'resource.hints.rd_mgi_8_status_monitoring',
  }),
  rd_mgi_9_maintenance: DS.attr({
    label: 'resource.fields.rd_mgi_9_maintenance',
    hint: 'resource.hints.rd_mgi_9_maintenance',
  }),
  // Geographical and Language availability fields
  rd_gla_1_geographical_availability: DS.attr({
    defaultValue: 'Europe',
    label: 'resource.fields.rd_gla_1_geographical_availability',
    hint: 'resource.hints.rd_gla_1_geographical_availability',
    formComponent: 'agora-chips',
    formAttrs: {
      options: countries,
      exactMatch: true,
    }
  }),
  rd_gla_2_language: DS.attr({
    formComponent: 'agora-chips',
    label: 'resource.fields.rd_gla_2_language',
    hint: 'resource.hints.rd_gla_2_language',
    formAttrs: {
      options: language_codes,
      exactMatch: true,
    },
  }),

  main_contact: DS.belongsTo('contact-information', {
    label: 'resource.fields.main_contact',
    hint: 'resource.hints.main_contact',
  }),
  public_contact: DS.belongsTo('contact-information', {
    label: 'resource.fields.public_contact',
    hint: 'resource.hints.public_contact',
  }),

  resource_admins_ids: DS.attr(),

  __api__: {
    serialize: function(hash) {
      // do not send readonly keys to backend
      delete hash['providers_names'];
      delete hash['resource_admins_ids'];
      delete hash['rd_mri_5_target_users_verbose'];
      delete hash['domain_names'];
      delete hash['subdomain_names'];
      return hash;
    },
  },
});
