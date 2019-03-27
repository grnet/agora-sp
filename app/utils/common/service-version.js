import { field } from 'ember-gen';
import { TABLE_FILTERS } from './component-implementation-detail-link';

const {
  get,
  computed,
} = Ember;

const access_policies = field('access_policies', {
  displayComponent: 'gen-display-field-table',
  modelMeta: {
    row: {
      fields: [
        'name',
        'geo_availability',
        'access_policy_url',
      ]
    }
  }
})


const SORT_FIELDS = [
  'is_in_catalogue',
  'visible_to_marketplace',
  'version',
  'status_ext',
];

const TABLE_FIELDS = [
  field('version', {
    type: 'text',
    label: 'service_version.fields.version'
  }),
  field('status_ext', {
    type: 'text',
    label: 'service_status.belongs.value'
  }),
  field('is_in_catalogue', {
    type: 'text',
    label: 'service_version.fields.in_catalogue'
  }),
  field('visible_to_marketplace', {
    type: 'text',
    label: 'service_version.fields.visible_to_marketplace'
  }),
  field('id_service_ext', {
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
    flex: [50, 50, 50, 50, 50, 50, 50]
  },
  fields: [
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
    flex: [50, 50, 50, 25, 25, 100, 100, 100],
  },
  fields: [
    field(
      'version', {
        label: 'service_version.fields.version',
        type: 'text'
      }
    ),
    field(
      'id_service_ext', {
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
      'visible_to_marketplace', {
        label: 'service_version.fields.visible_to_marketplace',
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
  fields: computed( 'role', 'user.id', 'model.service_admins_ids', function() {
    let role = get(this, 'role');
    let is_serviceadmin = role === 'serviceadmin';
    let admins_ids = get(this, 'model.service_admins_ids');
    let user_id = get(this, 'user.id').toString();

    // Component creation button is visible if the user is admin/superadmin
    // or is serviceadmin and owns the service of the service version
    let show_button = false;
    if (role === 'admin' || role === 'superadmin') {
      show_button = true;
    }
    if (admins_ids.split(',').includes(user_id) && is_serviceadmin) {
      show_button = true;
    }


      let cidl = field('cidl', {
        label: '',
        modelName: 'component_implementation_detail_link',
        displayComponent: 'gen-display-field-table',
        valueQuery: (store, params, model, value) => {
          if(model.get('id')) {
            return store.query('component_implementation_detail_link', { service_details_id: model.get('id') });
          }
        },
        modelMeta: {
          row: {
            actions: ['goToEdit', 'remove'],
            actionsMap: {
              remove: {
                label: 'remove',
                icon: 'delete',
                confirm: true,
                warn: true,
                hidden: computed('role', function() {
                  return get(this, 'role') !== 'superadmin';
                }),
                prompt: {
                  title: 'Remove service version component',
                  message: 'Are you sure you want to remove this service version component?',
                  cancel: 'Cancel',
                  ok: 'Confirm'
                },
                action(route, model) {
                  model.destroyRecord();
                }
              },
              goToEdit: {
                label: 'edit',
                icon: 'edit',
                hidden: computed('role', function() {
                  return get(this, 'role') !== 'superadmin';
                }),
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
      });
      let button = field('cidl_url', {
        displayComponent: 'cta-btn',
        displayAttrs: {
          hideLabel: true,
          //classNames: ['cta-btn cta-btn--text-right']
        },
        label: 'cidl.links.create_cidl',
      });
      if (show_button) {
        return [cidl, button];
      } else {
        return [cidl];
      }

  })
};


const BASIC_INFO_CREATE_FIELDSET = {
  label: 'service_version.cards.basic_information',
  layout: {
    flex: [50, 50, 50, 25, 25, 100, 100, 100],
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
      'visible_to_marketplace', {
        label: 'service_version.fields.visible_to_marketplace',
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

const BASIC_INFO_CREATE_FIELDSET_LIMITED = {
  label: 'service_version.cards.basic_information',
  layout: {
    flex: [50, 50, 50, 25, 25, 100, 100, 100],
  },
  fields: [
    field(
      'version', {
        label: 'service_version.fields.version',
        type: 'text'
      }
    ),
    field(
      'my_service', {
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
        hint: 'service_version.hints.in_catalogue',
        disabled: true,
      }
    ),
    field(
      'visible_to_marketplace', {
        label: 'service_version.fields.visible_to_marketplace',
        hint: 'service_version.hints.visible_to_marketplace',
        disabled: true,
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


const CONTRACT_FIELDSET = {
  label: 'service_version.cards.contract',
  fields: [
    field(
      'terms_of_use_url', {
        type: 'text',
        label: 'service_version.fields.terms_of_use',
        hint: 'service_version.hints.terms_of_use',
      }
    ),
    field(
      'privacy_policy_url', {
        type: 'text',
        label: 'service_version.fields.privacy_policy',
        hint: 'service_version.hints.privacy_policy',
      }
    ),
    access_policies,
  ],
  layout: {
    flex: [ 100, 100, 100 ]
  }
};

const DETAILS_FIELDSETS = [
  BASIC_INFO_FIELDSET,
  COMPONENT_LINKS_FIELDSET,
  URLS_FIELDSET,
  CONTRACT_FIELDSET,
];

const CREATE_FIELDSETS = [
  BASIC_INFO_CREATE_FIELDSET,
  URLS_FIELDSET,
  FINANCIAL_FIELDSET,
  CONTRACT_FIELDSET,
];

const CREATE_FIELDSETS_LIMITED = [
  BASIC_INFO_CREATE_FIELDSET_LIMITED,
  URLS_FIELDSET,
  FINANCIAL_FIELDSET,
  CONTRACT_FIELDSET,
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  CREATE_FIELDSETS_LIMITED
};
