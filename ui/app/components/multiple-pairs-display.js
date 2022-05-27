import Ember from 'ember';
const {
    get,
    computed,
} = Ember;

export default Ember.Component.extend({
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
});
