import { field } from 'ember-gen';
import { fileField, fields_eosc } from '../../lib/common';

const { get, computed } = Ember;

const DETAILS_MARKETING_FIELDSET = {
  label: 'provider.cards.marketing',
  text: 'provider.cards.marketing_hint',
  fields: [
    field('epp_mri_description', {
      type: 'text',
      htmlSafe: true,
      formComponent: 'text-editor',
    }),
    'epp_mri_logo',
    'epp_mri_multimedia',
  ],
  layout: {
    flex: [100, 100, 100],
  },
};

const MARKETING_FIELDSET = {
  label: 'provider.cards.marketing',
  text: 'provider.cards.marketing_hint',
  fields: computed('role', function () {
    let role = get(this, 'role');
    let editor = role === 'provideradmin' || role === 'portfolioadmin';
    let label_1 = 'provider.fields.epp_mri_description';
    let label_2 = 'provider.fields.epp_mri_logo';
    if (editor) {
      label_1 = 'provider.fields.epp_mri_description.required';
      label_2 = 'provider.fields.epp_mri_logo.required';
    }
    return [
      field('epp_mri_description', {
        type: 'text',
        label: label_1,
        htmlSafe: true,
        formComponent: 'text-editor',
      }),
      field('epp_mri_logo', { label: label_2 }),
      'epp_mri_multimedia',
    ];
  }),
  layout: {
    flex: [100, 100, 100],
  },
};

const MATURITY_FIELDSET = {
  label: 'provider.cards.maturity',
  text: 'provider.cards.maturity_hint',
  fields: ['epp_mti_life_cycle_status', 'epp_mti_certifications'],
  layout: {
    flex: [100, 100],
  },
};

const merildomain = field('epp_oth_meril_scientific_domain', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'eosc_id']),
    },
  },
});

const merilsubdomain = field('epp_oth_meril_scientific_subdomain', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['domain.name', 'name', 'description', 'eosc_id']),
    },
  },
});

const domain = field('epp_cli_scientific_domain', {
  displayComponent: 'gen-display-field-table',
  label: computed('role', function () {
    let role = get(this, 'role');
    let editor = role === 'provideradmin' || role === 'portfolioadmin';
    if (editor) {
      return 'provider.fields.epp_cli_scientific_domain.required';
    } else {
      return 'provider.fields.epp_cli_scientific_domain';
    }
  }),
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'eosc_id']),
    },
  },
});

const subdomain = field('epp_cli_scientific_subdomain', {
  displayComponent: 'gen-display-field-table',
  label: computed('role', function () {
    let role = get(this, 'role');
    let editor = role === 'provideradmin' || role === 'portfolioadmin';
    if (editor) {
      return 'provider.fields.epp_cli_scientific_subdomain.required';
    } else {
      return 'provider.fields.epp_cli_scientific_subdomain';
    }
  }),
  modelMeta: {
    row: {
      fields: fields_eosc(['domain.name', 'name', 'eosc_id']),
    },
  },
});

const structure = field('epp_cli_structure_type', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'description', 'eosc_id']),
    },
  },
});

const affiliations = field('epp_oth_affiliations', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['name'],
    },
  },
});

const networks = field('epp_oth_networks', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['abbreviation', 'name', 'eosc_id']),
    },
  },
});

const esfridomain = field('epp_oth_esfri_domain', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'description', 'eosc_id']),
    },
  },
});

const activity = field('epp_oth_areas_of_activity', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'eosc_id']),
    },
  },
});

const challenge = field('epp_oth_societal_grand_challenges', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'eosc_id']),
    },
  },
});

const CONTACT_FIELDSET = {
  label: 'provider.cards.contact',
  fields: [
    field('main_contact', {
      displayAttr: 'displayInfo',
    }),
    field('public_contact', {
      displayAttr: 'displayInfo',
    }),
  ],
  layout: {
    flex: [100, 100],
  },
};

const DETAILS_CONTACT_MAIN_FIELDSET = {
  label: 'provider.cards.main_contact',
  fields: [
    field('main_contact.first_name', {
      label: 'provider.fields.mc_first_name',
    }),
    field('main_contact.last_name', { label: 'provider.fields.mc_last_name' }),
    field('main_contact.email', { label: 'provider.fields.mc_email' }),
    field('main_contact.phone', { label: 'provider.fields.mc_phone' }),
    field('main_contact.position', { label: 'provider.fields.mc_position' }),
  ],
  layout: {
    flex: [50, 50, 50, 50, 50],
  },
};

