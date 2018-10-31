import DS from 'ember-data';
import gen from 'ember-gen/lib/attrs';

export default DS.Model.extend({
  privacy_policy_has: DS.attr({ type: 'boolean' }),
  privacy_policy_url: DS.attr(),
  monitoring_has: DS.attr({ type: 'boolean' }),
  monitoring_url: DS.attr(),
  user_documentation_has: DS.attr({ type: 'boolean' }),
  user_documentation_url: DS.attr(),
  decommissioning_procedure_has: DS.attr({ type: 'boolean' }),
  decommissioning_procedure_url: DS.attr(),
  accounting_has: DS.attr({ type: 'boolean' }),
  accounting_url: DS.attr(),
  operations_documentation_has: DS.attr({ type: 'boolean' }),
  operations_documentation_url: DS.attr(),
  business_continuity_plan_has: DS.attr({ type: 'boolean' }),
  business_continuity_plan_url: DS.attr(),
  disaster_recovery_plan_has: DS.attr({ type: 'boolean' }),
  disaster_recovery_plan_url: DS.attr(),
  usage_policy_has: DS.attr({ type: 'boolean' }),
  usage_policy_url: DS.attr(),
  features_current: DS.attr(),
  features_future: DS.attr(),
  cost_to_run: DS.attr(),
  version: DS.attr(),
  cost_to_build: DS.attr(),
  use_cases: DS.attr(),
  is_in_catalogue: DS.attr({ type: 'boolean' }),
  visible_to_marketplace: DS.attr({ type: 'boolean' }),
  cidl_url: Ember.computed('id', 'id_service.id', function() {
    const service =  Ember.get(this, 'id_service.id');
    const service_version = Ember.get(this, 'id');
    return `/component-implementation-detail-links/create?service=${service}&service_version=${service_version}`;
  }),
  //the object resembles the value to be printed in the create/update page of this referenced model
  //e.g. name is a key from the service-item model
  id_service: gen.belongsTo('service_item', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  status: gen.belongsTo('service_status', {
    formAttrs: {
      optionLabelAttr: 'value'
    }
  })
});
