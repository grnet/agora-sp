import Ember from 'ember';
import ApimasAuthenticator from 'ember-gen-apimas/authenticators/apimas';

export default ApimasAuthenticator.extend({
  processProfileData(data, profile) {
    Ember.merge(data, profile);
    return data;
  }
});
