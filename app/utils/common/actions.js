import Ember from 'ember';

const {
  computed,
  get,
} = Ember;

const rejectServiceOwnership = {
  label: 'reject.service_ownership',
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
    message: 'reject.service_ownership.message',
    title: 'reject.service_ownership.title',
  },
};

const approveServiceOwnership = {
  label: 'approve.service_ownership',
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
    message: 'approve.service_ownership.message',
    title: 'approve.service_ownership.title',
  },
};

const applyServiceOwnership = {
  label: 'apply.service_ownership',
  icon: 'grade',
  action: function(route, model) {
    return;
  },
  hidden: computed('role', 'model.service_owners_ids', 'user.id', function(){
    let ids = get(this, 'model.service_owners_ids');
    let user_id = get(this, 'user.id').toString();
    let role = get(this, 'role');

    if (role !== 'serviceowner') { return true; }
    if (ids.includes(user_id)) { return true; }

    return false;
  }),
  confirm: true,
  prompt: {
    ok: 'submit',
    cancel: 'cancel',
    message: 'apply.service_ownership.message',
    title: 'apply.service_ownership.title',
  },
};

export {
  rejectServiceOwnership,
  approveServiceOwnership,
  applyServiceOwnership,
}
