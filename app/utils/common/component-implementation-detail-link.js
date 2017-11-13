import { field } from 'ember-gen';

/********************************************
                LIST VIEW
********************************************/

const SORT_FIELDS = [];
const TABLE_FIELDS = [
    field('service_component_implementation_detail_id.component_id.name', {
      type: 'text',
    }),
    field('service_component_implementation_detail_id.component_implementation_id.name', {
      type: 'text',
    }),
    field('service_component_implementation_detail_id.version', {
      type: 'text',
    }),
    field('configuration_parameters', {
      type: 'text'
    }),
    field(
      'service_id.name', {
      type: 'text',
      }
    ),
    field(
      'service_details_id.version', {
      }
    ),
];

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'components',
    layout: {
      flex: [100, 100, 100 ,100]
    },
    fields: [
      field('service_component_implementation_detail_id.component_id.name', {
        type: 'text',
      }),
      field('service_component_implementation_detail_id.component_implementation_id.name', {
        type: 'text',
      }),
      field('service_component_implementation_detail_id.version', {
        type: 'text',
      }),
      field('configuration_parameters', {
        type: 'text'
      }),
    ]
  },
  {
    label: 'service version',
    fields: [
      field(
        'service_id.name', {
        type: 'text',
        }
      ),
      field(
        'service_details_id.version', {
        }
      ),
    ]
  }
];

/********************************************
                  EDIT VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'components',
    fields: [
      field('service_component', {}),
      field('service_component_implementation', {}),
      field('service_component_implementation_detail_id', {}),
      field('configuration_parameters', {})
    ]
  },
  {
    label: 'service version',
    fields: [
      field('service_id', {}),
      field('service_details_id', {}),
    ]
  }
];

/********************************************
                  EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [
  {
    label: 'components',
    fields: [
      'service_component',
      'service_component_implementation',
      'service_component_implementation_detail_id',
      field('configuration_parameters', {
        type: 'text'
      }),
    ]
  },
  {
    label: 'service version',
    fields: [
      'service_id',
      'service_details_id',
      /*field(
        'service_id', {
        type: 'model',
        modelName: 'service_item',
        displayAttr: 'name'
        }
      ),
      field(
        'service_details_id', {
        type: 'model',
        modelName: 'service_version',
        displayAttr: 'version'
        }
      ),*/
    ]
  }
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS
};
