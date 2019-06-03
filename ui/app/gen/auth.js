import gen from 'ember-gen/lib/gen';
import AuthGen from 'ember-gen/lib/auth';
import ENV from 'agora-admin/config/environment';

//export default gen.CRUDGen.extend({
//  modelName: 'auth'
//});

const {
    computed: { reads, not, equal },
    get, set, computed,
    merge
} = Ember;

function extractToken(loc) {
  let token = loc.hash && loc.hash.split("token=")[1];
  if (token) { resetHash(window) };
  return token;
};


function resetHash(win, replace='') {
  if (win.history.replaceState) {
    win.history.replaceState(null, null, '#' + replace);
  } else {
    win.location.hash = replace;
  }
}



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
          resetHash(window);
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
            resetHash(window);
            this.get('messageService').setSuccess('login.success');
            return session.authenticate('authenticator:agora', authData);
          });
        })
      },
      beforeModel(transition) {
        let token = extractToken(window.location);
        if (token) {
          return this.handleTokenLogin(decodeURI(token));
        }
        return this._super(transition);
      },


    }]
  }
});