const DETAILS_CONTACT_PUBLIC_FIELDSET = {
  label: 'provider.cards.public_contact',
  fields: [
    field('public_contact.first_name', {
      label: 'provider.fields.pc_first_name',
    }),
    field('public_contact.last_name', {
      label: 'provider.fields.pc_last_name',
    }),
    field('public_contact.email', { label: 'provider.fields.pc_email' }),
    field('public_contact.phone', { label: 'provider.fields.pc_phone' }),
    field('public_contact.position', { label: 'provider.fields.pc_position' }),
  ],
  layout: {
    flex: [50, 50, 50, 50, 50],
  },
};

const DETAILS_CLASSIFICATION_FIELDSET = {
  label: 'provider.cards.classification',
  fields: [
    'epp_cli_scientific_domain_verbose',
    'epp_cli_scientific_subdomain_verbose',
    'epp_cli_tags',
    'epp_cli_structure_type_verbose',
  ],
  layout: {
    flex: [100, 100, 100, 100],
  },
};

const CLASSIFICATION_FIELDSET = {
  label: 'provider.cards.classification',
  fields: [domain, subdomain, 'epp_cli_tags', 'epp_cli_structure_type'],
  layout: {
    flex: [100, 100, 100, 100],
  },
};

const DETAILS_DEPENDENCIES_FIELDSET = {
  label: 'provider.cards.dependencies',
  fields: [
    'epp_oth_participating_countries',
    'epp_oth_affiliations_verbose',
    'epp_oth_networks_verbose',
  ],
  layout: {
    flex: [100, 100, 100],
  },
};

const DETAILS_OTHER_FIELDSET = {
  label: 'provider.cards.other',
  fields: [
    'epp_oth_esfri_domain_verbose',
    field('epp_oth_esfri_type.name', {
      label: 'provider.fields.epp_oth_esfri_type',
    }),
    'epp_oth_meril_scientific_domain_verbose',
    'epp_oth_meril_scientific_subdomain_verbose',
    'epp_oth_areas_of_activity_verbose',
    'epp_oth_societal_grand_challenges_verbose',
    'epp_oth_national_roadmaps',
  ],
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
  },
};

const DEPENDENCIES_FIELDSET = {
  label: 'provider.cards.dependencies',
  fields: [
    'epp_oth_participating_countries',
    affiliations,
    networks,
  ],
  layout: {
    flex: [100, 100, 100],
  },
};

const OTHER_FIELDSET = {
  label: 'provider.cards.other',
  fields: [
    structure,
    esfridomain,
    'epp_oth_esfri_type',
    merildomain,
    merilsubdomain,
    activity,
    challenge,
    'epp_oth_national_roadmaps',
  ],
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
  },
};

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'provider.cards.basic_information',
    text: 'provider.cards.basic_hint',
    layout: {
      flex: [50, 50, 100, 100, 100, 50, 50, 100, 50, 50],
    },
    fields: fields_eosc([
      'epp_bai_id',
      'state',
      'epp_bai_name',
      'epp_bai_abbreviation',
      'epp_bai_website',
      'epp_bai_legal_entity',
      'epp_bai_legal_status',
      'epp_bai_hosting_legal_entity',
      'eosc_id',
      'eosc_state',
    ]),
  },
  DETAILS_CLASSIFICATION_FIELDSET,
  {
    label: 'provider.cards.location',
    text: 'provider.cards.location_hint',
    layout: {
      flex: [100, 100, 100, 100, 100],
    },
    fields: [
      'epp_loi_street_name_and_number',
      'epp_loi_postal_code',
      'epp_loi_city',
      'epp_loi_region',
      'epp_loi_country_or_territory',
    ],
  },
  DETAILS_MARKETING_FIELDSET,
  MATURITY_FIELDSET,
  DETAILS_CONTACT_MAIN_FIELDSET,
  DETAILS_CONTACT_PUBLIC_FIELDSET,
  DETAILS_DEPENDENCIES_FIELDSET,
  DETAILS_OTHER_FIELDSET,
];

