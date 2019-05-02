import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr({
    label: 'access_policy.fields.name',
    hint: 'access_policy.hints.name',
  }),
  access_mode: DS.attr({
    label: 'access_policy.fields.access_mode',
    hint: 'access_policy.hints.access_mode',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  payment_model: DS.attr({
    label: 'access_policy.fields.payment_model',
    hint: 'access_policy.hints.payment_model',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  pricing: DS.attr({
    label: 'access_policy.fields.pricing',
    hint: 'access_policy.hints.pricing',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  conditions: DS.attr({
    label: 'access_policy.fields.conditions',
    hint: 'access_policy.hints.conditions',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  geo_availability: DS.attr({
    defaultValue: 'Europe',
    label: 'access_policy.fields.geo_availability',
    hint: 'access_policy.hints.geo_availability',
  }),
  access_policy_url: DS.attr({
    label: 'access_policy.fields.access_policy_url',
    hint: 'access_policy.hints.access_policy_url',
  }),

});
