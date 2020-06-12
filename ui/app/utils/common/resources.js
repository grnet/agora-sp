import { field } from 'ember-gen';
const {
  get,
  computed,
} = Ember;

const domain = field('erp_cli_1_scientific_domain', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['name'],
    },
  },
});

const subdomain = field('erp_cli_2_scientific_subdomain', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['domain.name','name'],
    },
  },
});

const category = field('erp_cli_3_category', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['supercategory.name', 'name'],
    },
  },
});

const subcategory = field('erp_cli_4_subcategory', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['category.name', 'name'],
    },
  },
});

const providers = field('erp_bai_3_service_providers', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['epp_bai_1_name'],
    },
  },
});

const targetUsers = field('erp_cli_5_target_users', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['user'],
    },
  },

});

const required_resources = field('required_resources', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: [
        'erp_bai_0_id',
        'erp_bai_1_name',
        field('erp_bai_2_service_organisation.epp_bai_1_name', {
          label: 'resource.fields.erp_bai_2_service_organisation',
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
        'erp_bai_0_id',
        'erp_bai_1_name',
        field('erp_bai_2_service_organisation.epp_bai_1_name', {
          label: 'resource.fields.erp_bai_2_service_organisation',
        }),
      ],
    },
  },
});

const SORT_FIELDS = [
  'erp_bai_0_id',
  'erp_bai_1_name',
];

const TABLE_FIELDS = [
  field('erp_bai_0_id', {label: 'resource.table.erp_bai_0_id'}),
  field('erp_bai_1_name', {label: 'resource.table.erp_bai_1_name'}),
  field('erp_bai_2_service_organisation.epp_bai_1_name', {label: 'resource.table.erp_bai_2_service_organisation'}),
];


const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'resource.cards.basic',
  fields: [
    'erp_bai_0_id',
    'erp_bai_1_name',
    field('erp_bai_2_service_organisation.epp_bai_1_name', {label: 'resource.fields.erp_bai_2_service_organisation'}),
    'providers_names',
    'erp_bai_4_webpage',
  ],
  layout: {
    flex: [50, 50, 100, 100, 100],
  },
};

const DETAILS_CLASSIFICATION_FIELDSET = {
  label: 'provider.cards.classification',
  fields: [
    'domain_names',
    'subdomain_names',
    'category_names',
    'subcategory_names',
    'erp_cli_5_target_users',
    'erp_cli_6_access_type',
    'erp_cli_7_access_mode',
    'erp_cli_8_tags',
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
    'erp_cli_6_access_type',
    'erp_cli_7_access_mode',
    'erp_cli_5_target_users',
    'erp_cli_8_tags',
  ],
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 100, 100],
  },
};

const MANAGEMENT_INFORMATION_FIELDSET = {
  label: 'resource.cards.management_information',
  fields: [
    'erp_mgi_1_helpdesk_webpage',
    'erp_mgi_2_user_manual',
    'erp_mgi_3_terms_of_use',
    'erp_mgi_4_privacy_policy',
    'erp_mgi_5_access_policy',
    'erp_mgi_6_sla_specification',
    'erp_mgi_7_training_information',
    'erp_mgi_8_status_monitoring',
    'erp_mgi_9_maintenance',
  ],
  layout: {
    flex: [50, 50, 50, 50, 50, 50, 50, 50, 100]
  },
};

const DETAILS_MARKETING_FIELDSET = {
  label: 'resource.cards.marketing',
  fields: [
    'erp_mri_1_description',
    'erp_mri_2_tagline',
    'erp_mri_3_logo',
    'erp_mri_4_mulitimedia',
    'erp_mri_5_use_cases',
  ],
  layout: {
    flex: [100, 100, 100, 100, 100]
  },
};

const EDIT_OR_CREATE_MARKETING_FIELDSET = {
  label: 'resource.cards.marketing',
  fields: [
    'erp_mri_1_description',
    'erp_mri_2_tagline',
    'erp_mri_3_logo',
    'erp_mri_4_mulitimedia',
    'erp_mri_5_use_cases',
  ],
  layout: {
    flex: [100, 100, 100, 100, 100]
  },
};

