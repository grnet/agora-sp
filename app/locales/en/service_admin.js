const service_admin = {
  'cards': {
    'basic_information': 'Basic information',
    'basic_hint': ''
  },
  'fields': {
    'service_name': 'Service name',
    'admin_email': 'Admin email',
    'admin_full_name': 'Admin name',
    'state': 'State',
  },
  'hints': {
    'service_name': '',
    'admin_email': '',
    'state': '',
  },
  'menu': 'Service Admins',
  'belongs': {
    'full_name': 'Service Admin'
  },
  'inform_rejected': {
    'label': 'Application rejected',
    'title': 'Application rejected',
    'message': 'Your application for service admin has been rejected.',
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
    'message': 'Service admins can edit service details.<br> Are you sure you want to apply?',
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
    'message': 'The approved user will be able to edit service details.<br>Are you sure you want to approve this application?',
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
  }
};

export { service_admin };
