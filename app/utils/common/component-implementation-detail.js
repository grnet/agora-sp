import { field } from 'ember-gen';

const SORT_FIELDS = [
  'version',
];

/********************************************
                LIST VIEW
********************************************/

const TABLE_FIELDS = [
  field('component_id.name', {
    type: 'text',
    label: 'component.belongs.name'
  }),
  field('component_implementation_id.name', {
    type: 'text',
    label: 'component_implementation.belongs.name'
  }),
  field('version', {
    type: 'text',
    label: 'component_implementation_detail.fields.version'
  }),
];

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'component_implementation.cards.basic_information',
    fields: [
      field('version', {
        type: 'text',
        label: 'component_implementation_detail.fields.version'
      }),
      field('component_implementation_id.name', {
        type: 'text',
        label: 'component_implementation.belongs.name'
      }),
      field('component_id.name', {
        type: 'text',
        label: 'component.belongs.name'
      }),
    ]
  }
];

/********************************************
            EDIT VIEW/CREATE VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'component_implementation_detail.cards.basic_information',
    fields: [
      field('component_id', {
        label: 'component.belongs.name'
      }),
      field('component_implementation_id', {
        label: 'component_implementation.belongs.name'
      }),
      field('version', {
        type: 'text',
        label: 'component_implementation_detail.fields.version'
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
