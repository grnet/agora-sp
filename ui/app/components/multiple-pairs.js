import Ember from 'ember';
const {
    get, set,
    computed,
    computed: { or, alias, reads },
    on
} = Ember;

export default Ember.Component.extend({
  i18n: Ember.inject.service(),
  classNames: ['multiple-pairs'],
  tagName: 'md-input-container',
  error: false,

  actionTitle: reads('fattrs.actionTitle'),

  item1: reads('fattrs.item1'),
  item2: reads('fattrs.item2'),

  input1: computed('', function(){
    let item1 = get(this, 'item1');
    return Ember.$(`#${item1}`);
  }),

  input2: computed('', function(){
    let item2 = get(this, 'item2');
    return Ember.$(`#${item2}`);
  }),
  errorHint: computed('', function(){
    let i18n = get(this, 'i18n');
    let item1 = get(this, 'item1');
    let trans1 = i18n.t(item1);
    let item2 = get(this, 'item2');
    let trans2 = i18n.t(item2);
    return `Both ${trans1} and ${trans2} must be filled`;
  }),

  clearInput(){
    let input1 = get(this, 'input1');
    let input2 = get(this, 'input2');
    input1.val(null);
    input2.val(null);
  },

  valueObj: computed('value', function(){
    let val = get(this, 'value');
    let res = {};
    try {
      res = JSON.parse(val);
    } catch(e) {
      console.log('Value needs to be in JSON format')
    }
    return res;
  }),

  valueArr: computed('valueObj', function(){
    let valueObj = get(this, 'valueObj');
    if (!!valueObj) {
      return Object.entries(valueObj);
    }
    else {
      return [];
    }
  }),


  actions: {

    removePair(name, url){
      let valueObj = get(this, 'valueObj');
      if (valueObj[name] == url) {
        delete valueObj[name];
      }
      return this.sendAction('onChange', JSON.stringify(valueObj));
    },

    addPair(e) {
      let input1 = get(this, 'input1');
      let input1_val = input1.val();
      let input2 = get(this, 'input2');
      let input2_val = input2.val();
      let valueObj = get(this, 'valueObj');
      if (!valueObj) {
        valueObj = {};
      }
      valueObj[input1_val] = input2_val;
      if (!input1_val || !input2_val) {
        set(this, 'error', true);
        return;
      } else {
        set(this, 'error', false);
      }

      this.clearInput();
      return this.sendAction('onChange', JSON.stringify(valueObj));
    },
  }
});
