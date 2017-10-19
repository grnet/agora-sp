import { field } from 'ember-gen';

const DETAILS_FIELDSETS = [
  //this creates a new referenced table inside another gen
  {
    label: 'service_item.cards.basic_information',
    fields: [
      field(
        'name', {
          type: 'text',
          label: 'service_item.fields.name'
        }
      ),
      field(
        'service_area.name', {
          type: 'text',
          label: 'service_item.fields.service_area'
        }
      ),
      field(
        'service_trl.value', {
          type: 'text',
          label: 'service_trl.belongs.value'
        }
      ),
    ],
    layout: {
      flex: [ 100, 100, 100 ]
    }
  },
  {
    label: 'service_version.belongs.cards.title',
    layout: {
      flex: [ 100, 100 ]
    },
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
            actions: ['goToDetails', 'goToEdit'],
            actionsMap: {
              goToDetails: {
                label: 'details',
                icon: 'remove red eye',
                action(route, model) {
                  let resource = model.get('_internalModel.modelName'),
                    dest_route = `${resource}.record.index`;
                  route.transitionTo(dest_route, model)
                }
              },
              goToEdit: {
                label: 'edit',
                icon: 'edit',
                action(route, model) {
                  let resource = model.get('_internalModel.modelName'),
                    dest_route = `${resource}.record.edit.index`;
                  route.transitionTo(dest_route, model)
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
                'id_service.name', {
                  label: 'service_item.belongs.name'
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
  },
  {
    label: 'service_item.cards.details',
    fields: [
      field(
        'service_type', {
          type: 'text',
          label: 'service_item.fields.service_type'
        }
      ),
      field(
        'short_description', {
          type: 'text',
          label: 'service_item.fields.short_description',
          htmlSafe: true
        }
      ),
      field(
        'description_external', {
          type: 'text',
          label: 'service_item.fields.description_external',
          htmlSafe: true
        }
      ),
      field(
        'description_internal', {
          type: 'text',
          label: 'service_item.fields.description_external',
          htmlSafe: true
        }
      ),
      field(
        'funders_for_service', {
          type: 'text',
          label: 'service_item.fields.funders',
          htmlSafe: true
        }
      ),
      field(
        'value_to_customer', {
          type: 'text',
          label: 'service_item.fields.customer_value',
          htmlSafe: true
        }
      ),
      field(
        'competitors', {
          type: 'text',
          label: 'service_item.fields.competitors',
          htmlSafe: true
        }
      ),
      field(
        'risks', {
          type: 'text',
          label: 'service_item.fields.risks',
          htmlSafe: true
        }
      ),
      field(
        'request_procedures', {
          type: 'text',
          label: 'service_item.fields.procedures',
          htmlSafe: true
        }
      ),
      field(
        'id_service_owner.full_name', {
          type: 'text',
          label: 'service_owner.belongs.full_name'
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
      flex: [ 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100 ]
    }
  },
];

export { DETAILS_FIELDSETS };
