import ENV from 'agora-admin/config/environment';

const domestic_login_msg = ENV.APP.domestic_login_msg;

const login = {
  'domestic': {
    'description': 'You can login with your home organization account',
    'label': domestic_login_msg,
    'title': domestic_login_msg,
  },
  'default': {
    'description': 'You can login with username/password',
    'label': 'Username',
    'title': 'Login',
  }
}

export { login }
