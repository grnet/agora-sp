import { field } from 'ember-gen';

/********************************************
                LIST VIEW
********************************************/

const SORT_FIELDS = [];
const TABLE_FIELDS = [
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
    field('service_type', {
      type: 'text',
      label: 'cidl.fields.service_type'
    }),
    field('service_id.name', {
      type: 'text',
      label: 'service_item.belongs.name'
    }),
    field('service_details_id.version', {
      type: 'text',
      label: 'service_version.belongs.version'
    }),
];

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [
  {
    label: 'cidl.cards.components',
    layout: {
      flex: [100, 100, 100 ,100]
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
      field('service_type', {
        type: 'text',
        label: 'cidl.fields.service_type'
      }),
      field('configuration_parameters', {
        type: 'text',
        label: 'cidl.fields.configuration_parameters'
      }),
    ]
  },
  {
    label: 'cidl.cards.service_version',
    fields: [
      field(
        'service_id.name', {
          type: 'text',
          label: 'service_item.belongs.name'
        }
      ),
      field(
        'service_details_id.version', {
          label: 'service_version.belongs.version'
        }
      ),
    ],
    layout: {
      flex: [100, 100]
    }
  }
];

/********************************************
                  EDIT VIEW
********************************************/

const CREATE_FIELDSETS = [
  {
    label: 'cidl.cards.components',
    fields: [
      field('service_component', {
        label: 'component.belongs.name'
      }),
      field('service_component_implementation', {
        label: 'component_implementation.belongs.name'
      }),
      field('service_component_implementation_detail_id', {
        label: 'component_implementation_detail.belongs.name'
      }),
      field('service_type', {
        label: 'cidl.fields.service_type',
        hint: 'cidl.hints.service_type'
      }),
      field('configuration_parameters', {
        label: 'cidl.fields.configuration_parameters'
      })
    ],
    layout: {
      flex: [100, 100, 100, 100]
    }
  },
  {
    label: 'cidl.cards.service_version',
    fields: [
      field('service_id', {
        label: 'service_item.belongs.name'
      }),
      field('service_details_id', {
        label: 'service_version.belongs.version'
      }),
    ],
    layout: {
      flex: [100, 100]
    }
  }
];

/********************************************
                  EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [
  {
    label: 'components',
    fields: [
      field('service_component', {
        label: 'component.belongs.name'
      }),
      field('service_component_implementation', {
        label: 'component_implementation.belongs.name'
      }),
      field('service_component_implementation_detail_id', {
        label: 'component_implementation_detail.belongs.name'
      }),
      field('service_type', {
        type: 'text',
        hint: 'cidl.hints.service_type'
      }),
      field('configuration_parameters', {
        type: 'text'
      }),
    ],
    layout: {
      flex: [100, 100, 100, 100]
    }
  },
  {
    label: 'service version',
    fields: [
      field('service_id', {
        label: 'service_item.belongs.name'
      }),
      field('service_details_id', {
        label: 'service_version.belongs.version'
      }),
    ],
    layout: {
      flex: [100, 100]
    }
  }
];

/********************************************
                  FILTERS
********************************************/
const TABLE_FILTERS = [
  field(
    'service_id', {
      modelName:'service_item',
      type: 'model',
      label: 'service_item.belongs.name',
      displayAttr: 'name'
    }
  ),
  field(
    'service_details_id', {
      disabled: Ember.computed('model.changeset.service_id.id', function() {
        return !Ember.get(this, 'model.changeset.service_id');
      }),
      label: 'service_version.belongs.version',
      modelName:'service_version',
      type: 'model',
      displayAttr: 'version',
      query: Ember.computed('model.changeset.service_id.id', function() {
        let comp = Ember.get(this, 'model.changeset.service_id.id');
        return function(select, store, field, params) {
          params = params || {};
          params.id_service = comp;
          return store.query('service-version', params);
        }
      })
    }
  ),
];

export {
  TABLE_FIELDS,
  SORT_FIELDS,
  DETAILS_FIELDSETS,
  CREATE_FIELDSETS,
  EDIT_FIELDSETS,
  TABLE_FILTERS
};
