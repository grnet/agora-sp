import { field } from 'ember-gen';
import { TABLE_FILTERS } from './component-implementation-detail-link';

const SORT_FIELDS = [
  'status.value',
  'id_service.name',
  'version'
];

const TABLE_FIELDS = [
  field('version', {
    type: 'text',
    label: 'service_version.fields.version'
  }),
  field('status.value', {
    type: 'text',
    label: 'service_status.belongs.value'
  }),
  field('is_in_catalogue', {
    type: 'text',
    label: 'service_version.fields.in_catalogue'
  }),
  field('id_service.name', {
    type: 'text',
    label: 'service_item.belongs.name'
  })
];

const FINANCIAL_FIELDSET = {
  label: 'service_version.cards.more_information',
  layout: {
    flex: [50, 50]
  },
  fields: [
    field(
      'cost_to_run', {
        label: 'service_version.fields.cost_to_run',
        type: 'text',
      }
    ),
    field(
      'cost_to_build', {
        label: 'service_version.fields.cost_to_build',
        type: 'text',
      }
    ),
  ]
};

const URLS_FIELDSET = {
  label: 'service_version.cards.resources',
  layout: {
    flex: [50, 50, 50, 50, 50, 50, 50, 50, 50]
  },
  fields: [
    field(
      'usage_policy_url', {
        type: 'text',
        label: 'service_version.fields.usage_policy'
      }
    ),
    field(
      'privacy_policy_url', {
        type: 'text',
        label: 'service_version.fields.privacy_policy'
      }
    ),
    field(
      'user_documentation_url', {
        type: 'text',
        label: 'service_version.fields.user_documentation'
      }
    ),
    field(
      'operations_documentation_url', {
        type: 'text',
        label: 'service_version.fields.operations_documentation'
      }
    ),
    field(
      'monitoring_url', {
        type: 'text',
        label: 'service_version.fields.monitoring'
      }
    ),
    field(
      'accounting_url', {
        type: 'text',
        label: 'service_version.fields.accounting'
      }
    ),
    field(
      'business_continuity_plan_url', {
        type: 'text',
        label: 'service_version.fields.business_continuity'
      }
    ),
    field(
      'disaster_recovery_plan_url', {
        type: 'text',
        label: 'service_version.fields.disaster_recovery_plan'
      }
    ),
    field(
      'decommissioning_procedure_url', {
        type: 'text',
        label: 'service_version.fields.decommissioning_procedure'
      }
    ),
  ]
};

const BASIC_INFO_FIELDSET = {
  label: 'service_version.cards.basic_information',
  layout: {
    flex: [50, 50, 50, 50, 100, 100, 100],
  },
  fields: [
    field(
      'version', {
        label: 'service_version.fields.version',
        type: 'text'
      }
    ),
    field(
      'id_service.name', {
        label: 'service_item.belongs.name',
      }
    ),
    field(
      'status.value', {
        label: 'service_status.belongs.value',
      }
    ),
    field(
      'is_in_catalogue', {
        label: 'service_version.fields.in_catalogue',
      }
    ),
  field(
    'features_current', {
      label: 'service_version.fields.features_current',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  field(
    'features_future', {
      label: 'service_version.fields.features_future',
      type: 'text',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  field(
    'use_cases', {
      label: 'service_version.fields.use_cases',
      type: 'text',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  ]
};

const COMPONENT_LINKS_FIELDSET = {
  label: 'cidl.belongs.cards.title',
  layout: {
    flex: [ 100, 100 ]
  },
  fields: [
    field('cidl', {
      label: '',
      modelName: 'component_implementation_detail_link',
      displayComponent: 'gen-display-field-table',
      valueQuery: (store, params, model, value) => {
        if(model.get('id')) {
          return store.query('component_implementation_detail_link', { service_details_id: model.get('id') });
        }
      },
      modelMeta: {
        /*filter: {
          active: true,
          serverSide: true,
          search: false,
          meta: {
            fields: TABLE_FILTERS
          }
        },*/
        row: {
          actions: ['goToEdit', 'remove'],
          actionsMap: {
            remove: {
              label: 'remove',
              icon: 'delete',
              confirm: true,
              warn: true,
              prompt: {
                title: 'Remove service version component',
                message: 'Are you sure you want to remove this service version component?',
                cancel: 'Cancel',
                ok: 'Confirm'
              },
              action(route, model) {
                model.destroyRecord();
                //model.save();
              }
            },
            /*goToDetails: {
              label: 'details',
              icon: 'remove red eye',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.index`;
                route.transitionTo(dest_route, model);
              }
            },*/
            goToEdit: {
              label: 'edit',
              icon: 'edit',
              action(route, model) {
                let resource = model.get('_internalModel.modelName'),
                  dest_route = `${resource}.record.edit.index`,
                  queryParams = {
                    service_version: route.currentModel.id
                  };
                route.transitionTo(dest_route, model, { queryParams });
              }
            }
          },
          fields: [
            field('service_component_implementation_detail_id.component_id.name', {
              type: 'text',
              label: 'component.belongs.name'
            }),
            field('service_component_implementation_detail_id.component_implementation_id.name', {
              type: 'text',
              label: 'component_implementation.belongs.name'
            }),
            field('service_component_implementation_detail_id.version', {
              type: 'text',
              label: 'component_implementation_detail.belongs.name'
            }),
            field('configuration_parameters', {
              type: 'text',
              label: 'cidl.fields.configuration_parameters'
            }),
          ]
        }
      }
    }),
    field('cidl_url', {
      displayComponent: 'cta-btn',
      displayAttrs: {
        hideLabel: true,
        //classNames: ['cta-btn cta-btn--text-right']
      },
      label: 'cidl.links.create_cidl',
    }),
  ]
};

const DETAILS_FIELDSETS = [
  BASIC_INFO_FIELDSET,
  COMPONENT_LINKS_FIELDSET,
  URLS_FIELDSET,
  FINANCIAL_FIELDSET
];


const BASIC_INFO_CREATE_FIELDSET = {
  label: 'service_version.cards.basic_information',
  layout: {
    flex: [50, 50, 50, 50, 100, 100, 100],
  },
  fields: [
    field(
      'version', {
        label: 'service_version.fields.version',
        type: 'text'
      }
    ),
    field(
      'id_service', {
        label: 'service_item.belongs.name',
      }
    ),
    field(
      'status', {
        label: 'service_status.belongs.value',
      }
    ),
    field(
      'is_in_catalogue', {
        label: 'service_version.fields.in_catalogue',
      }
    ),
  field(
    'features_current', {
      label: 'service_version.fields.features_current',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  field(
    'features_future', {
      label: 'service_version.fields.features_future',
      type: 'text',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  field(
    'use_cases', {
      label: 'service_version.fields.use_cases',
      type: 'text',
      formComponent: 'text-editor',
      htmlSafe: true
    }
  ),
  ]
};

const CREATE_FIELDSETS = [
  BASIC_INFO_CREATE_FIELDSET,
  URLS_FIELDSET,
  FINANCIAL_FIELDSET,
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS
};
