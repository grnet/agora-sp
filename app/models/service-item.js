import DS from 'ember-data';
import Ember from 'ember';

export default DS.Model.extend({
  service_type: DS.attr(),
  funders_for_service: DS.attr(),
  name: DS.attr(),
  description_external: DS.attr(),
  value_to_customer: DS.attr(),
  service_area: DS.attr(),
  service_version_url: Ember.computed('id', function() {
    return `/service-versions/create?service=${Ember.get(this, 'id')}`;
  }),
  competitors: DS.attr(),
  id_contact_information: DS.belongsTo('contact-information', {
    formAttrs: {
      optionLabelAttr: 'first_name'
    }
  }),
  id_contact_information_internal: DS.belongsTo('contact-information', {
    formAttrs: {
      optionLabelAttr: 'first_name'
    }
  }),
  risks: DS.attr(),
  description_internal: DS.attr(),
  short_description: DS.attr(),
  logo: DS.attr(),
  request_procedures: DS.attr(),
  service_trl: DS.belongsTo('service-trl', {
    formAttrs: {
      optionLabelAttr: 'value'
    }
  }),
  id_service_owner: DS.belongsTo('service-owner', {
    formAttrs: {
      optionLabelAttr: 'full_name'
    }
  }),
  __api__: {
    path: 'services'
  }
});
