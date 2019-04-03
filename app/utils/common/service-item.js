import { field } from 'ember-gen';
import { fileField } from '../../lib/common';

const SORT_FIELDS = [
  'name',
  'service_category_ext',
  'service_trl_ext',
  'service_type',
];

const organisations = field('organisations', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: ['name'],
    },
  },
});

/********************************************
                LIST VIEW
********************************************/

const TABLE_FIELDS = [
  field('name', {
    type: 'text',
    label: 'service_item.fields.name',
  }),
  field('service_category_ext', {
    type: 'text',
    label: 'service_item.fields.service_category',
  }),
  field('service_type', {
    type: 'text',
    label: 'service_item.fields.service_type',
  }),
  field('service_trl_ext', {
    type: 'text',
    label: 'service_trl.belongs.value',
  }),
  field('organisations_names', {
    type: 'text',
    label: 'service_item.fields.organisations_names',
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
      50,
      50,
      50,
      25,
      25,
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

const EXTERNAL_CONTACT_FIELDSET = {
  label: 'service_item.cards.contact_external',
  layout: {
    flex: [50, 50, 50, 50, 100],
  },
  fields: [
    'contact_external_first_name',
    'contact_external_last_name',
    'contact_external_email',
    'contact_external_phone',
    'contact_external_url',
  ],
};

const INTERNAL_CONTACT_FIELDSET = {
  label: 'service_item.cards.contact_internal',
  layout: {
    flex: [50, 50, 50, 50, 100],
  },
  fields: [
    'contact_internal_first_name',
    'contact_internal_last_name',
    'contact_internal_email',
    'contact_internal_phone',
    'contact_internal_url',
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

const ORGANISATIONS_FIELDSET = {
  label: 'service_item.cards.organisations',
  fields: [organisations],
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

const DETAILS_FIELDSETS = [
  DETAILS_BASIC_INFO_FIELDSET,
  USER_CUSTOMERS_FIELDSET,
  //this creates a new referenced table inside another gen
  CUSTOM_VERSIONS_FIELDSET,
  MORE_INFO_FIELDSET,
  BUSINESS_INFO_FIELDSET,
  ORGANISATIONS_FIELDSET,
  EXTERNAL_CONTACT_FIELDSET,
  INTERNAL_CONTACT_FIELDSET,
];

/********************************************
            CREATE VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'service_item.cards.basic_information',
    fields: BASIC_INFO_FORM_FIELDS_CREATE,
    layout: {
      flex: [100, 50, 50, 100],
    },
  },
  MORE_INFO_FIELDSET,
  BUSINESS_INFO_FIELDSET,
  ORGANISATIONS_FIELDSET,
  EXTERNAL_CONTACT_FIELDSET,
  INTERNAL_CONTACT_FIELDSET,
];

/********************************************
            EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [
  {
    label: 'service_item.cards.basic_information',
    fields: BASIC_INFO_FORM_FIELDS_EDIT,
    layout: {
      flex: [100, 50, 50, 100],
    },
  },
  MORE_INFO_FIELDSET,
  BUSINESS_INFO_FIELDSET,
  ORGANISATIONS_FIELDSET,
  EXTERNAL_CONTACT_FIELDSET,
  INTERNAL_CONTACT_FIELDSET,
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  BASIC_INFO_FIELDS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
};
