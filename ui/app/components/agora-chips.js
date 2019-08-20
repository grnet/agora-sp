import Ember from 'ember';
import BaseFieldMixin from 'ember-gen/lib/base-field';

const {
  get,
  computed,
} = Ember;

export default Ember.Component.extend(BaseFieldMixin, {
  tagName: 'md-input-container',
  classNames: ['md-default-theme'],
  classNameBindings: [
    'disabled:field-disabled',
    'isEmpty',
    'errors.length:md-input-invalid',
  ],

  newVal: computed('content.@each', function(){
    return get(this, 'content').join(', ');
  }),

  content: computed('value', function(){
    let value = get(this, 'value') || '';

    return value
      .split(',')
      .map(x => { return x.trim()})
      .filter( x => { return x!= ''})
  }),

  isEmpty: computed('content.@each', function(){
    if (get(this, 'content').length > 0) {
      return 'md-input-has-value';
    }
  }),

  getInput() {
    return this.element.querySelector('.md-chip-input-container input');
  },

  click() {
    this.getInput().focus();
  },

  actions: {

    removeItem(item) {
      let content = get(this, 'content');

      content.removeObject(item);
      this.onChange(get(this, 'newVal'));
    },

    addItem(item) {
      item = item.trim();
      let content = get(this, 'content');

      content.pushObject(item);
      this.onChange(get(this, 'newVal'));
    },
  },

})
