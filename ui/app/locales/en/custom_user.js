const custom_user = {
  'cards': {
    'basic_information': 'Basic information',
    'basic_hint': ''
  },
  'fields': {
    'username': 'Username',
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'full_name': 'Full Name',
    'email': 'Email',
    'is_active': 'Active',
    'is_staff': 'Staff',
    'date_joined': 'Date joined',
    'shibboleth_id': 'Shibboleth ID',
    'organisation':'Provider',
    'role': 'Role',
  },
  'hints': {
    'username': '',
    'first_name': '',
    'last_name': '',
    'full_name': '',
    'email': '',
    'is_active': '',
    'is_staff': '',
    'date_joined': '',
    'shibboleth_id': ''
  },
  'menu': 'Users',
  'placeholders': {
    'search': 'Search by username, full name or email',
  },
  errors:  {
    unique_email: 'A user with the same email already exists',
    unique_username: 'A user with the same username already exists'
  }

};

export { custom_user };
