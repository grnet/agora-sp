import { field } from 'ember-gen';
import { fileField } from '../../lib/common';


/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [{
  label: 'service_area.cards.basic_information',
  text: 'service_area.cards.basic_hint',
  layout: {
    flex: [100, 100]
  },
  fields: [
    field(
      'name', {
        'label': 'service_area.fields.name',
        'hint': 'service_area.hints.name'
      }
    ),
    fileField(
      'icon', 'service-area', 'icon', {
        readonly: true,
        label: 'service_area.fields.icon',
        hint: 'service_area.hints.icon',
      }, {
        img: true
      }
    ),
  ]
}]


/********************************************
                EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [{
  label: 'service_area.cards.basic_information',
  text: 'service_area.cards.basic_hint',
  layout: {
    flex: [100, 100]
  },
  fields: [
    field(
      'name', {
        'label': 'service_area.fields.name',
        'hint': 'service_area.hints.name'
      }
    ),
    fileField(
      'icon', 'service-area', 'icon', {
        readonly: false,
        label: 'service_area.fields.icon',
        hint: 'service_area.hints.icon',
      }, {
        replace: true,
        img: true
      }
    ),
  ]
}]


/********************************************
                CREATE  VIEW
********************************************/

const CREATE_FIELDSETS = [{
  label: 'service_area.cards.basic_information',
  text: 'service_area.cards.basic_hint',
  layout: {
    flex: [100, 100]
  },
  fields: [
    field(
      'name', {
        'label': 'service_area.fields.name',
        'hint': 'service_area.hints.name'
      }
    ),
  ]
}]


export {
  DETAILS_FIELDSETS,
  EDIT_FIELDSETS,
  CREATE_FIELDSETS
};
