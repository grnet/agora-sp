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

  __api__: {
    serialize: function(hash, _) {
      // do not send readonly keys to backend
      delete hash['providers_names'];
      return hash;
    },
  },
});
