import { CRUDGen } from 'ember-gen/lib/gen';
import { field } from 'ember-gen';
import _ from 'lodash/lodash';
import ENV from '../config/environment';
import validate from 'ember-gen/validate';
const EOSC_DISABLED = ENV.APP.eosc_portal.disabled;

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
  _metaMixin: {
    session: Ember.inject.service(),
    role: reads('session.session.authenticated.role')
  },
  list: {
    layout: 'table',
    paginate: {
      limits: [ 10, 50, 100 ],
      serverSide: true,
      active: true
    }
  },
  create: {
    onSubmit(model) {
      let modelName = get(this, 'modelName');
      let index = `${modelName}.record.index`;
      this.transitionTo(index, model);
    },
  },
  details:{
    actions: [
      'gen:edit',
    ],
  },
  edit: {
    actions: [
      'gen:details',
    ],
    onSubmit(model) {
      let modelName = get(this, 'modelName');
      let index = `${modelName}.record.index`;
      this.transitionTo(index, model);
    },
  },


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

function computeI18NChoice(key, choices, ...args) {
    if (typeof lastArg === 'function') {
          hook = args.pop();
        }
    let choicesValues = choices.map(key => key[0]);

    return computed(key, 'i18n.locale', ...args, function() {
          let i18n = get(this, 'i18n');
          let value = get(this, key);
          let i18nKey = '';
          if (choicesValues.indexOf(value) >= 0) {
                  i18nKey = choices[choicesValues.indexOf(value)][1];
                }
          return value && i18nKey && i18n.t(i18nKey);
        });
}

const capitalize = (s) => {
  if (typeof s !== 'string') return ''
  return s.charAt(0).toUpperCase() + s.slice(1)
}


const httpValidator = validate.format({
  regex: /^(https:\/\/|http:\/\/)/i,
  allowBlank: true,
  message: 'urlStarts.message',
})


function basic_model(desc) {
  let fields = desc? ['name', 'description', 'eosc_id']: ['name', 'eosc_id'];
  return basic_model_fields(fields);
}

function basic_model_fields(fields, required) {

  if (EOSC_DISABLED) {
    fields.pop();
  }
  let flex = new Array(fields.length).fill(100);
  let validators = {};
  if (fields.includes('name')) {
    validators.name = [validate.presence(true)]
  }
  if (required) {
    validators[required] = [validate.presence(true)]
  }
  return {
    common: {
      fieldsets: [
        {
          label: 'common.cards.basic',
          fields,
          layout: {
            flex,
          },
        }
      ],
      validators,
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['name', 'eosc_id', 'user'],
    },
  }
}

function fields_eosc(fields) {
  if (EOSC_DISABLED) {
    fields.pop();
  }
  return fields;
}

const EOSC_HINT = EOSC_DISABLED ? '': '<span class="pill">EOSC required</span>';


export {
  AgoraGen,
  fileField,
  computeI18NChoice,
	capitalize,
  httpValidator,
  basic_model,
  basic_model_fields,
  fields_eosc,
  EOSC_HINT,
};
