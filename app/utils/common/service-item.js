import { field } from 'ember-gen';
import { fileField } from '../../lib/common';

const SORT_FIELDS = [
  'name',
  'owner_name',
  'service_type',
];

const providers = field('providers', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['name'],
    },
  },
});


const service_categories = field('service_categories', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: [
        'name',
      ]
    }
  }
})

/********************************************
                LIST VIEW
********************************************/

const TABLE_FIELDS = [
  field('name', {
    label: 'service_item.fields.name',
  }),
  field('service_categories_names', {
    label: 'service_item.fields.service_categories',
  }),
  field('owner_name', {
    label: 'service_item.fields.owner_name',
  }),
  field('providers_names', {
    label: 'service_item.fields.providers_names',
  }),
];

/********************************************
                DETAILS VIEW
********************************************/

const BASIC_INFO_FIELDS = [
  field('name', {
    label: 'service_item.fields.name',
  }),
  field('url', {
    type: 'text',
    label: 'service_item.fields.url',
  }),
  field('endpoint', {
    type: 'text',
    label: 'service_item.fields.endpoint',
  }),
  'customer_facing',
  'internal',
  field('service_type', {
    label: 'service_item.fields.service_type',
  }),
  field('short_description', {
    label: 'service_item.fields.short_description',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  field('tagline', {
    label: 'service_item.fields.tagline',
  }),
  field('user_value', {
    label: 'service_item.fields.user_value',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  field('target_customers', {
    label: 'service_item.fields.target_customers',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  field('target_users', {
    label: 'service_item.fields.target_users',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),

  fileField(
    'logo',
    'service',
    'logo',
    {
      readonly: true,
      label: 'service.fields.logo',
      hint: 'service.hints.icon',
    },
    {
      img: true,
    }
  ),
  field('screenshots_videos', {
    label: 'service_item.fields.screenshots_videos',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  field('languages', {
    label: 'service_item.fields.languages',
  }),
  field('standards', {
    label: 'service_item.fields.standards',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  field('certifications', {
    label: 'service_item.fields.certifications',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),

];

const BASIC_INFO_FORM_FIELDS_EDIT = [
  field('name', {
    label: 'service_item.fields.name',
  }),
  field('url', {
    type: 'text',
    label: 'service_item.fields.url',
  }),
  field('endpoint', {
    type: 'text',
    label: 'service_item.fields.endpoint',
  }),
  'customer_facing',
  'internal',
  field('service_type', {
    label: 'service_item.fields.service_type',
  }),
  field('short_description', {
    label: 'service_item.fields.short_description',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('tagline', {
    label: 'service_item.fields.tagline',
    hint: 'service_item.hints.tagline',
  }),
  field('user_value', {
    label: 'service_item.fields.user_value',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('target_customers', {
    label: 'service_item.fields.target_customers',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('target_users', {
    label: 'service_item.fields.target_users',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  fileField(
    'logo',
    'service-item',
    'logo',
    {
      readonly: false,
      label: 'service_item.fields.logo',
      hint: 'service_item.hints.logo',
    },
    {
      replace: true,
      img: true,
    }
  ),
  field('screenshots_videos', {
    label: 'service_item.fields.screenshots_videos',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('languages', {
    label: 'service_item.fields.languages',
    hint: 'service_item.hints.languages',
  }),
  field('standards', {
    label: 'service_item.fields.standards',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('certifications', {
    label: 'service_item.fields.certifications',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
];

const BASIC_INFO_FORM_FIELDS_CREATE = [
  field('name', {
    label: 'service_item.fields.name',
  }),
  field('url', {
    type: 'text',
    label: 'service_item.fields.url',
  }),
  field('endpoint', {
    type: 'text',
    label: 'service_item.fields.endpoint',
  }),
  'customer_facing',
  'internal',
  field('service_type', {
    label: 'service_item.fields.service_type',
  }),
  field('short_description', {
    label: 'service_item.fields.short_description',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('tagline', {
    label: 'service_item.fields.tagline',
    hint: 'service_item.hints.tagline',
  }),
  field('user_value', {
    label: 'service_item.fields.user_value',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('target_customers', {
    label: 'service_item.fields.target_customers',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('target_users', {
    label: 'service_item.fields.target_users',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('screenshots_videos', {
    label: 'service_item.fields.screenshots_videos',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('languages', {
    label: 'service_item.fields.languages',
    hint: 'service_item.hints.languages',
  }),
  field('standards', {
    label: 'service_item.fields.standards',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
  field('certifications', {
    label: 'service_item.fields.certifications',
    htmlSafe: true,
    formComponent: 'text-editor',
  }),
];

const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'service_item.cards.basic_information',
  fields: BASIC_INFO_FIELDS,
  layout: {
    flex: [
      100,
      50,
      50,
      50,
      50,
      100,
      100,
      100,
      100,
      100,
      100,
      100,
      100,
      100,
      100,
      100,
    ],
  },
};

const CUSTOM_VERSIONS_FIELDSET = {
  label: 'service_version.belongs.cards.title',
  layout: {
    flex: [100, 100],
  },
  fields: [
    field('versions', {
      label: '',
      modelName: 'service_version',
      displayComponent: 'gen-display-field-table',
      valueQuery: (store, params, model, value) => {
        if (model.get('id')) {
          return store.query('service_version', {
            id_service: model.get('id'),
          });
        }
      },
      modelMeta: {
        row: {
          actions: ['goToDetails', 'goToEdit', 'remove'],
          actionsMap: {
            remove: {
              label: 'remove',
              icon: 'delete',
              confirm: true,
              warn: true,
              prompt: {
                title: 'Remove service version',
                message:
                  'Are you sure you want to remove this service version?',
                cancel: 'Cancel',
                ok: 'Confirm',
              },
              action(route, model) {
                model.destroyRecord();
              },
            },
            goToDetails: {
              label: 'details',
              icon: 'remove red eye',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.index`;
                route.transitionTo(dest_route, model);
              },
            },
            goToEdit: {
              label: 'edit',
              icon: 'edit',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.edit.index`;
                route.transitionTo(dest_route, model);
              },
            },
          },
          fields: [
            field('version', {
              label: 'service_version.fields.version',
            }),
            field('status.value', {
              label: 'service_status.belongs.value',
            }),
            field('is_in_catalogue', {
              label: 'service_version.fields.in_catalogue',
            }),
            field('visible_to_marketplace', {
              label: 'service_version.fields.visible_to_marketplace',
            }),
          ],
        },
      },
    }),
    field('service_version_url', {
      displayComponent: 'cta-btn',
      displayAttrs: {
        hideLabel: true,
        //classNames: ['cta-btn cta-btn--text-right']
      },
      label: 'service_item.links.create_service_version',
    }),
  ],
};


const USER_CUSTOMERS_FIELDSET = {
  label: 'User Customers',
  layout: {
    flex: [100, 100],
  },
  fields: [
    field('customers', {
      label: '',
      modelName: 'user_customer',
      displayComponent: 'gen-display-field-table',
      valueQuery: (store, params, model, value) => {
        if (model.get('id')) {
          return store.query('user_customer', { service_id: model.get('id') });
        }
      },
      modelMeta: {
        row: {
          actions: ['goToDetails', 'goToEdit', 'remove'],
          actionsMap: {
            remove: {
              label: 'remove',
              icon: 'delete',
              confirm: true,
              warn: true,
              prompt: {
                title: 'Remove user customer',
                message: 'Are you sure you want to remove this user customer?',
                cancel: 'Cancel',
                ok: 'Confirm',
              },
              action(route, model) {
                model.destroyRecord();
              },
            },
            goToDetails: {
              label: 'details',
              icon: 'remove red eye',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.index`;
                route.transitionTo(dest_route, model);
              },
            },
            goToEdit: {
              label: 'edit',
              icon: 'edit',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.edit.index`;
                route.transitionTo(dest_route, model);
              },
            },
          },
          fields: [
            field('name.name', {
              label: 'Name',
            }),
            field('__role', {
              label: 'role',
              htmlSafe: true,
            }),
          ],
        },
      },
    }),
  ],
};

const TEXT_FIELDS = [
  field('description_internal', {
    type: 'text',
    label: 'service_item.fields.description_internal',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  field('description_external', {
    type: 'text',
    label: 'service_item.fields.description_external',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
  field('request_procedures', {
    type: 'text',
    label: 'service_item.fields.procedures',
    formComponent: 'text-editor',
    htmlSafe: true,
  }),
];

const MORE_INFO_FIELDSET = {
  label: 'service_item.cards.details',
  fields: TEXT_FIELDS,
  layout: {
    flex: [100, 100, 100],
  },
};

const PROVIDERS_FIELDSET = {
  label: 'service_item.cards.providers',
  fields: [providers],
  layout: {
    flex: [100],
  },
};

const BUSINESS_INFO_FIELDSET = {
  label: 'service_item.cards.business_info',
  fields: [
    field('funders_for_service', {
      type: 'text',
      label: 'service_item.fields.funders',
      formComponent: 'text-editor',
      htmlSafe: true,
    }),
    field('risks', {
      type: 'text',
      label: 'service_item.fields.risks',
      formComponent: 'text-editor',
      htmlSafe: true,
    }),
    field('competitors', {
      type: 'text',
      label: 'service_item.fields.competitors',
      formComponent: 'text-editor',
      htmlSafe: true,
    }),
  ],
  layout: {
    flex: [100, 100, 100, 100],
  },
};


const MATURITY_FIELDSET = {
  label: 'service_item.cards.maturity',
  fields: [
    field('last_update', {
        label: 'service_item.fields.last_update',
        hint: 'service_item.hints.last_update',
      }
    ),
    field(
      'changelog', {
        label: 'service_item.fields.changelog',
        hint: 'service_item.hints.changelog',
        formComponent: 'text-editor',
        htmlSafe: true,
      }
    ),
  ],
  layout: {
    flex: [ 100, 100 ]
  }
};


const CLASSIFICATION_FIELDSET = {
  label: 'service_item.cards.classification',
  fields: [
    service_categories,
    field(
      'tags', {
        label: 'service_item.fields.tags',
        hint: 'service_item.hints.tags',
      }
    ),
    field(
      'scientific_fields', {
        label: 'service_item.fields.scientific_fields',
        hint: 'service_item.hints.scientific_fields',
      }
    ),
  ],
  layout: {
    flex: [ 100, 100, 100 ]
  }
};

const MANAGEMENT_FIELDSET = {
  label: 'service_item.cards.management',
  fields: [
    field(
      'owner_name', {
    type: 'text',
        label: 'service_item.fields.owner_name',
        hint: 'service_item.hints.owner_name',
      }
    ),
    field(
      'owner_contact', {
        label: 'service_item.fields.owner_contact',
        hint: 'service_item.hints.owner_contact',
      }
    ),
    field(
      'support_name', {
        label: 'service_item.fields.support_name',
        hint: 'service_item.hints.support_name',
      }
    ),
    field(
      'support_contact', {
        label: 'service_item.fields.support_contact',
        hint: 'service_item.hints.support_contact',
      }
    ),
    field(
      'security_name', {
        label: 'service_item.fields.security_name',
        hint: 'service_item.hints.security_name',
      }
    ),
    field(
      'security_contact', {
        label: 'service_item.fields.security_contact',
        hint: 'service_item.hints.security_contact',
      }
    ),
    field(
      'helpdesk', {
        label: 'service_item.fields.helpdesk',
        hint: 'service_item.hints.helpdesk',
      }
    ),
    field(
      'order', {
        label: 'service_item.fields.order',
        hint: 'service_item.hints.order',
      }
    ),
    field('order_type', {
      label: 'service_item.fields.order_type',
      formComponent: 'text-editor',
      htmlSafe: true,
    }),
  ],
  layout: {
    flex: [ 50, 50, 50, 50, 50, 50, 50, 50, 100 ]
  }
};


const DETAILS_FIELDSETS = [
  DETAILS_BASIC_INFO_FIELDSET,
  MATURITY_FIELDSET,
  CLASSIFICATION_FIELDSET,
  MANAGEMENT_FIELDSET,
  //this creates a new referenced table inside another gen
  CUSTOM_VERSIONS_FIELDSET,
  PROVIDERS_FIELDSET,
];

/********************************************
            CREATE VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'service_item.cards.basic_information',
    fields: BASIC_INFO_FORM_FIELDS_CREATE,
    layout: {
      flex: [100, 50, 50, 50, 50, 100],
    },
  },
  MATURITY_FIELDSET,
  CLASSIFICATION_FIELDSET,
  MANAGEMENT_FIELDSET,
  PROVIDERS_FIELDSET,
];

/********************************************
            EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [
  {
    label: 'service_item.cards.basic_information',
    fields: BASIC_INFO_FORM_FIELDS_EDIT,
    layout: {
      flex: [100, 50, 50, 50, 50, 100],
    },
  },
  MATURITY_FIELDSET,
  CLASSIFICATION_FIELDSET,
  MANAGEMENT_FIELDSET,
  PROVIDERS_FIELDSET,
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  BASIC_INFO_FIELDS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
};
