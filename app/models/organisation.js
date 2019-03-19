import DS from 'ember-data';
import { shorten } from '../utils/common/common';

const {
  get,
  computed,
} = Ember;


export default DS.Model.extend({
  name: DS.attr({
    label: 'organisation.fields.name',
    hint: 'organisation.hints.name'
  }),
  description: DS.attr({
    label: 'organisation.fields.description',
    hint: 'organisation.hints.description'
  }),
  logo: DS.attr({
    label: 'organisation.fields.logo',
    hint: 'organisation.hints.logo'
  }),
  // computed
  short_desc: computed('description', function() {
    return shorten(get(this, 'description'));
  }),
});
