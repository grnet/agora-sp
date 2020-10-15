import Ember from 'ember';
import config from './config/environment';

const {
  get,
  getOwner,
}  = Ember;


const title = config.title || 'Agora Admin';

const Router = Ember.Router.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
});


Router.reopen({
  setTitle: function(title) {
    const container = getOwner ? getOwner(this) : this.container;
    const renderer = container.lookup('renderer:-dom');

    if (renderer) {
      Ember.set(renderer, '_dom.document.title', title);
    } else {
      document.title = title;
    }
  },
  init: function() {
    this.setTitle(title)
    this._super(...arguments);
  }
});

export default Router;
