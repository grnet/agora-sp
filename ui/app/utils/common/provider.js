import { field } from 'ember-gen';
import { fileField } from '../../lib/common';

/********************************************
                DETAILS VIEW
********************************************/

const DETAILS_FIELDSETS = [{
  label: 'provider.cards.basic_information',
  text: 'provider.cards.basic_hint',
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 100, 100, 100, 50]
  },
  fields: [
    'name',
    'contact',
    'pd_bai_0_id',
    'pd_bai_1_name',
    'pd_bai_2_abbreviation',
    'pd_bai_3_legal_status',
    'pd_bai_4_website',
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
      }
    ),
    fileField(
      'logo', 'provider', 'logo', {
        readonly: true,
      }, {
        img: true
      }
    ),
    'pd_bai_3_legal_entity',
  ]
}]


/********************************************
                EDIT VIEW
********************************************/

const EDIT_FIELDSETS = [{
  label: 'provider.cards.basic_information',
  text: 'provider.cards.basic_hint',
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 50]
  },
  fields: [
    'name',
    'contact',
    'pd_bai_0_id',
    'pd_bai_1_name',
    'pd_bai_2_abbreviation',
    'pd_bai_3_legal_status',
    'pd_bai_4_website',
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
      }
    ),
    fileField(
      'logo', 'provider', 'logo', {
      }, {
        img: true
      }
    ),
    'pd_bai_3_legal_entity',
  ]
}]



/********************************************
                CREATE  VIEW
********************************************/

const CREATE_FIELDSETS = [{
  label: 'provider.cards.basic_information',
  text: 'provider.cards.basic_hint',
  layout: {
    flex: [100, 100, 100, 100, 100, 100, 50]
  },
  fields: [
    'name',
    'contact',
    'pd_bai_0_id',
    'pd_bai_1_name',
    'pd_bai_2_abbreviation',
    'pd_bai_3_legal_status',
    'pd_bai_4_website',
    field(
      'description', {
        type: 'text',
        htmlSafe: true,
        formComponent: 'text-editor',
      }
    ),
    'pd_bai_3_legal_entity',
  ]
}]


export {
  DETAILS_FIELDSETS,
  EDIT_FIELDSETS,
  CREATE_FIELDSETS
};
