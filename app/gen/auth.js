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
          //resetHash(window);
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
            user.auth_token = token;
            //resetHash(window);
            this.get('messageService').setSuccess('login.success');
            return session.authenticate('authenticator:agora', user);
          });
        })
      },
    }]
  }
});
