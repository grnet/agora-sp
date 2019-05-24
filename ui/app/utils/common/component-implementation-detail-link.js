import { field } from 'ember-gen';

const COMPONENT_EDIT_FIELDSET = {
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
    flex: [100, 100, 100, 100, 100]
  }
};

const SERVICE_EDIT_FIELDSET = {
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
};


const SERVICE_EDIT_FIELDSET_LIMITED = {
  label: 'cidl.cards.service_version',
  fields: [
    field('my_service', {
      label: 'service_item.belongs.name'
    }),
    field('my_service_version', {
      label: 'service_version.belongs.version'
    }),
  ],
  layout: {
    flex: [100, 100]
  }
};

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
      flex: [100, 100, 100 ,100, 100]
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
                  CREATE VIEW
********************************************/

const CREATE_FIELDSETS = [
  COMPONENT_EDIT_FIELDSET,
  SERVICE_EDIT_FIELDSET,
];

const CREATE_FIELDSETS_LIMITED = [
  COMPONENT_EDIT_FIELDSET,
  SERVICE_EDIT_FIELDSET_LIMITED,
];

/********************************************
                  EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [
  COMPONENT_EDIT_FIELDSET,
  SERVICE_EDIT_FIELDSET,
];

const EDIT_FIELDSETS_LIMITED = [
  COMPONENT_EDIT_FIELDSET,
  SERVICE_EDIT_FIELDSET_LIMITED,
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
  CREATE_FIELDSETS_LIMITED,
  EDIT_FIELDSETS,
  EDIT_FIELDSETS_LIMITED,
  TABLE_FILTERS
};
