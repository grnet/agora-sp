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
  pd_bai_3_legal_status: DS.attr({
    type: 'select',
    choices: ENV.APP.resources.LEGAL_STATUSES,
    label: 'provider.fields.pd_bai_3_legal_status',
    hint: 'provider.hints.pd_bai_3_legal_status',
  }),

  // computed
  short_desc: computed('description', function() {
    return shorten(get(this, 'description'));
  }),
});
