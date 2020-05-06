import { field } from 'ember-gen';
const {
  get,
  computed,
} = Ember;


const providers = field('rd_bai_3_service_providers', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['name'],
    },
  },
});

const targetUsers = field('rd_mri_5_target_users', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['user'],
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
  label: 'resource.cards.basic',
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

const DETAILS_MARKETING_FIELDSET = {
  label: 'resource.cards.marketing',
  fields: [
    'rd_mri_1_description',
    'rd_mri_2_tagline',
    'rd_mri_3_logo',
    'rd_mri_4_mulitimedia',
    'rd_mri_5_target_users_verbose',
    'rd_mri_6_target_customer_tags',
    'rd_mri_7_use_cases',
  ],
  layout: {
    flex: [100, 100, 50, 50, 100, 100, 100]
  },
};

const EDIT_OR_CREATE_MARKETING_FIELDSET = {
  label: 'resource.cards.marketing',
  fields: [
    'rd_mri_1_description',
    'rd_mri_2_tagline',
    'rd_mri_3_logo',
    'rd_mri_4_mulitimedia',
    targetUsers,
    'rd_mri_6_target_customer_tags',
    'rd_mri_7_use_cases',
  ],
  layout: {
    flex: [100, 100, 50, 50, 100, 100, 100]
  },
};

const EDIT_OR_CREATE_BASIC_INFO_FIELDSET = {
  label: 'resource.cards.basic',
  fields: computed('role', function() {
    const role = get(this, 'role');
    // serviceadmins cannot change resource organsation
    const disabled = role === 'serviceadmin';

    return [
      field('rd_bai_0_id'),
      'rd_bai_1_name',
      field('rd_bai_2_service_organisation', {
        disabled
      }),
      providers,
      'rd_bai_4_webpage',
    ]

  }),
  layout: {
    flex: [100, 50, 50, 100, 100],
  },
};


const GEO_FIELDSET = {
  label: 'resource.cards.geo',
  fields: [
    'rd_gla_1_geographical_availability',
    'rd_gla_2_language',
  ],
  layout: {
    flex: [100, 100],
  },
};

const CONTACT_FIELDSET = {
  label: 'resource.cards.contact',
  fields: [
    field(
      'main_contact', {
        displayAttr: 'displayInfo'
      }
    ),
    field(
      'public_contact', {
        displayAttr: 'displayInfo'
      }
    ),
  ],
  layout: {
    flex: [100, 100],
  },
};

const DETAILS_CONTACT_MAIN_FIELDSET = {
  label: 'resource.cards.main_contact',
  fields: [
    field('main_contact.first_name', {label: 'resource.fields.mc_first_name'}),
    field('main_contact.last_name', {label: 'resource.fields.mc_last_name'}),
    field('main_contact.email', {label: 'resource.fields.mc_email'}),
    field('main_contact.phone', {label: 'resource.fields.mc_phone'}),
    field('main_contact.position', {label: 'resource.fields.mc_position'}),
    field('main_contact.organisation.name', {label: 'resource.fields.mc_organisation'}),
  ],
  layout: {
    flex: [50, 50, 50, 50, 50, 50],
  },
};


const DETAILS_CONTACT_PUBLIC_FIELDSET = {
  label: 'resource.cards.public_contact',
  fields: [
    field('public_contact.first_name', {label: 'resource.fields.pc_first_name'}),
    field('public_contact.last_name', {label: 'resource.fields.pc_last_name'}),
    field('public_contact.email', {label: 'resource.fields.pc_email'}),
    field('public_contact.phone', {label: 'resource.fields.pc_phone'}),
    field('public_contact.position', {label: 'resource.fields.pc_position'}),
    field('public_contact.organisation.name', {label: 'resource.fields.pc_organisation'}),
  ],
  layout: {
    flex: [50, 50, 50, 50, 50, 50],
  },
};
const DETAILS_FIELDSETS = [
  DETAILS_BASIC_INFO_FIELDSET,
  DETAILS_MARKETING_FIELDSET,
  GEO_FIELDSET,
  DETAILS_CONTACT_MAIN_FIELDSET,
  DETAILS_CONTACT_PUBLIC_FIELDSET,
];

const CREATE_FIELDSETS = [
  EDIT_OR_CREATE_BASIC_INFO_FIELDSET,
  EDIT_OR_CREATE_MARKETING_FIELDSET,
  GEO_FIELDSET,
  CONTACT_FIELDSET,
];

const EDIT_FIELDSETS = [
  EDIT_OR_CREATE_BASIC_INFO_FIELDSET,
  EDIT_OR_CREATE_MARKETING_FIELDSET,
  GEO_FIELDSET,
  CONTACT_FIELDSET,
];

export {
  TABLE_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  SORT_FIELDS,
}
