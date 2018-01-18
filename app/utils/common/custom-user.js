import { field } from 'ember-gen';


/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [{
  label: 'custom_user.cards.basic_information',
  text: 'custom_user.cards.basic_hint',
  layout: {
    flex: [50, 50, 50, 50, 50, 50, 50, 50]
  },
  fields: [
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
  ]
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
    'is_active',
    'is_staff',
    'role'
  ]
}]


export {
  DETAILS_FIELDSETS,
  CREATE_OR_EDIT_FIELDSETS,
}
