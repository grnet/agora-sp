import DS from 'ember-data';
import { shorten } from '../utils/common/common';
import ENV from '../config/environment';

const {
  get,
  computed,
} = Ember;


export default DS.Model.extend({
  name: DS.attr({
    label: 'provider.fields.name',
    hint: 'provider.hints.name'
  }),
  description: DS.attr({
    label: 'provider.fields.description',
    hint: 'provider.hints.description'
  }),
  logo: DS.attr({
    label: 'provider.fields.logo',
    hint: 'provider.hints.logo'
  }),
  contact: DS.attr({
    label: 'provider.fields.contact',
    hint: 'provider.hints.contact',
  }),
  pd_bai_3_legal_entity: DS.attr({
    type: 'boolean',
    defaultValue: false,
    label: 'provider.fields.pd_bai_3_legal_entity',
    hint: 'provider.hints.pd_bai_3_legal_entity',
  }),
  pd_bai_0_id: DS.attr({
    label: 'provider.fields.pd_bai_0_id',
    hint: 'provider.hints.pd_bai_0_id',
  }),
  pd_bai_1_name: DS.attr({
    label: 'provider.fields.pd_bai_1_name',
    hint: 'provider.hints.pd_bai_1_name',
  }),
  pd_bai_2_abbreviation: DS.attr({
    label: 'provider.fields.pd_bai_2_abbreviation',
    hint: 'provider.hints.pd_bai_2_abbreviation',
  }),
  pd_bai_3_legal_status: DS.attr({
    type: 'select',
    choices: ENV.APP.resources.LEGAL_STATUSES,
    label: 'provider.fields.pd_bai_3_legal_status',
    hint: 'provider.hints.pd_bai_3_legal_status',
  }),
  pd_bai_4_website: DS.attr({
    label: 'provider.fields.pd_bai_4_website',
    hint: 'provider.hints.pd_bai_4_website',
  }),
  // computed
  short_desc: computed('description', function() {
    return shorten(get(this, 'description'));
  }),
});