const EDIT_OR_CREATE_BASIC_INFO_FIELDSET = {
  label: 'resource.cards.basic',
  fields: computed('role', function() {
    const role = get(this, 'role');
    // serviceadmins cannot change resource organsation
    const disabled = role === 'serviceadmin';

    return [
      field('erp_bai_0_id'),
      'erp_bai_1_name',
      field('erp_bai_2_service_organisation', {
        disabled
      }),
      providers,
      'erp_bai_4_webpage',
    ]

  }),
  layout: {
    flex: [100, 50, 50, 100, 100],
  },
};


const GEO_FIELDSET = {
  label: 'resource.cards.geo',
  fields: [
    'erp_gla_1_geographical_availability',
    'erp_gla_2_language',
  ],
  layout: {
    flex: [100, 100],
  },
};

const LOCATION_FIELDSET = {
  label: 'resource.cards.location',
  fields: [
    'erp_rli_1_geographic_location',
  ],
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
    'erp_coi_13_helpdesk_email',
    'erp_coi_14_security_contact_email',
  ],
  layout: {
    flex: [100, 100, 50, 50],
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
    field('main_contact.organisation.epp_bai_1_name', {label: 'resource.fields.mc_organisation'}),
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
    field('public_contact.organisation.epp_bai_1_name', {label: 'resource.fields.pc_organisation'}),
  ],
  layout: {
    flex: [50, 50, 50, 50, 50, 50],
  },
};


const DETAILS_CONTACT_OTHER_FIELDSET = {
  label: 'resource.cards.other_contact',
  fields: [
    'erp_coi_13_helpdesk_email',
    'erp_coi_14_security_contact_email',
  ],
  layout: {
    flex: [50, 50],
  },
};

const ACCESS_ORDER_FIELDSET = {
  label: 'resource.cards.access_order',
  fields: [
    'erp_aoi_1_order_type',
    'erp_aoi_2_order',
  ],
  layout: {
    flex: [50, 50],
  },
};
const FINANCIAL_FIELDSET = {
  label: 'resource.cards.financial',
  fields: [
    'erp_fni_1_payment_model',
    'erp_fni_2_pricing',
  ],
  layout: {
    flex: [50, 50],
  },
};

const DEPENDENCIES_FIELDSET = {
  label: 'resource.cards.dependencies',
  fields: [
    required_resources,
    related_resources,
    'erp_dei_3_related_platforms',
  ],
  layout: {
    flex: [ 100, 100, 100 ]
  }
};

const ATTRIBUTION_FIELDSET = {
  label: 'resource.cards.attribution',
  fields: [
    'erp_ati_1_funding_body',
    'erp_ati_2_funding_program',
    'erp_ati_3_grant_project_name',
  ],
  layout: {
    flex: [ 100, 100, 100 ]
  }
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
  DEPENDENCIES_FIELDSET,
  ATTRIBUTION_FIELDSET,
  ACCESS_ORDER_FIELDSET,
  FINANCIAL_FIELDSET,
];

const CREATE_FIELDSETS = [
  EDIT_OR_CREATE_BASIC_INFO_FIELDSET,
  EDIT_OR_CREATE_MARKETING_FIELDSET,
  CLASSIFICATION_FIELDSET,
  MANAGEMENT_INFORMATION_FIELDSET,
  GEO_FIELDSET,
  LOCATION_FIELDSET,
  CONTACT_FIELDSET,
  DEPENDENCIES_FIELDSET,
  ATTRIBUTION_FIELDSET,
  ACCESS_ORDER_FIELDSET,
  FINANCIAL_FIELDSET,
];

const EDIT_FIELDSETS = [
  EDIT_OR_CREATE_BASIC_INFO_FIELDSET,
  EDIT_OR_CREATE_MARKETING_FIELDSET,
  CLASSIFICATION_FIELDSET,
  MANAGEMENT_INFORMATION_FIELDSET,
  GEO_FIELDSET,
  LOCATION_FIELDSET,
  CONTACT_FIELDSET,
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
}
