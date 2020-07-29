const resource_admin = {
  'cards': {
    'basic_information': 'Basic information',
    'basic_hint': '',
    'admin_info': 'Administrator',
    'resource_info': 'resource',
  },
  'fields': {
    'resource_name': 'Resource name',
    'admin_email': 'Admin email',
    'admin_full_name': 'Admin name',
    'state': 'State',
    'created_at': 'Created',
    'updated_at': 'Updated',
  },
  'hints': {
    'resource_name': '',
    'admin_email': '',
    'state': '',
  },
  'menu': 'Resource Admins',
  'belongs': {
    'full_name': 'Resource Admin',
  },
  'inform_rejected': {
    'label': 'Application rejected',
    'title': 'Application rejected',
    'message': 'Your application for resource admin has been rejected.',
  },
  'revoke': {
    'label': 'Revoke application',
    'message': 'Are you sure you want to revoke your application?',
    'title': 'Revoke application',
    'success': 'Your application has been revoked.',
    'error': 'Error',
    'ok': 'revoke',
  },
  'apply': {
    'label': 'Apply for admin',
    'message': 'Resource admins can edit resources.<br> Are you sure you want to apply?',
    'title': 'Apply for admin',
    'success': 'You will be informed via email when your application gets reviewed.',
    'error': 'Error',
    'ok': 'apply',
  },
  'reject': {
    'label': 'Reject application',
    'message': 'Are you sure you want to reject this application?',
    'title': 'Reject application',
    'success': 'Application successfully rejected.',
    'error': 'Error',
    'ok': 'reject',
  },
  'approve': {
    'label': 'Approve application',
    'message': 'The approved user will be able to edit resource details.<br>Are you sure you want to approve this application?',
    'title': 'Approve application',
    'success': 'Application successfully approved.',
    'error': 'Error',
    'ok': 'approve',
  },
  'undo': {
    'label': 'Reassess application',
    'message': 'The application state will be set to <strong>pending</strong> and you can accept/reject it later.<br>Are you sure you want to continue?',
    'title': 'Reassess application',
    'success': 'Application\'s state successfully set to pending.',
    'error': 'Error',
    'ok': 'reassess',
  },
  'errors': {
    'object_exists': 'The user already admins the Resource you chose',
    'no_organisation': 'The user must be assigned to a Provider',
  }
};

export { resource_admin };
