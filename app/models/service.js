import DS from 'ember-data';

export default DS.Model.extend({
  service_type: DS.attr(),
  funders_for_service: DS.attr(),
  name: DS.attr(),
  description_external: DS.attr(),
  value_to_customer: DS.attr(),
  service_area: DS.attr(),
  service_trl: DS.belongsTo('service-trl'),
  competitors: DS.attr(),
  id_contact_information: DS.attr(),
  id_contact_information_internal: DS.attr(),
  risks: DS.attr(),
  description_internal: DS.attr(),
  short_description: DS.attr(),
  logo: DS.attr(),
  request_procedures: DS.attr(),
});
