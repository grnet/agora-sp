import ApplicationAdapter from './application';
import ENV from '../config/environment';

const {
  get,
  inject,
} = Ember;

export default ApplicationAdapter.extend({
  session: inject.service('session'),
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

    data = this.filterRecordData('partial_update', data, type.apimasResourceName)

    return this.ajax(url, 'PATCH', { data: data });

  },

  createRecord(store, type, snapshot) {
    let data = {};
    let serializer = store.serializerFor(type.modelName);
    let url = this.buildURL(type.modelName, null, snapshot, 'createRecord');

    serializer.serializeIntoHash(data, type, snapshot, { includeId: true });
    data = this.filterRecordData('create', data, type.apimasResourceName)

    return this.ajax(url, 'POST', { data: data });
  },

});
