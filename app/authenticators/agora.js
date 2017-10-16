import Ember from 'ember';
import ApimasAuthenticator from 'ember-gen-apimas/authenticators/apimas';

export default ApimasAuthenticator.extend({
  processProfileData(data, profile) {
   /* let user = profile.user;
    user.user_id = user.id.toString();
    delete user.id;
    delete profile.user;

    merge(data, user);
    merge(data, profile);

    if(data.id) {
      data.id = data.id.toString();
    }

    if (data.hasOwnProperty('is_verified') && data.is_verified === false) {
      data.pending_role = data.role;
      delete data.role;
    }*/
    return data;
  }
});
