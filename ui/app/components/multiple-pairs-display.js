import Ember from 'ember';
const {
    get,
    computed,
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
    console.log(valueObj)
    if (!!valueObj) {
      return Object.entries(valueObj);
    }
    else {
      return [];
    }
  }),
});
