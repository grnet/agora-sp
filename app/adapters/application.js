import BaseAdapter from 'ember-gen-apimas/adapters/application';

export default BaseAdapter.extend({
  extract_last_token(str, sep) {
    return str.split(sep).filter(t => t).pop();
  },

  buildURL(modelName, endpoint, snapshot, requestType, query) {
    const id = endpoint && this.extract_last_token(endpoint, "/");
    const url = this._super(modelName, id, snapshot, requestType, query);
    return url;
  },
});
