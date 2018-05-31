import Ember from 'ember';
import ENV from 'agora-admin/config/environment';

const {
  get
} = Ember;


const DEFAULT_ROUTE = ENV.APP.default_route || 'component.index';

export default Ember.Route.extend({
  session: Ember.inject.service(),
  beforeModel(transition) {
    if (get(this, 'session.isAuthenticated')) {
      let role = get(this, 'session.session.authenticated.role');
      transition.abort();
      return this.transitionTo(DEFAULT_ROUTE);
    }
  }
});
