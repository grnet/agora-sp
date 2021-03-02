import { field } from 'ember-gen';
import ENV from '../../config/environment';
const EOSC_DISABLED = !ENV.APP.eosc_portal.enabled;

const SORT_FIELDS = [
  'name',
  'eosc_id',
];

let TABLE_FIELDS = [
  field('domain.name', {label: 'merilsubdomain.table.domain'}),
  field('name', {label: 'merilsubdomain.table.name'}),
  'eosc_id',
];

if (EOSC_DISABLED) {
  TABLE_FIELDS.pop();
}

let fields_details = [
  'domain.name',
  'name',
  'description',
  'eosc_id',
];

let fields_ce = [
  'domain',
  'name',
  'description',
  'eosc_id',
]


if (EOSC_DISABLED) {
  fields_details.pop();
  fields_ce.pop();
}



const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'subdomain.cards.basic',
  fields: fields_details,
  layout: {
    flex: [100,100,100, 100],
  },
};


const BASIC_INFO_FIELDSET = {
  label: 'subdomain.cards.basic',
  fields: fields_ce,
  layout: {
    flex: [100,100,100, 100],
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
