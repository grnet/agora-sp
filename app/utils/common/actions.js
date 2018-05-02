import Ember from 'ember';

const {
  computed,
  get,
} = Ember;

const rejectServiceAdminship = {
  label: 'service_membership.reject.label',
  icon: 'cancel',
  accent: true,
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'rejected');
    model.save().then((value) => {
      m.setSuccess('form.saved');

      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('reason.errors');

      return reason.errors;
    });
  },
  hidden: computed('model.state', 'role', 'user.role', function(){
    let state = get(this, 'model.state');
    let role = get(this, 'role');

    if (!(['superadmin', 'admin'].includes(role))) { return true; }
    if (state === 'rejected') { return true; }

    return false;
  }),
  confirm: true,
  prompt: {
    ok: 'submit',
    cancel: 'cancel',
    message: 'service_adminship.reject.message',
    title: 'service_adminship.reject.title',
  },
};

const approveServiceAdminship = {
  label: 'service_adminship.approve.label',
  icon: 'check_circle',
  classNames: 'md-icon-success',
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'approved');
    model.save().then((value) => {
      m.setSuccess('form.saved');

      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('reason.errors');

      return reason.errors;
    });
  },
  hidden: computed('model.state', 'role', function(){
    let state = get(this, 'model.state');
    let role = get(this, 'role');

    if (!(['superadmin', 'admin'].includes(role))) { return true; }
    if (state === 'approved') { return true; }

    return false;
  }),
  confirm: true,
  prompt: {
    ok: 'submit',
    cancel: 'cancel',
    message: 'service_adminship.approve.message',
    title: 'service_adminship.approve.title',
  },
};

const applyServiceAdminship = {
  label: 'service_adminship.apply.label',
  icon: 'grade',
  action: function(route, model) {
    return;
  },
  hidden: computed('role', 'model.service_admins_ids', 'user.id', function(){
    let ids = get(this, 'model.service_admins_ids');
    let user_id = get(this, 'user.id').toString();
    let role = get(this, 'role');

    if (role !== 'serviceadmin') { return true; }
    if (ids.includes(user_id)) { return true; }

    return false;
  }),
  confirm: true,
  prompt: {
    ok: 'submit',
    cancel: 'cancel',
    message: 'service_adminship.apply.message',
    title: 'service_adminship.apply.title',
  },
};

export {
  rejectServiceAdminship,
  approveServiceAdminship,
  applyServiceAdminship,
}
