import { field } from 'ember-gen';
import { fileField } from '../../lib/common';

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'service_provider.cards.basic_information',
    text: 'service_provider.cards.basic_hint',
    layout: {
      flex: [100, 75, 25, 100],
    },
    fields: [
      'name',
      'webpage',
      'country',
      fileField( 'logo', 'service-provider', 'logo', {
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
    label: 'service_provider.cards.basic_information',
    text: 'service_provider.cards.basic_hint',
    layout: {
      flex: [100, 50, 50, 100],
    },
    fields: [
      'name',
      'webpage',
      'country',
      fileField( 'logo', 'service-provider', 'logo', {
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
    label: 'service_provider.cards.basic_information',
    text: 'service_provider.cards.basic_hint',
    layout: {
      flex: [100, 50, 50],
    },
    fields: ['name', 'webpage', 'country'],
  },
];

export { DETAILS_FIELDSETS, EDIT_FIELDSETS, CREATE_FIELDSETS };
