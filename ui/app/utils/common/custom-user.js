import { field } from 'ember-gen';
import Ember from 'ember';

const {
  set,
  get,
  computed
} = Ember;

const providers = field('providers', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: [
        'name',
      ]
    }
  }
})

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [{
  label: 'custom_user.cards.basic_information',
  text: 'custom_user.cards.basic_hint',
  layout: {
    flex: [50, 50, 50, 50, 50, 50, 50, 50, 100]
  },
  fields: computed('role', 'model.role', function() {
    let role = get(this, 'role');
    let model_role = get(this, 'model.role');
    let fields = [
      'username',
      'full_name',
      field('date_joined_format', {
        label: 'custom_user.fields.date_joined',
        hint: 'custom_user.hints.date_joined'
      }),
      'shibboleth_id',
      'email',
      field('role_verbose', {
        label: 'custom_user.fields.role',
      })
    ];
    if ( (role === 'superadmin' || role === 'provideradmin') &&
        (model_role==='serviceadmin' ||  model_role==='provideradmin')) {
      fields.push('organisation');
    }
    return fields;
  }),
}]


/********************************************
           CREATE  OR EDIT VIEW
********************************************/

const CREATE_OR_EDIT_FIELDSETS = [{
  label: 'custom_user.cards.basic_information',
  text: 'custom_user.cards.basic_hint',
  fields: [
    'username',
    'first_name',
    'last_name',
    'email',
    'role',
    field('organisation', {
      disabled: computed('mode.role', 'model.changeset.role', function(){
        let role = get(this, 'model.role');
        let changed_role = get(this, 'model.changeset.role');
        let no_org_roles = ['superadmin', 'observer', 'portfolioadmin'];
        if (no_org_roles.includes(changed_role)) {
          Ember.run.once(this, () => {
            get(this, 'model').set('organisation', null);
            get(this, 'model.changeset').set('organisation', null);
          });
          return true;
        } else {
          return false;
        }


      })

    }),
  ]
}]


const PROFILE_FIELDSETS = [{
  label: 'profile.cards.basic_information',
  text: 'profile.cards.basic_hint',
  fields: computed('role', 'model.role', function() {
    let role = get(this, 'role');
    let model_role = get(this, 'model.role');
    let fields = [
      field('username', {class: 'skata', fattrs: {class: 'skata'}}),
      'email',
      'role',
      'full_name',
    ];
    if (model_role === 'serviceadmin' || model_role === 'provideradmin') {
      fields.push('organisation');
    }
    return fields;
  }),
  layout: {
    flex: [50, 50, 50, 50, 100]
  }
}]

export {
  PROFILE_FIELDSETS,
  DETAILS_FIELDSETS,
  CREATE_OR_EDIT_FIELDSETS,
}
