import BaseAdapter from 'ember-gen-apimas/adapters/application';
import ENV from '../config/environment';

const {
  get,
  inject,
} = Ember;

export default BaseAdapter.extend({
  session: inject.service('session'),

  removeDuplicates(type, data) {
  /*
   * In the case of model fields that use agora-chips formComponent,
   * we want to remove duplicate entries before sending to backend.
   * For example, 'tennis, windsurf, tennis, tricking' field value
   * would be sent as 'tennis, windsurf, tricking'.
   *
   * */
    let fields_to_check = [];
    // gather model fields that need to be checked
    type.eachAttribute(function(name, meta) {
      let options = meta.options;
      if ('formComponent'in options && options['formComponent'] === 'agora-chips' ) {
        fields_to_check.push(name);
      }
    });

    for (var field of Object.keys(data)) {
      if (fields_to_check.includes(field)) {

        let value = data[field] || '';

        let noDuplicates = (item, index, arr) => {
          return arr.indexOf(item) === index
        };

        // remove duplicates from data's field value
        let newValue = value
          .split(',')
          .map(x => { return x.trim()})
          .filter(noDuplicates)
          .filter( x => { return x!= ''})
          .join(', ')

        data[field] = newValue;

      }
    }

    return data;
  },

  filterRecordData(action, data, model_name) {
    let permissions = (ENV.APP || {}).permissions || {'*': {'*': {'*': {'*': {'*': 'default'}}}}};
    let role = get(this, 'session.session.authenticated.role');

    let res = {};
    let fields = Object.keys(permissions[model_name][action][role]);
    if (fields == '*') { return data; }
    fields.forEach((f) => {
      res[f] = data[f]
    })
    return res;
  },

  updateRecord(store, type, snapshot) {
    let data = {};
    let serializer = store.serializerFor(type.modelName);

    serializer.serializeIntoHash(data, type, snapshot);

    let id = snapshot.id;
    let url = this.buildURL(type.modelName, id, snapshot, 'updateRecord');

    data = this.removeDuplicates(type, data);

    if (type.hasOwnProperty('apimasResourceName')) {
      data = this.filterRecordData('partial_update', data, type.apimasResourceName)
    }

    return this.ajax(url, 'PATCH', { data: data });

  },

  createRecord(store, type, snapshot) {
    let data = {};
    let serializer = store.serializerFor(type.modelName);
    let url = this.buildURL(type.modelName, null, snapshot, 'createRecord');

    serializer.serializeIntoHash(data, type, snapshot, { includeId: true });

    data = this.removeDuplicates(type, data);

    if (type.hasOwnProperty('apimasResourceName')) {
      data = this.filterRecordData('create', data, type.apimasResourceName)
    }

    return this.ajax(url, 'POST', { data: data });
  },

});
