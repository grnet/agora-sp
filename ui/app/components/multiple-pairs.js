import Ember from 'ember';
const {
    get, set,
    computed,
    computed: { or, alias },
    on
} = Ember;

function isValidHttpUrl(string) {
  let url;
  
  try {
    url = new URL(string);
  } catch (_) {
    return false;
  }

  return url.protocol === "http:" || url.protocol === "https:";
}

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
      if (typeof val === 'string' && isValidHttpUrl(val)) {
        res['multimedia link'] = val
      }
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
      let name = Ember.$('#multimedia-name').val();
      let url = Ember.$('#multimedia-url').val();
      let valueObj = get(this, 'valueObj');
      if (!valueObj) {
        valueObj = {};
      }
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
