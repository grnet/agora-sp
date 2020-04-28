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
      optionLabelAttr: 'name',
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

  __api__: {
    serialize: function(hash) {
      // do not send readonly keys to backend
      delete hash['providers_names'];
      delete hash['rd_mri_5_target_users_verbose'];
      return hash;
    },
  },
});
