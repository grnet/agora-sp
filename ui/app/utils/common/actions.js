import Ember from 'ember';

const {
  computed,
  get,
} = Ember;

const rejectResourceAdminship = {
  label: 'resource_admin.reject.label',
  icon: 'block',
  accent: true,
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'rejected');
    model.save().then((value) => {
      m.setSuccess('resource_admin.reject.success');

      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('resource_admin.reject.error');

      return reason.errors;
    });
  },
  hidden: computed('model.state', 'model.admin_id', function(){
    let user_id = get(this, 'session.session.authenticated.id').toString();
    let admin_id = get(this, 'model.admin_id');
    let state = get(this, 'model.state');

    if (admin_id === user_id) { return true; }

    return !(state === 'pending')
  }),
  confirm: true,
  prompt: {
    ok: 'resource_admin.reject.ok',
    cancel: 'cancel',
    message: 'resource_admin.reject.message',
    title: 'resource_admin.reject.title',
  },
};

const approveResourceAdminship = {
  label: 'resource_admin.approve.label',
  icon: 'check',
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'approved');
    model.save().then((value) => {
      m.setSuccess('resource_admin.approve.success');

      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('resource_admin.approve.error');

      return reason.errors;
    });
  },
  hidden: computed('model.state', 'model.admin_id', function(){
    let user_id = get(this, 'session.session.authenticated.id').toString();
    let admin_id = get(this, 'model.admin_id');
    let state = get(this, 'model.state');

    if (admin_id === user_id) { return true; }

    return !(state === 'pending')
  }),
  confirm: true,
  prompt: {
    ok: 'resource_admin.approve.ok',
    cancel: 'cancel',
    message: 'resource_admin.approve.message',
    title: 'resource_admin.approve.title',
  },
};

const undoResourceAdminship = {
  label: 'resource_admin.undo.label',
  icon: 'undo',
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'pending');
    model.save().then((value) => {
      m.setSuccess('resource_admin.undo.success');

      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('resource_admin.undo.error');

      return reason.errors;
    });
  },
  hidden: computed('model.state', 'model.admin_id', function(){
    let user_id = get(this, 'session.session.authenticated.id').toString();
    let admin_id = get(this, 'model.admin_id');
    let state = get(this, 'model.state');

    if (admin_id === user_id) { return true; }

    return state === 'pending'
  }),
  confirm: true,
  prompt: {
    ok: 'resource_admin.undo.ok',
    cancel: 'cancel',
    message: 'resource_admin.undo.message',
    title: 'resource_admin.undo.title',
  },
};

const applyResourceAdminship = {
  label: 'resource_admin.apply.label',
  icon: 'grade',
  action: function(route, model) {
    let m = route.get('messageService');
    let store = route.get('store');
    let resource_admin = store.createRecord('resource-admin', {
      resource: model,
    })

    resource_admin.save().then((value) => {
      model.reload().then(() => {
        m.setSuccess('resource_admin.apply.success');
      })
    }, (error) => {
      let msg = error.errors && error.errors[0].detail || 'resource_admin.apply.error'
      m.setError(msg);
    });
  },
  hidden: computed('model.can_apply_adminship', function(){
    return !get(this, 'model.can_apply_adminship');
  }),
  confirm: true,
  prompt: {
    ok: 'resource_admin.apply.ok',
    cancel: 'cancel',
    message: 'resource_admin.apply.message',
    title: 'resource_admin.apply.title',
  },
};

const revokeResourceAdminship = {
  label: 'resource_admin.revoke.label',
  icon: 'undo',
  action: function(route, model) {
    let m = route.get('messageService');
    let store = route.get('store');
    let user_id = get(route, 'session.session.authenticated.id');

    return store.query('resource-admin', {
      admin: user_id,
      resource: model.id,
      state: 'pending',
    }).then(function(res) {
      if (get(res, 'length') === 1) {
        res.forEach(function(el) {
          el.destroyRecord().then(()=> {
            model.reload().then(()=> {
              m.setSuccess('resource_admin.revoke.success');
            })
          }).catch((err)=> {
            throw err;
          })
        })
      } else {
        m.setError('resource_admin.revoke.error!!!!');
      }
    });
  },
  hidden: computed('model.can_revoke_adminship', function(){
    return !get(this, 'model.can_revoke_adminship');
  }),
  confirm: true,
  prompt: {
    ok: 'resource_admin.revoke.ok',
    cancel: 'cancel',
    message: 'resource_admin.revoke.message',
    title: 'resource_admin.revoke.title',
  },
};

