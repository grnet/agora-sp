import DS from 'ember-data';
import Serializer from './application';

 export default Serializer.extend({
   serialize(snapshot, options) {
    var json = this._super(...arguments);
    Object.keys(json).forEach(function(key) {
      if (key.endsWith('_url')) {
        let new_key = key.replace('_url', '_has');
        json[new_key] = key? true: false;
      }
    });
    return json;
  }

 })
