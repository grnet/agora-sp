import { field } from 'ember-gen';
import { fileField, fields_eosc } from '../../lib/common';

const { get, computed } = Ember;

const domain = field('erp_cli_scientific_domain', {
  displayComponent: 'gen-display-field-table',
  label: 'resource.fields.erp_cli_scientific_domain.required',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'eosc_id']),
    },
  },
});

const subdomain = field('erp_cli_scientific_subdomain', {
  displayComponent: 'gen-display-field-table',
  label: 'resource.fields.erp_cli_scientific_subdomain.required',
  modelMeta: {
    row: {
      fields: fields_eosc(['domain.name', 'name', 'eosc_id']),
    },
  },
});

const category = field('erp_cli_category', {
  displayComponent: 'gen-display-field-table',
  label: 'resource.fields.erp_cli_category.required',
  modelMeta: {
    row: {
      fields: fields_eosc(['supercategory.name', 'name', 'eosc_id']),
    },
  },
});

const subcategory = field('erp_cli_subcategory', {
  displayComponent: 'gen-display-field-table',
  label: 'resource.fields.erp_cli_subcategory.required',
  modelMeta: {
    row: {
      fields: fields_eosc(['category.name', 'name', 'eosc_id']),
    },
  },
});

const providers = field('erp_bai_service_providers', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['epp_bai_name'],
    },
  },
});

const target_users = field('erp_cli_target_users', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['user', 'eosc_id']),
    },
  },
});

const access_type = field('erp_cli_access_type', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'description', 'eosc_id']),
    },
  },
});

const access_mode = field('erp_cli_access_mode', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'description', 'eosc_id']),
    },
  },
});

const funding_body = field('erp_ati_funding_body', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'eosc_id']),
    },
  },
});

const funding_program = field('erp_ati_funding_program', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: fields_eosc(['name', 'eosc_id']),
    },
  },
});

const required_resources = field('required_resources', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: [
        'erp_bai_id',
        'erp_bai_name',
        field('erp_bai_service_organisation.epp_bai_name', {
          label: 'resource.fields.erp_bai_service_organisation',
        }),
      ],
    },
  },
});

const related_resources = field('related_resources', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: [
        'erp_bai_id',
        'erp_bai_name',
        field('erp_bai_service_organisation.epp_bai_name', {
          label: 'resource.fields.erp_bai_service_organisation',
        }),
      ],
    },
  },
});

const contact = function (field_name) {
  return field(field_name, {
    type: 'model',
    displayAttr: 'displayInfo',
    query: Ember.computed(
      'model.changeset.erp_bai_service_organisation',
      'model.erp_bai_service_organisation',
      function () {
        let org_id_changed = get(
          this,
          'model.changeset.erp_bai_service_organisation.id'
        );
        let org_id = get(this, 'model.erp_bai_service_organisation.id');
        let organisation = org_id_changed || org_id;
        return function (select, store, field, params) {
          params = params || {};
          params.organisation = organisation;
          return store.query('contact-information', params);
        };
      }
    ),
  });
};

const SORT_FIELDS = ['erp_bai_id', 'erp_bai_name', 'eosc_id'];

const TABLE_FIELDS = fields_eosc([
  field('erp_bai_id', { label: 'resource.table.erp_bai_id' }),
  field('erp_bai_name', { label: 'resource.table.erp_bai_name' }),
  field('erp_bai_abbreviation', {
    label: 'resource.fields.erp_bai_abbreviation.required',
  }),
  field('erp_bai_service_organisation.epp_bai_name', {
    label: 'resource.table.erp_bai_service_organisation',
  }),
  field('erp_mti_technology_readiness_level.name', {
    label: 'resource.table.erp_mti_technology_readiness_level',
  }),
  field('state_verbose', { label: 'resource.table.state_verbose' }),
  'eosc_id',
  'eosc_state',
]);

const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'resource.cards.basic',
  fields: fields_eosc([
    'erp_bai_id',
    'state',
    'erp_bai_name',
    'erp_bai_abbreviation',
    field('erp_bai_service_organisation.epp_bai_name', {
      label: 'resource.fields.erp_bai_service_organisation',
    }),
    'erp_bai_providers_verbose',
    'erp_bai_webpage',
    'eosc_id',
    'eosc_state'
  ]),
  layout: {
    flex: [50, 50, 50, 50, 50, 100, 100, 50, 50],
  },
};

const DETAILS_CLASSIFICATION_FIELDSET = {
  label: 'provider.cards.classification',
  fields: [
    'erp_cli_scientific_domain_verbose',
    'erp_cli_scientific_subdomain_verbose',
    'erp_cli_category_verbose',
    'erp_cli_subcategory_verbose',
    target_users,
    access_type,
    access_mode,
    'erp_cli_tags',
  ],
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 100, 100],
  },
};

