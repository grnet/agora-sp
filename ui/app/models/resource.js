import DS from 'ember-data';

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

  __api__: {
    serialize: function(hash) {
      // do not send readonly keys to backend
      delete hash['providers_names'];
      delete hash['rd_mri_5_target_users_verbose'];
      return hash;
    },
  },
});
