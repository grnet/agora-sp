import { field } from 'ember-gen';


const SORT_FIELDS = [
  'name',
];

const TABLE_FIELDS = [
  field('name', {label: 'structure.table.name'}),
];


const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'structure.cards.basic',
  fields: [
    'name',
  ],
  layout: {
    flex: [100],
  },
};


const BASIC_INFO_FIELDSET = {
  label: 'structure.cards.basic',
  fields: [
    'name',
  ],
  layout: {
    flex: [100],
  },
};

const DETAILS_FIELDSETS = [
  DETAILS_BASIC_INFO_FIELDSET,
];

const CREATE_FIELDSETS = [
  BASIC_INFO_FIELDSET,
];

const EDIT_FIELDSETS = [
  BASIC_INFO_FIELDSET,
];

export {
  TABLE_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  SORT_FIELDS,
}