const CLASSIFICATION_FIELDSET = {
  label: 'provider.cards.classification',
  fields: [
    domain,
    subdomain,
    category,
    subcategory,
    target_users,
    access_type,
    access_mode,
    'erp_cli_tags',
  ],
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 100, 100],
  },
};

const MANAGEMENT_INFORMATION_FIELDSET = {
  label: 'resource.cards.management_information',
  fields: [
    'erp_mgi_helpdesk_webpage',
    'erp_mgi_user_manual',
    'erp_mgi_terms_of_use',
    'erp_mgi_privacy_policy',
    'erp_mgi_access_policy',
    'erp_mgi_sla_specification',
    'erp_mgi_training_information',
    'erp_mgi_status_monitoring',
    'erp_mgi_maintenance',
  ],
  layout: {
    flex: [50, 50, 50, 50, 50, 50, 50, 50, 100],
  },
};

const DETAILS_MARKETING_FIELDSET = {
  label: 'resource.cards.marketing',
  fields: [
    'erp_mri_description',
    'erp_mri_tagline',
    'erp_mri_logo',
    'erp_mri_multimedia',
    'erp_mri_use_cases',
  ],
  layout: {
    flex: [100, 100, 100, 100, 100],
  },
};

const EDIT_OR_CREATE_MARKETING_FIELDSET = {
  label: 'resource.cards.marketing',
  fields: [
    'erp_mri_description',
    'erp_mri_tagline',
    'erp_mri_logo',
    'erp_mri_multimedia',
    'erp_mri_use_cases',
  ],
  layout: {
    flex: [100, 100, 100, 100, 100],
  },
};

const EDIT_BASIC_INFO_FIELDSET = {
  label: 'resource.cards.basic',
  fields: computed('role', function () {
    const role = get(this, 'role');
    // serviceadmins cannot change resource organsation
    const disabled = role === 'serviceadmin' || role === 'provideradmin';

    return fields_eosc([
      field('erp_bai_id', { label: 'resource.fields.erp_bai_id.required' }),
      field('state', {
        disabled: true,
      }),
      field('erp_bai_name', {
        label: 'resource.fields.erp_bai_name.required',
      }),
      field('erp_bai_abbreviation', {
        label: 'resource.fields.erp_bai_abbreviation.required',
      }),
      field('erp_bai_service_organisation', {
        disabled,
        label: 'resource.fields.erp_bai_service_organisation.required',
      }),
      providers,
      'erp_bai_webpage',
      field('eosc_id', { disabled }),
      field('eosc_state', { disabled }),
    ]);
  }),
  layout: {
    flex: [50, 50, 50, 50, 100, 100, 100, 50, 50],
  },
};

const CREATE_BASIC_INFO_FIELDSET = {
  label: 'resource.cards.basic',
  fields: computed('role', function () {
    const role = get(this, 'role');
    // serviceadmins/provideradmins cannot change resource organsation
    const disabled = role === 'serviceadmin' || role === 'provideradmin';

    return fields_eosc([
      field('erp_bai_id', { label: 'resource.fields.erp_bai_id.required' }),
      field('erp_bai_name', {
        label: 'resource.fields.erp_bai_name.required',
      }),
      field('erp_bai_abbreviation', {
        label: 'resource.fields.erp_bai_abbreviation.required',
      }),
      field('erp_bai_service_organisation', {
        disabled,
        label: 'resource.fields.erp_bai_service_organisation.required',
      }),
      providers,
      'erp_bai_webpage',
      field('eosc_id', { disabled }),
      field('eosc_state', { disabled }),
    ]);
  }),
  layout: {
    flex: [50, 50, 50, 50, 100, 100, 50, 50],
  },
};
const GEO_FIELDSET = {
  label: 'resource.cards.geo',
  fields: ['erp_gla_geographical_availability', 'erp_gla_language'],
  layout: {
    flex: [100, 100],
  },
};

const LOCATION_FIELDSET = {
  label: 'resource.cards.location',
  fields: ['erp_rli_geographic_location'],
};

const CONTACT_FIELDSET = {
  label: 'resource.cards.contact',
  fields: [
    contact('main_contact'),
    contact('public_contact'),
    'erp_coi_helpdesk_email',
    'erp_coi_security_contact_email',
  ],
  layout: {
    flex: [100, 100, 50, 50],
  },
};

const DETAILS_CONTACT_MAIN_FIELDSET = {
  label: 'resource.cards.main_contact',
  fields: [
    field('main_contact.first_name', {
      label: 'resource.fields.mc_first_name',
    }),
    field('main_contact.last_name', { label: 'resource.fields.mc_last_name' }),
    field('main_contact.email', { label: 'resource.fields.mc_email' }),
    field('main_contact.phone', { label: 'resource.fields.mc_phone' }),
    field('main_contact.position', { label: 'resource.fields.mc_position' }),
    field('main_contact.organisation.epp_bai_name', {
      label: 'resource.fields.mc_organisation',
    }),
  ],
  layout: {
    flex: [50, 50, 50, 50, 50, 50],
  },
};

