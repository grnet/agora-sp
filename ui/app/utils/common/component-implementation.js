import { field } from 'ember-gen';

const SORT_FIELDS = [
  'name',
];

/********************************************
                LIST VIEW
********************************************/

const TABLE_FIELDS = [
  field('name', {
    type: 'text',
    label: 'component_implementation.fields.name'
  }),
  field('desc', {
    type: 'text',
    label: 'component_implementation.fields.description'
  }),
  field('component_id.name', {
    type: 'text',
    label: 'component.belongs.name'
  }),
];

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'component_implementation.cards.basic_information',
    fields: [
      field('name', {
        type: 'text',
        label: 'component_implementation.fields.name'
      }),
      field('description', {
        type: 'text',
        label: 'component_implementation.fields.description',
        htmlSafe: true
      }),
      field('component_id.name', {
        type: 'text',
        label: 'component.belongs.name'
      }),
    ],
    layout: {
      flex: [100, 100, 100]
    }
  }
];

/********************************************
            EDIT VIEW/CREATE VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'component_implementation.cards.basic_information',
    fields: [
      field('name', {
        type: 'text',
        label: 'component_implementation.fields.name'
      }),
      field('component_id', {
        label: 'component.belongs.name'
      }),
      field('description', {
        type: 'text',
        formComponent: 'text-editor',
        label: 'component_implementation.fields.description'
      }),
    ]
  }
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS
};
