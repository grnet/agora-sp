import { field } from 'ember-gen';
import { fileField } from '../../lib/common';

const SORT_FIELDS = [
  'name',
  'service_area_ext',
  'service_trl_ext',
  'service_type',
];

/********************************************
                LIST VIEW
********************************************/

const TABLE_FIELDS = [
  field(
    'name', {
      type: 'text',
      label: 'service_item.fields.name'
    }
  ),
  /*field(
    'logo', {
      type: 'text',
      label: 'service_item.fields.logo'
    }
  ),*/
  field(
    'service_area_ext', {
      type: 'text',
      label: 'service_item.fields.service_area'
    }
  ),
  field(
    'service_type', {
      type: 'text',
      label: 'service_item.fields.service_type'
    }
  ),
  field(
    'service_trl_ext', {
      type: 'text',
      label: 'service_trl.belongs.value'
    }
  ),
  field(
    'short_desc', {
      type: 'text',
      label: 'service_item.fields.short_description',
      htmlSafe: true,
      formComponent: 'text-editor',
    }
  ),
  field(
    'id_contact_information.full_name', {
      type: 'text',
      label: 'External Contact'
    }
  ),
  field(
    'id_contact_information_internal.full_name', {
      type: 'text',
      label: 'Internal Contact'
    }
  ),
];

/********************************************
                DETAILS VIEW
********************************************/

const BASIC_INFO_FIELDS =  [
  field(
    'name', {
      type: 'text',
      label: 'service_item.fields.name'
    }
  ),
  fileField(
    'logo', 'service', 'logo', {
      readonly: true,
      label: 'service.fields.logo',
      hint: 'service.hints.icon',
    }, {
      img: true
    }
  ),
  field(
    'service_area.name', {
      type: 'text',
      label: 'service_item.fields.service_area'
    }
  ),
  field(
    'service_type', {
      type: 'text',
      label: 'service_item.fields.service_type'
    }
  ),
  field(
    'service_trl.value', {
      type: 'text',
      label: 'service_trl.belongs.value'
    }
  ),
  field(
    'short_description', {
      type: 'text',
      label: 'service_item.fields.short_description',
      htmlSafe: true,
      formComponent: 'text-editor',
    }
  ),
  field(
    'id_contact_information.full_name', {
      type: 'text',
      label: 'Contact Information'
    }
  ),
  field(
    'id_contact_information_internal.full_name', {
      type: 'text',
      label: 'Contact Information'
    }
  ),
  'customer_facing',
  'internal',
];

const BASIC_INFO_FORM_FIELDS_EDIT =  [
  field(
    'name', {
      label: 'service_item.fields.name'
    }
  ),
  fileField(
    'logo', 'service-item', 'logo', {
      readonly: false,
      label: 'service_item.fields.icon',
      hint: 'service_item.hints.icon',
    }, {
      replace: true,
      img: true
    }
  ),
  field(
    'service_area', {
      label: 'service_item.fields.service_area'
    }
  ),
  field(
    'service_type', {
      label: 'service_item.fields.service_type'
    }
  ),
  field(
    'service_trl', {
      label: 'service_trl.belongs.value'
    }
  ),
  field(
    'short_description', {
      label: 'service_item.fields.short_description',
      htmlSafe: true,
      formComponent: 'text-editor',
    }
  ),
  field(
    'id_contact_information', {
      label: 'contact_information.belongs.external'
    }
  ),
  field(
    'id_contact_information_internal', {
      label: 'contact_information.belongs.internal'
    }
  ),
  'customer_facing',
  'internal',
];

const BASIC_INFO_FORM_FIELDS_CREATE =  [
  field(
    'name', {
      label: 'service_item.fields.name'
    }
  ),
  field(
    'service_area', {
      label: 'service_item.fields.service_area'
    }
  ),
  field(
    'service_type', {
      label: 'service_item.fields.service_type'
    }
  ),
  field(
    'service_trl', {
      label: 'service_trl.belongs.value'
    }
  ),
  field(
    'short_description', {
      label: 'service_item.fields.short_description',
      htmlSafe: true,
      formComponent: 'text-editor',
    }
  ),
  field(
    'id_contact_information', {
      label: 'contact_information.belongs.external'
    }
  ),
  field(
    'id_contact_information_internal', {
      label: 'contact_information.belongs.internal'
    }
  ),
  'customer_facing',
  'internal',
];

const DETAILS_BASIC_INFO_FIELDSET = {
  label: 'service_item.cards.basic_information',
  fields: BASIC_INFO_FIELDS,
  layout: {
    flex: [ 100, 100, 100, 100, 100, 100, 100, 100, 100, 50, 50 ]
  }
};

