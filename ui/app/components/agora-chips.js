import Ember from 'ember';
import BaseFieldMixin from 'ember-gen/lib/base-field';

const {
  get,
  set,
  computed,
  computed: { reads },
} = Ember;

/*
 *  Agora-chips component is based on ember-paper's paper-chips component.
 *  In order to be used, the field must have formComponent: agora-chips,
 *  and the following formAttrs are available:
 *  - options (array): The available options for autocompleting the field
 *  - exactMatch (boolean): If set to true, the value typed by the user
 *  must be an exact match of one of the options.
 *
 * */
export default Ember.Component.extend(BaseFieldMixin, {
  i18n: Ember.inject.service(),
  tagName: 'md-input-container',
  classNames: ['md-default-theme'],
  classNameBindings: [
    'disabled:field-disabled',
    'isEmpty',
    'errors.length:md-input-invalid',
    'focused:md-focused',
    'focused:md-input-focused',
  ],
  exactMatch: reads('fattrs.exactMatch'),
  options: reads('fattrs.options'),

  requireMatch: computed('exactMatch', 'options', function(){
    let exactMatch = get(this, 'exactMatch');
    let options = get(this, 'options');

    if (options) {
      return exactMatch? exactMatch: false;
    } else {
      return null;
    }
  }),

  noMatchesMessage: computed('requireMatch', function(){
    const i18n = this.get('i18n');
    let requireMatch = get(this, 'requireMatch');
    if (requireMatch) {
      return i18n.t('common.chips.noMatchFound');
    } else if (requireMatch === false) {
      return i18n.t('common.chips.noMatchFoundClickToAdd');
    } else {
      return null;
    }

  }),

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

    focusIn: function() {
      set(this, 'focused', true);
    },

    focusOut: function() {
      set(this, 'focused', false);
    },

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
