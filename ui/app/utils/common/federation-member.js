import { field } from 'ember-gen';
import { fileField } from '../../lib/common';

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'federation_member.cards.basic_information',
    text: 'federation_member.cards.basic_hint',
    layout: {
      flex: [100, 75, 25, 100],
    },
    fields: [
      'name',
      'webpage',
      'country',
      fileField( 'logo', 'federation-member', 'logo', {
          readonly: true,
        }, {
          img: true,
        }
      ),
    ],
  },
];

/********************************************
                EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [
  {
    label: 'federation_member.cards.basic_information',
    text: 'federation_member.cards.basic_hint',
    layout: {
      flex: [100, 50, 50, 100],
    },
    fields: [
      'name',
      'webpage',
      'country',
      fileField( 'logo', 'federation-member', 'logo', {
        },{
          img: true,
        }
      ),
    ],
  },
];

/********************************************
                CREATE  VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'federation_member.cards.basic_information',
    text: 'federation_member.cards.basic_hint',
    layout: {
      flex: [100, 50, 50],
    },
    fields: ['name', 'webpage', 'country'],
  },
];

export { DETAILS_FIELDSETS, EDIT_FIELDSETS, CREATE_FIELDSETS };
