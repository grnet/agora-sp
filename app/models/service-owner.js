import DS from 'ember-data';
import ENV from '../config/environment';

const CHOICES = ENV.APP.resources;

export default DS.Model.extend({
  owner: DS.belongsTo('custom-user', {
    formAttrs: {
      optionLabelAttr: 'username',
    },
  }),
  service: DS.belongsTo('service-item', {
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  state: DS.attr({ type: 'select', choices: CHOICES.SERVICE_OWNERSHIP_STATES }),

});
