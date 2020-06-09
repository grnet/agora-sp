import { field } from 'ember-gen';

const SORT_FIELDS = [
  'name',
];

const FIELDSETS = [{
  label: 'order_type.cards.basic',
  fields: [
    'name',
    'description'
  ],
  layout: {
    flex: [100, 100],
  },
}];

export {
  FIELDSETS,
  SORT_FIELDS,
}
