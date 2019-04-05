import { field } from 'ember-gen';
import { fileField } from '../../lib/common';


/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [{
  label: 'provider.cards.basic_information',
  text: 'provider.cards.basic_hint',
  layout: {
    flex: [100, 100, 100]
  },
  fields: [
    'name',
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
      }
    ),
    fileField(
      'logo', 'provider', 'logo', {
        readonly: true,
      }, {
        img: true
      }
    ),
  ]
}]


/********************************************
                EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [{
  label: 'provider.cards.basic_information',
  text: 'provider.cards.basic_hint',
  layout: {
    flex: [100, 100, 100]
  },
  fields: [
    'name',
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
      }
    ),
    fileField(
      'logo', 'provider', 'logo', {
      }, {
        img: true
      }
    ),
  ]
}]



/********************************************
                CREATE  VIEW
********************************************/

const CREATE_FIELDSETS = [{
  label: 'provider.cards.basic_information',
  text: 'provider.cards.basic_hint',
  layout: {
    flex: [100, 100, 100]
  },
  fields: [
    'name',
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
      }
    ),
  ]
}]


export {
  DETAILS_FIELDSETS,
  EDIT_FIELDSETS,
  CREATE_FIELDSETS
};