/********************************************
                EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [
  {
    label: 'provider.cards.basic_information',
    text: 'provider.cards.basic_hint',
    layout: {
      flex: [50, 50, 100, 100, 100, 50, 50, 100, 50, 50],
    },
    fields: computed('role', function () {
      let role = get(this, 'role');
      const editor = role === 'provideradmin';
      const disabled = editor;
      let abbreviation_label = 'provider.fields.epp_bai_abbreviation';
      if (editor) {
        abbreviation_label = 'provider.fields.epp_bai_abbreviation.required';
      }
      return fields_eosc([
        field('epp_bai_id', {
          label: 'provider.fields.epp_bai_id.required',
        }),
        field('state', { disabled: true }),
        field('epp_bai_name', {
          label: 'provider.fields.epp_bai_name.required',
        }),
        field('epp_bai_abbreviation', {
          label: abbreviation_label,
        }),
        'epp_bai_website',
        'epp_bai_legal_entity',
        'epp_bai_legal_status',
        'epp_bai_hosting_legal_entity',
        field('eosc_id', { disabled }),
        field('eosc_state', { disabled }),
      ]);
    }),
  },
  CLASSIFICATION_FIELDSET,
  {
    label: 'provider.cards.location',
    text: 'provider.cards.location_hint',
    layout: {
      flex: [100, 100, 100, 100, 100],
    },
    fields: computed('role', function () {
      let role = get(this, 'role');
      const editor = role === 'provideradmin' || role === 'portfolioadmin';
      let label_1 = 'provider.fields.epp_loi_street_name_and_number';
      let label_2 = 'provider.fields.epp_loi_postal_code';
      let label_3 = 'provider.fields.epp_loi_city';
      let label_5 = 'provider.fields.epp_loi_country_or_territory';
      if (editor) {
        label_1 = 'provider.fields.epp_loi_street_name_and_number.required';
        label_2 = 'provider.fields.epp_loi_postal_code.required';
        label_3 = 'provider.fields.epp_loi_city.required';
        label_5 = 'provider.fields.epp_loi_country_or_territory.required';
      }
      return [
        field('epp_loi_street_name_and_number', { label: label_1 }),
        field('epp_loi_postal_code', { label: label_2 }),
        field('epp_loi_city', { label: label_3 }),
        'epp_loi_region',
        field('epp_loi_country_or_territory', { label: label_5 }),
      ];
    }),
  },
  MARKETING_FIELDSET,
  MATURITY_FIELDSET,
  CONTACT_FIELDSET,
  DEPENDENCIES_FIELDSET,
  OTHER_FIELDSET,
];

/********************************************
                CREATE  VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'provider.cards.basic_information',
    text: 'provider.cards.basic_hint',
    layout: {
      flex: [100, 100, 100, 100, 50, 50, 100, 50, 50],
    },
    fields: computed('role', function () {
      let role = get(this, 'role');
      const editor = role === 'provideradmin' || role === 'portfolioadmin';
      const disabled = editor;
      let abbreviation_label = 'provider.fields.epp_bai_abbreviation';
      if (editor) {
        abbreviation_label = 'provider.fields.epp_bai_abbreviation.required';
      }
      return fields_eosc([
        field('epp_bai_id', {
          label: 'provider.fields.epp_bai_id.required',
        }),
        field('epp_bai_name', {
          label: 'provider.fields.epp_bai_name.required',
        }),
        field('epp_bai_abbreviation', {
          label: abbreviation_label,
        }),
        'epp_bai_website',
        'epp_bai_legal_entity',
        'epp_bai_legal_status',
        'epp_bai_hosting_legal_entity',
        'eosc_id',
        'eosc_state',
      ]);
    }),
  },
  CLASSIFICATION_FIELDSET,
  {
    label: 'provider.cards.location',
    text: 'provider.cards.location_hint',
    layout: {
      flex: [100, 100, 100, 100, 100],
    },
    fields: computed('role', function () {
      let role = get(this, 'role');
      const editor = role === 'provideradmin' || role === 'portfolioadmin';
      let label_1 = 'provider.fields.epp_loi_street_name_and_number';
      let label_2 = 'provider.fields.epp_loi_postal_code';
      let label_3 = 'provider.fields.epp_loi_city';
      let label_5 = 'provider.fields.epp_loi_country_or_territory';
      if (editor) {
        label_1 = 'provider.fields.epp_loi_street_name_and_number.required';
        label_2 = 'provider.fields.epp_loi_postal_code.required';
        label_3 = 'provider.fields.epp_loi_city.required';
        label_5 = 'provider.fields.epp_loi_country_or_territory.required';
      }
      return [
        field('epp_loi_street_name_and_number', { label: label_1 }),
        field('epp_loi_postal_code', { label: label_2 }),
        field('epp_loi_city', { label: label_3 }),
        'epp_loi_region',
        field('epp_loi_country_or_territory', { label: label_5 }),
      ];
    }),
  },
  MARKETING_FIELDSET,
  MATURITY_FIELDSET,
  CONTACT_FIELDSET,
  DEPENDENCIES_FIELDSET,
  OTHER_FIELDSET,
];

const PROVIDER_TABLE_FIELDS = fields_eosc([
  field('epp_bai_id', { label: 'provider.table.epp_bai_id' }),
  field('epp_bai_name', { label: 'provider.table.epp_bai_name' }),
  field('epp_bai_abbreviation', {
    label: 'provider.table.epp_bai_abbreviation',
  }),
  field('state_verbose', { label: 'provider.fields.state' }),
  'eosc_id',
  'eosc_state',
]);

export {
  DETAILS_FIELDSETS,
  EDIT_FIELDSETS,
  CREATE_FIELDSETS,
  PROVIDER_TABLE_FIELDS,
};
