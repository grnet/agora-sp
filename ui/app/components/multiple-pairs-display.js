import Ember from 'ember';
const {
    get,
    computed,
} = Ember;

export default Ember.Component.extend({
  valueObj: computed('value', function(){
    let val = get(this, 'value');
    return JSON.parse(val);
  }),
  valueArr: computed('valueObj', function(){
    let valueObj = get(this, 'valueObj');
    return Object.entries(valueObj);
  }),
});
