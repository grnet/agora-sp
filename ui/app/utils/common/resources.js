import { field } from 'ember-gen';

const providers = field('rd_bai_3_service_providers', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['name'],
    },
  },
});

const SORT_FIELDS = [
  'rd_bai_0_id',
  'rd_bai_1_name',
];

const TABLE_FIELDS = [
  field('rd_bai_0_id', {label: 'resource.table.rd_bai_0_id'}),
  field('rd_bai_1_name', {label: 'resource.table.rd_bai_1_name'}),
  field('rd_bai_2_service_organisation.name', {label: 'resource.table.rd_bai_2_service_organisation'}),
];


const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'resource.cards.basic_information',
  fields: [
    'rd_bai_0_id',
    'rd_bai_1_name',
    field('rd_bai_2_service_organisation.name', {label: 'resource.fields.rd_bai_2_service_organisation'}),
    'providers_names',
    'rd_bai_4_webpage',
  ],
  layout: {
    flex: [50, 50, 100, 100, 100],
  },
};

const EDIT_BASIC_INFO_FIELDSET = {
  label: 'resource.cards.basic_information',
  fields: [
    field('rd_bai_0_id'),
    'rd_bai_1_name',
    'rd_bai_2_service_organisation',
    providers,
    'rd_bai_4_webpage',
  ],
  layout: {
    flex: [100, 50, 50, 100, 100],
  },
};

const CREATE_BASIC_INFO_FIELDSET = {
  label: 'resource.cards.basic_information',
  fields: [
    field('rd_bai_0_id'),
    'rd_bai_1_name',
    'rd_bai_2_service_organisation',
    providers,
    'rd_bai_4_webpage',
  ],
  layout: {
    flex: [100, 50, 50, 100, 100],
  },
};

const DETAILS_FIELDSETS = [
  DETAILS_BASIC_INFO_FIELDSET,
];

const CREATE_FIELDSETS = [
  CREATE_BASIC_INFO_FIELDSET,
];

const EDIT_FIELDSETS = [
  EDIT_BASIC_INFO_FIELDSET,
];

export {
  TABLE_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  SORT_FIELDS,
}