const CUSTOM_VERSIONS_FIELDSET = {
  label: 'service_version.belongs.cards.title',
  layout: {
    flex: [ 100, 100 ]
  },
  fields: [
    field('versions', {
      label: '',
      modelName: 'service_version',
      displayComponent: 'gen-display-field-table',
      valueQuery: (store, params, model, value) => {
        if(model.get('id')) {
          return store.query('service_version', { id_service: model.get('id') });
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
                message: 'Are you sure you want to remove this service version?',
                cancel: 'Cancel',
                ok: 'Confirm'
              },
              action(route, model) {
                model.destroyRecord();
              }
            },
            goToDetails: {
              label: 'details',
              icon: 'remove red eye',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.index`;
                route.transitionTo(dest_route, model);
              }
            },
            goToEdit: {
              label: 'edit',
              icon: 'edit',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.edit.index`;
                route.transitionTo(dest_route, model);
              }
            }
          },
          fields: [
            field(
              'version', {
                label: 'service_version.fields.version'
              }
            ),
            field(
              'status.value', {
                label: 'service_status.belongs.value'
              }
            ),
            field(
              'is_in_catalogue', {
                label: 'service_version.fields.in_catalogue'
              }
            ),
            field(
              'visible_to_marketplace', {
                label: 'service_version.fields.visible_to_marketplace'
              }
            ),
          ]
        }
      }
    }),
    field('service_version_url', {
      displayComponent: 'cta-btn',
      displayAttrs: {
        hideLabel: true,
        //classNames: ['cta-btn cta-btn--text-right']
      },
      label: 'service_item.links.create_service_version',
    }),
  ]
};

const USER_CUSTOMERS_FIELDSET = {
  label: 'User Customers',
  layout: {
    flex: [ 100, 100 ]
  },
  fields: [
    field('customers', {
      label: '',
      modelName: 'user_customer',
      displayComponent: 'gen-display-field-table',
      valueQuery: (store, params, model, value) => {
        if(model.get('id')) {
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
                ok: 'Confirm'
              },
              action(route, model) {
                model.destroyRecord();
              }
            },
            goToDetails: {
              label: 'details',
              icon: 'remove red eye',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.index`;
                route.transitionTo(dest_route, model);
              }
            },
            goToEdit: {
              label: 'edit',
              icon: 'edit',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.edit.index`;
                route.transitionTo(dest_route, model);
              }
            }
          },
          fields: [
            field(
              'name.name', {
                label: 'Name'
              }
            ),
            field(
              '__role', {
                label: 'role',
                htmlSafe: true
              }
            ),
          ]
        }
      }
    })
  ]
};

const TEXT_FIELDS = [
  field(
    'description_internal', {
      type: 'text',
      label: 'service_item.fields.description_internal',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  field(
    'description_external', {
      type: 'text',
      label: 'service_item.fields.description_external',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  field(
    'request_procedures', {
      type: 'text',
      label: 'service_item.fields.procedures',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
];

const MORE_INFO_FIELDSET = {
  label: 'service_item.cards.details',
  fields: TEXT_FIELDS,
  layout: {
    flex: [ 100, 100, 100 ]
  }
};

const BUSINESS_INFO_FIELDSET = {
  label: 'service_item.cards.business_info',
  fields: [
  field(
    'funders_for_service', {
      type: 'text',
      label: 'service_item.fields.funders',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  field(
    'value_to_customer', {
      type: 'text',
      label: 'service_item.fields.customer_value',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  field(
    'risks', {
      type: 'text',
      label: 'service_item.fields.risks',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  field(
    'competitors', {
      type: 'text',
      label: 'service_item.fields.competitors',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  ],
  layout: {
    flex: [ 100, 100, 100, 100 ]
  }
};

const DETAILS_FIELDSETS = [
  DETAILS_BASIC_INFO_FIELDSET,
  USER_CUSTOMERS_FIELDSET,
  //this creates a new referenced table inside another gen
  CUSTOM_VERSIONS_FIELDSET,
  MORE_INFO_FIELDSET,
  BUSINESS_INFO_FIELDSET
];

/********************************************
            CREATE VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'service_item.cards.basic_information',
    fields: BASIC_INFO_FORM_FIELDS_CREATE
  },
  MORE_INFO_FIELDSET,
  BUSINESS_INFO_FIELDSET
];

/********************************************
            EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [
  {
    label: 'service_item.cards.basic_information',
    fields: BASIC_INFO_FORM_FIELDS_EDIT
  },
  MORE_INFO_FIELDSET,
  BUSINESS_INFO_FIELDSET
];


export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  BASIC_INFO_FIELDS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS
};
