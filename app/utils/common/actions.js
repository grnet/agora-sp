import Ember from 'ember';

const {
  computed,
  get,
} = Ember;

const rejectServiceAdminship = {
  label: 'service_admin.reject.label',
  icon: 'block',
  accent: true,
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'rejected');
    model.save().then((value) => {
      m.setSuccess('service_admin.reject.success');

      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('service_admin.reject.error');

      return reason.errors;
    });
  },
  hidden: computed('model.state', 'role', function(){
    let state = get(this, 'model.state');

    return !(state === 'pending')
  }),
  confirm: true,
  prompt: {
    ok: 'service_admin.reject.ok',
    cancel: 'cancel',
    message: 'service_admin.reject.message',
    title: 'service_admin.reject.title',
  },
};

const approveServiceAdminship = {
  label: 'service_admin.approve.label',
  icon: 'check',
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'approved');
    model.save().then((value) => {
      m.setSuccess('service_admin.approve.success');

      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('service_admin.approve.error');

      return reason.errors;
    });
  },
  hidden: computed('model.state', function(){
    let state = get(this, 'model.state');

    return !(state === 'pending')
  }),
  confirm: true,
  prompt: {
    ok: 'service_admin.approve.ok',
    cancel: 'cancel',
    message: 'service_admin.approve.message',
    title: 'service_admin.approve.title',
  },
};

const undoServiceAdminship = {
  label: 'service_admin.undo.label',
  icon: 'undo',
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'pending');
    model.save().then((value) => {
      m.setSuccess('service_admin.undo.success');

      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('service_admin.undo.error');

      return reason.errors;
    });
  },
  hidden: computed('model.state', 'model.admin.id', function(){
    let admin_id = get(this, 'model.admin.id');

    if (admin_id) { return true; }

    let state = get(this, 'model.state');

    return state === 'pending'
  }),
  confirm: true,
  prompt: {
    ok: 'service_admin.undo.ok',
    cancel: 'cancel',
    message: 'service_admin.undo.message',
    title: 'service_admin.undo.title',
  },
};

const applyServiceAdminship = {
  label: 'service_admin.apply.label',
  icon: 'grade',
  action: function(route, model) {
    let m = route.get('messageService');
    let store = route.get('store');
    let service_admin = store.createRecord('service-admin', {
      service: model,
    })

    service_admin.save().then((value) => {
      model.reload().then(() => {
        m.setSuccess('service_admin.apply.success');
      })
    }, (error) => {
      m.setError('service_admin.apply.error');
    });
  },
  hidden: computed('model.can_apply_adminship', function(){
    return !get(this, 'model.can_apply_adminship');
  }),
  confirm: true,
  prompt: {
    ok: 'service_admin.apply.ok',
    cancel: 'cancel',
    message: 'service_admin.apply.message',
    title: 'service_admin.apply.title',
  },
};

const revokeServiceAdminship = {
  label: 'service_admin.revoke.label',
  icon: 'undo',
  action: function(route, model) {
    let m = route.get('messageService');
    let store = route.get('store');
    let user_id = get(route, 'session.session.authenticated.id');

    return store.query('service-admin', {
      admin: user_id,
      service: model.id,
      state: 'pending',
    }).then(function(res) {
      if (get(res, 'length') === 1) {
        res.forEach(function(el) {
          el.destroyRecord().then(()=> {
            model.reload().then(()=> {
              m.setSuccess('service_admin.revoke.success');
            })
          }).catch((err)=> {
            throw err;
          })
        })
      } else {
        m.setError('service_admin.revoke.error!!!!');
      }
    });
  },
  hidden: computed('model.can_revoke_adminship', function(){
    return !get(this, 'model.can_revoke_adminship');
  }),
  confirm: true,
  prompt: {
    ok: 'service_admin.revoke.ok',
    cancel: 'cancel',
    message: 'service_admin.revoke.message',
    title: 'service_admin.revoke.title',
  },
};

const informAdminshipRejected = {
  label: 'service_admin.inform_rejected.label',
  icon: 'warning',
  action: function() {},
  hidden: computed('model.has_rejected_adminship', function(){
    return !get(this, 'model.has_rejected_adminship');
  }),
  confirm: true,
  prompt: {
    message: 'service_admin.inform_rejected.message',
    title: 'service_admin.inform_rejected.title',
    noControls: true,
  },
};

export {
  rejectServiceAdminship,
  approveServiceAdminship,
  undoServiceAdminship,
  applyServiceAdminship,
  revokeServiceAdminship,
  informAdminshipRejected,
}
