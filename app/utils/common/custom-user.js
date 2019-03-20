import { field } from 'ember-gen';
import Ember from 'ember';

const {
  get,
  computed
} = Ember;

const organisations = field('organisations', {
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
      'is_active',
      'is_staff',
      'role'
    ];
    if (role === 'superadmin' && model_role === 'serviceadmin') {
      fields.push(organisations);
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
  fields: computed('role', 'model.role', function() {
    let role = get(this, 'role');
    let model_role = get(this, 'model.role');
    let fields = [
      'username',
      'first_name',
      'last_name',
      'email',
      'is_active',
      'is_staff',
      'role',
    ];
    if (role === 'superadmin' && model_role === 'serviceadmin') {
      fields.push(organisations);
    }
    return fields;
  }),
}]


export {
  DETAILS_FIELDSETS,
  CREATE_OR_EDIT_FIELDSETS,
}
