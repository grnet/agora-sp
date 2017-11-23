import DS from 'ember-data';
import Ember from 'ember';
import { shorten } from '../utils/common/common';

export default DS.Model.extend({
  name: DS.attr(),
  service_type: DS.attr(),
  funders_for_service: DS.attr(),
  description_external: DS.attr(),
  value_to_customer: DS.attr(),
  risks: DS.attr(),
  description_internal: DS.attr(),
  short_description: DS.attr(),
  competitors: DS.attr(),
  logo: DS.attr(),
  request_procedures: DS.attr(),
  service_version_url: Ember.computed('id', function() {
    return `/service-versions/create?service=${Ember.get(this, 'id')}`;
  }),
  service_area: DS.belongsTo('service-area', {
    formAttrs: {
      optionLabelAttr: 'name'
    }
  }),
  id_contact_information: DS.belongsTo('contact-information', {
    formAttrs: {
      optionLabelAttr: 'full_name'
    }
  }),
  id_contact_information_internal: DS.belongsTo('contact-information', {
    formAttrs: {
      optionLabelAttr: 'full_name'
    }
  }),
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
  //computed
  short_desc: Ember.computed('short_description', function() {
    return shorten(Ember.get(this, 'short_description'));
  }),
  __api__: {
    path: 'services'
  }
});
