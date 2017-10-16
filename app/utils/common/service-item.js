import { field } from 'ember-gen';

const DETAILS_FIELDSETS = [
  //this creates a new referenced table inside another gen
  {
    label: 'test',
    fields: [
      field(
        'name', {
          type: 'text',
          label: 'service_item.fields.name'
        }
      ),
      field(
        'service_area', {
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
        'short_description', {
          type: 'text',
          label: 'service_item.fields.short_description'
        }
      ),
      field(
        'description_external', {
          type: 'text',
          label: 'service_item.fields.description_external'
        }
      ),
      field(
        'description_internal', {
          type: 'text',
          label: 'Internal Description'
        }
      ),
      field(
        'funders_for_service', {
          type: 'text',
          label: 'Funders for Service'
        }
      ),
      field(
        'value_to_customer', {
          type: 'text',
          label: 'Value to customer'
        }
      ),
      field(
        'competitors', {
          type: 'text',
          label: 'Competitors'
        }
      ),
      field(
        'risks', {
          type: 'text',
          label: 'Risks'
        }
      ),
      field(
        'request_procedures', {
          type: 'text',
          label: 'Request Procedures'
        }
      ),
      field(
        'service_trl.value', {
          type: 'text',
          label: 'Service TRL'
        }
      ),
      field(
        'id_service_owner.full_name', {
          type: 'text',
          label: 'Service Owner'
        }
      ),
      field(
        'id_contact_information.first_name', {
          type: 'text',
          label: 'Contact Information'
        }
      ),
    ],
    layout: {
      flex: [ 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100 ]
    }
  },
  {
    label: 'Service Versions',
    fields: [
      field('versions', {
        modelName: 'service_version',
        displayComponent: 'gen-display-field-table',
        valueQuery: (store, params, model, value) => {
          if(model.get('id')) {
            return store.query('service_version', { id_service: model.get('id') });
          }
        },
        modelMeta: {
          row: {
            fields: [
              'version',
              'id_service.name'
            ]
          }
        }
      })
    ]
  },
];

export { DETAILS_FIELDSETS };
