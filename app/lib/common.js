import { CRUDGen } from 'ember-gen/lib/gen';
import { field } from 'ember-gen';

const {
  get,
  computed: { reads },
  computed,
  merge,
  assign,
  assert,
  inject
} = Ember;


const AgoraGen = CRUDGen.extend({
  auth: true,
  list: {
    layout: 'table',
    paginate: {
      limits: [ 10, 50, 100 ],
      serverSide: false,
      active: true
    }
  }
});

function fileField(key, path, kind, attrs, formAttrs) {
  return field(key, assign({}, {
    type: 'file',
    formComponent: 'agora-file-field',
    displayComponent: 'agora-file-field',
    displayAttrs: assign({hideLabel: true}, { path, kind }, formAttrs || {}),
    sortBy: 'filename',
    formAttrs: assign({}, { path, kind }, formAttrs || {})
  }, attrs || {}));
}


export {
  AgoraGen,
  fileField
};