const DETAILS_CONTACT_PUBLIC_FIELDSET = {
  label: 'resource.cards.public_contact',
  fields: [
    field('public_contact.first_name', {
      label: 'resource.fields.pc_first_name',
    }),
    field('public_contact.last_name', {
      label: 'resource.fields.pc_last_name',
    }),
    field('public_contact.email', { label: 'resource.fields.pc_email' }),
    field('public_contact.phone', { label: 'resource.fields.pc_phone' }),
    field('public_contact.position', { label: 'resource.fields.pc_position' }),
    field('public_contact.organisation.epp_bai_name', {
      label: 'resource.fields.pc_organisation',
    }),
  ],
  layout: {
    flex: [50, 50, 50, 50, 50, 50],
  },
};

const DETAILS_CONTACT_OTHER_FIELDSET = {
  label: 'resource.cards.other_contact',
  fields: ['erp_coi_helpdesk_email', 'erp_coi_security_contact_email'],
  layout: {
    flex: [50, 50],
  },
};

const ACCESS_ORDER_FIELDSET = {
  label: 'resource.cards.access_order',
  fields: ['erp_aoi_order_type', 'erp_aoi_order'],
  layout: {
    flex: [50, 50],
  },
};
const FINANCIAL_FIELDSET = {
  label: 'resource.cards.financial',
  fields: ['erp_fni_payment_model', 'erp_fni_pricing'],
  layout: {
    flex: [50, 50],
  },
};

const MATURITY_FIELDSET = {
  label: 'resource.cards.maturity',
  fields: [
    'erp_mti_technology_readiness_level',
    'erp_mti_life_cycle_status',
    'erp_mti_certifications',
    'erp_mti_standards',
    'erp_mti_open_source_technologies',
    'erp_mti_version',
    'erp_mti_last_update',
    'erp_mti_changelog',
  ],
  layout: {
    flex: [50, 50, 100, 100, 100, 50, 50, 100],
  },
};
const DEPENDENCIES_FIELDSET = {
  label: 'resource.cards.dependencies',
  fields: [
    required_resources,
    related_resources,
    'erp_dei_related_platforms',
  ],
  layout: {
    flex: [100, 100, 100],
  },
};

const ATTRIBUTION_FIELDSET = {
  label: 'resource.cards.attribution',
  fields: [funding_body, funding_program, 'erp_ati_grant_project_name'],
  layout: {
    flex: [100, 100, 100],
  },
};

const DETAILS_FIELDSETS = [
  DETAILS_BASIC_INFO_FIELDSET,
  DETAILS_MARKETING_FIELDSET,
  DETAILS_CLASSIFICATION_FIELDSET,
  MANAGEMENT_INFORMATION_FIELDSET,
  GEO_FIELDSET,
  LOCATION_FIELDSET,
  DETAILS_CONTACT_MAIN_FIELDSET,
  DETAILS_CONTACT_PUBLIC_FIELDSET,
  DETAILS_CONTACT_OTHER_FIELDSET,
  MATURITY_FIELDSET,
  DEPENDENCIES_FIELDSET,
  ATTRIBUTION_FIELDSET,
  ACCESS_ORDER_FIELDSET,
  FINANCIAL_FIELDSET,
];

const CREATE_FIELDSETS = [
  CREATE_BASIC_INFO_FIELDSET,
  EDIT_OR_CREATE_MARKETING_FIELDSET,
  CLASSIFICATION_FIELDSET,
  MANAGEMENT_INFORMATION_FIELDSET,
  GEO_FIELDSET,
  LOCATION_FIELDSET,
  CONTACT_FIELDSET,
  MATURITY_FIELDSET,
  DEPENDENCIES_FIELDSET,
  ATTRIBUTION_FIELDSET,
  ACCESS_ORDER_FIELDSET,
  FINANCIAL_FIELDSET,
];

const EDIT_FIELDSETS = [
  EDIT_BASIC_INFO_FIELDSET,
  EDIT_OR_CREATE_MARKETING_FIELDSET,
  CLASSIFICATION_FIELDSET,
  MANAGEMENT_INFORMATION_FIELDSET,
  GEO_FIELDSET,
  LOCATION_FIELDSET,
  CONTACT_FIELDSET,
  MATURITY_FIELDSET,
  DEPENDENCIES_FIELDSET,
  ATTRIBUTION_FIELDSET,
  ACCESS_ORDER_FIELDSET,
  FINANCIAL_FIELDSET,
];

export {
  TABLE_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  SORT_FIELDS,
};
