import DS from 'ember-data';
import { shorten } from '../utils/common/common';

const {
  get,
  computed,
} = Ember;


export default DS.Model.extend({
  name: DS.attr({
    label: 'provider.fields.name',
    hint: 'provider.hints.name'
  }),
  description: DS.attr({
    label: 'provider.fields.description',
    hint: 'provider.hints.description'
  }),
  logo: DS.attr({
    label: 'provider.fields.logo',
    hint: 'provider.hints.logo'
  }),
  // computed
  short_desc: computed('description', function() {
    return shorten(get(this, 'description'));
  }),
});
