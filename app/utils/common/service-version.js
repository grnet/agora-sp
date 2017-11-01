import { field } from 'ember-gen';

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
      type: 'text',
      htmlSafe: true
    }
  ),
  field(
    'features_future', {
      label: 'service_version.fields.features_future',
      type: 'text',
      htmlSafe: true
    }
  ),
  field(
    'use_cases', {
      label: 'service_version.fields.use_cases',
      type: 'text',
      htmlSafe: true
    }
  ),
  ]
};

const DETAILS_FIELDSETS = [
  BASIC_INFO_FIELDSET,
  URLS_FIELDSET,
  FINANCIAL_FIELDSET
];

const CREATE_FIELDSETS = [
  BASIC_INFO_FIELDSET,
  URLS_FIELDSET,
  FINANCIAL_FIELDSET,
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS
};