const informAdminshipRejected = {
  label: 'resource_admin.inform_rejected.label',
  icon: 'warning',
  action: function() {},
  hidden: computed('model.has_rejected_adminship', function(){
    return !get(this, 'model.has_rejected_adminship');
  }),
  confirm: true,
  prompt: {
    message: 'resource_admin.inform_rejected.message',
    title: 'resource_admin.inform_rejected.title',
    noControls: true,
  },
};

const publishProvider = {
  label: 'provider.publish.label',
  icon: 'public',
  classNames: 'md-icon-success',
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'published');
    model.save().then((value) => {
      m.setSuccess('provider.publish.success');
      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('provider.publish.error');
      return reason.errors;
    });
  },
  hidden: computed('role', 'model.state', function(){
    let role = get(this, 'role');
    let state =  get(this, 'model.state');
    if (role !== 'superadmin' && role!=='portfolioadmin') { return true; }
    if (state === 'published') { return true;}
    return false;
  }),
  confirm: true,
  prompt: {
    ok: 'provider.publish.ok',
    cancel: 'cancel',
    message: 'provider.publish.message',
    title: 'provider.publish.title',
  },
};

const unpublishProvider = {
  label: 'provider.unpublish.label',
  icon: 'block',
  accent: true,
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'draft');
    model.save().then((value) => {
      m.setSuccess('provider.unpublish.success');
      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('provider.unpublish.error');
      return reason.errors;
    });
  },
  hidden: computed('role', 'model.state', function(){
    let role = get(this, 'role');
    let state =  get(this, 'model.state');
    if (role !== 'superadmin' && role!=='portfolioadmin') { return true; }
    if (state === 'published') { return false;}
    return true;
  }),
  confirm: true,
  prompt: {
    ok: 'provider.unpublish.ok',
    cancel: 'cancel',
    message: 'provider.unpublish.message',
    title: 'provider.unpublish.title',
  },
};

const publishResource = {
  label: 'resource.publish.label',
  icon: 'public',
  classNames: 'md-icon-success',
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'published');
    model.save().then((value) => {
      m.setSuccess('resource.publish.success');
      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('resource.publish.error');
      return reason.errors;
    });
  },
  hidden: computed('role', 'model.state', 'user.organisation', 'model.erp_bai_service_organisation', function(){
    let role = get(this, 'role');
    let state =  get(this, 'model.state');
    let resource_org = get(this, 'model.erp_bai_service_organisation.id');
    let user_org = get(this, 'session.session.authenticated.organisation');
    if (role === 'observer') {
      return true;
    }
    if (role === 'serviceadmin') {
      return true;
    }

    if (role === 'provideradmin' && user_org !== resource_org) {
      return true;
    }
    if (state === 'published') { return true;}
    return false;
  }),
  confirm: true,
  prompt: {
    ok: 'resource.publish.ok',
    cancel: 'cancel',
    message: 'resource.publish.message',
    title: 'resource.publish.title',
  },
};

const unpublishResource = {
  label: 'resource.unpublish.label',
  icon: 'block',
  accent: true,
  action: function(route, model) {
    let m = route.get('messageService');

    model.set('state', 'draft');
    model.save().then((value) => {
      m.setSuccess('resource.unpublish.success');
      return value;
    }, (reason) => {
      model.rollbackAttributes();
      m.setError('resource.unpublish.error');
      return reason.errors;
    });
  },
  hidden: computed('role', 'model.state', 'model.erp_bai_service_organisation', function(){
    let role = get(this, 'role');
    let state =  get(this, 'model.state');
    let resource_org = get(this, 'model.erp_bai_service_organisation.id');
    let user_org = get(this, 'session.session.authenticated.organisation');
    if (role === 'observer') {
      return true;
    }
    if (role === 'serviceadmin') {
      return true;
    }

    if (role === 'provideradmin' && user_org !== resource_org) {
      return true;
    }
    if (state === 'published') { return false;}
    return true;
  }),
  confirm: true,
  prompt: {
    ok: 'resource.unpublish.ok',
    cancel: 'cancel',
    message: 'resource.unpublish.message',
    title: 'resource.unpublish.title',
  },
};

export {
  rejectResourceAdminship,
  approveResourceAdminship,
  undoResourceAdminship,
  applyResourceAdminship,
  revokeResourceAdminship,
  informAdminshipRejected,
  publishProvider,
  unpublishProvider,
  publishResource,
  unpublishResource,
}
