import routes from 'ember-gen/lib/routes';
import gen from 'ember-gen/lib/gen';
import AuthGen from 'ember-gen/lib/auth';
import ENV from 'agora-admin/config/environment';

import {
  PROFILE_FIELDSETS,
} from '../utils/common/custom-user';


const {
    computed: { reads, not, equal },
    get, set, computed,
    merge
} = Ember;

export default AuthGen.extend({
  routeMixins: {
    actions: {
      shibbolethLogin() {
        window.location = ENV.APP.shibboleth_login_url + '?login=1'
      }
    }
  },
  login: {
    config: {
      authenticator: 'agora'
    },
    templateName: 'agora-login',
    routeMixins: [{
      handleTokenLogin(token) {
        if (get(this, 'session.isAuthenticated')) {
          localStorage.removeItem('auth_token');
          return;
        }
        let url = ENV.APP.backend_host + '/auth/me/';
        return fetch(url, {
          headers: {
          'Accept': 'application/json',
          'Authorization': `Token ${token}`
          }
        }).then((resp) => {
          if (resp.status !== 200) {
            return resp.json().then((json) => {
              this.get('messageService').setError('login.failed');
            });
          }
          return resp.json().then((user) => {
            let session = get(this, 'session');
            let authData = { auth_token: token, user: user }
            localStorage.removeItem('auth_token');
            this.get('messageService').setSuccess('login.success');
            return session.authenticate('authenticator:agora', authData);
          });
        })
      },
      beforeModel(transition) {
        const token = localStorage.getItem('auth_token');
        if (token) {
          return this.handleTokenLogin(decodeURI(token));
        }
        let error = localStorage.getItem('error');
        if (error) {
          this.get('messageService').setError(error);
          localStorage.removeItem('error');
        }
        return this._super(transition);
      },


    }]
  },

  profile: {
    modelName: 'custom-user',
    name: 'profile',
    gens: {
      details: gen.GenRoutedObject.extend({
        routeBaseClass: routes.DetailsRoute,
        component: 'gen-details',
        getModel() {
          let id = get(this, 'session.session.authenticated.id');
          return get(this, 'store').findRecord('custom-user', id);
        },
        fieldsets: PROFILE_FIELDSETS,
      })
    },
    page: {
      title: 'profile.menu',
    },
    menu: {
      order: 1,
      display: true,
      icon: 'portrait',
      label: 'profile.menu',
    },
    getModel() {
      let id = get(this, 'session.session.authenticated.id');
      return get(this, 'store').findRecord('custom-user', id).then((user)=>{
        this.transitionTo('auth.profile.details');
      })
    },
  },

});

