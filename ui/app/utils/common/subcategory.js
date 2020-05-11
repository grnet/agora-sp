import { field } from 'ember-gen';


const SORT_FIELDS = [
  'category.name',
  'name',
];

const TABLE_FIELDS = [
  field('category.name', {label: 'subcategory.table.domain'}),
  field('name', {label: 'subcategory.table.name'}),
];


const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'subcategory.cards.basic',
  fields: [
    'category.name',
    'name',
  ],
  layout: {
    flex: [100,100],
  },
};


const BASIC_INFO_FIELDSET = {
  label: 'subcategory.cards.basic',
  fields: [
    'category',
    'name',
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
