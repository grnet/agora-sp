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
},
{
  label: 'provider.cards.location',
  text: 'provider.cards.location_hint',
  layout: {
    flex: [100, 100, 100, 100, 100]
  },
  fields: [
    'pd_loi_1_street_name_and_number',
    'pd_loi_2_postal_code',
    'pd_loi_3_city',
    'pd_loi_4_region',
    'pd_loi_5_country_or_territory',
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
},
{
  label: 'provider.cards.location',
  text: 'provider.cards.location_hint',
  layout: {
    flex: [100, 100, 100, 100, 100]
  },
  fields: [
    'pd_loi_1_street_name_and_number',
    'pd_loi_2_postal_code',
    'pd_loi_3_city',
    'pd_loi_4_region',
    'pd_loi_5_country_or_territory',
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
},
{
  label: 'provider.cards.location',
  text: 'provider.cards.location_hint',
  layout: {
    flex: [100, 100, 100, 100, 100]
  },
  fields: [
    'pd_loi_1_street_name_and_number',
    'pd_loi_2_postal_code',
    'pd_loi_3_city',
    'pd_loi_4_region',
    'pd_loi_5_country_or_territory',
  ]
}]


export {
  DETAILS_FIELDSETS,
  EDIT_FIELDSETS,
  CREATE_FIELDSETS
};
