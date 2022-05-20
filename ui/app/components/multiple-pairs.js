import Ember from 'ember';
const {
    get, set,
    computed,
    computed: { or, alias },
    on
} = Ember;

export default Ember.Component.extend({
  classNames: ['multiple-pairs'],
  tagName: 'md-input-container',
  error: false,

  clearInput(){
    Ember.$('#multimedia-name').val(null);
    Ember.$('#multimedia-url').val(null);
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
    return Object.entries(valueObj);

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
      let name = Ember.$('#multimedia-name').val();
      let url = Ember.$('#multimedia-url').val();
      let valueObj = get(this, 'valueObj');
      valueObj[name] = url;
      if (!name || !url) {
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
