import Ember from 'ember';

const {
  get
} = Ember;


const DEFAULT_ROUTE = 'component.index';

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
