import { field } from 'ember-gen';
import ENV from '../../config/environment';
const EOSC_DISABLED = ENV.APP.eosc_portal.disabled;

const SORT_FIELDS = [
  'name',
  'eosc_id',
];

let TABLE_FIELDS = [
  'name',
  'supercategory.name',
  'eosc_id',
];

let fields_details = [
  'supercategory.name',
  'name',
  'eosc_id',
];

let fields_ce = [
  'supercategory',
  'name',
  'eosc_id',
]

if (EOSC_DISABLED) {
  fields_details.pop();
  fields_ce.pop();
  TABLE_FIELDS.pop();
}


const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'category.cards.basic',
  fields: fields_details,
  layout: {
    flex: [100,100,100],
  },
};


const BASIC_INFO_FIELDSET = {
  label: 'category.cards.basic',
  fields: fields_ce,
  layout: {
    flex: [100,100,100],
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
