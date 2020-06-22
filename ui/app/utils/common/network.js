import { field } from 'ember-gen';


const SORT_FIELDS = [
  'abbreviation',
  'name',
];

const TABLE_FIELDS = [
  field('abbreviation', {label: 'network.table.abbreviation'}),
  field('name', {label: 'network.table.name'}),
];


const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'network.cards.basic',
  fields: [
    'name',
    'abbreviation',
    
  ],
  layout: {
    flex: [100,100],
  },
};


const BASIC_INFO_FIELDSET = {
  label: 'network.cards.basic',
  fields: [
    'name',
    'abbreviation',
  ],
  layout: {
    flex: [100,100],
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
