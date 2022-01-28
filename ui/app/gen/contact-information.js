import { AgoraGen } from '../lib/common';
import { field } from 'ember-gen';
import validate from 'ember-gen/validate';

const { get, set, computed } = Ember;

export default AgoraGen.extend({
  modelName: 'contact-information',
  order: 600,
  path: 'contact-information',
  resourceName: 'api/v2/contact-information',
  abilityStates: {
    // a servicedmin can edit a contact if they belongs
    // to the same organisation
    update_organisation_owned: computed('model.organisation_id', 'user.organisation', function() {
      let user_org =  get(this, 'user.organisation');
      let contact_org =  get(this, 'model.organisation_id');
      return user_org === contact_org;
    }),
    create_organisation_owned: true,
  },
  common: {
    validators: {
      first_name: [validate.presence(true)],
      last_name: [validate.presence(true)],
      email: [
        validate.presence(true),
        validate.format({type: 'email'})
      ],
      phone: [
        validate.number({ integer: true, allowBlank: true }),
        validate.length({ min: 10, max: 20, allowBlank: true }),
      ],
      organisation: [validate.presence(true)],
    },
    fieldsets: [ {
      text: 'contact_information.cards.basic_hint',
      label: 'contact_information.cards.basic_info',
      fields: computed('user.role', function() {
        let role = get(this, 'user.role');
        let disabled  = role === 'serviceadmin' || role === 'provideradmin' ;
        return [
          field('first_name', { label: 'contact_information.fields.first_name.required' }),
          field('last_name', { label: 'contact_information.fields.last_name.required' }),
          field('email', { label: 'contact_information.fields.email.required' }),
          'phone',
          'position',
          field('organisation', {disabled, label: 'contact_information.fields.organisation.required'}),
        ]
      }),
      layout: {
        flex: [50, 50, 50, 50, 50, 50],
      },
    }],
  },
  list: {
    page: {
      title: 'contact_information.menu'
    },
    row: {
      actions: ['gen:details', 'gen:edit', 'remove'],
      fields: [
        'first_name',
        'last_name',
        'email',
        'position',
        field('organisation.epp_bai_1_name', {label: 'contact_information.fields.organisation'}),
      ]
    },
    menu: {
      label: 'contact_information.menu',
      icon: 'ContactMail',
      order: 60,
    },
    sort: {
      serverSide: true,
      active: true,
      fields: ['email', 'position', 'first_name', 'last_name'],
    },
    filter: {
      active: true,
      serverSide: true,
      search: true,
      searchPlaceholder: 'contact_information.placeholders.search',
      meta: {
        fields: [
          field('organisation', {
            modelName:'provider',
            label: 'contact_information.fields.organisation',
            type: 'model',
            displayAttr: 'epp_bai_1_name',
          }),
        ],
      },
    },
  },
  details: {

    fieldsets: [ {
      label: 'contact_information.cards.basic_info',
      fields: [
        'first_name',
        'last_name',
        'email',
        'phone',
        'position',
        field('organisation.epp_bai_1_name',{label:'contact_information.fields.organisation'}),
      ],
      layout: {
        flex: [50, 50, 50, 50, 50, 50],
      },
    }],
  },
  create: {
    // If the user creating the Contact is a serviceadmin, the
    // organisation should be prefilled with user's organisation
    getModel(params) {
      const store = get(this, 'store');
      const role = get(this, 'session.session.authenticated.role')
      const org_id = get(this, 'session.session.authenticated.organisation')
      if (role === 'serviceadmin' || role === 'provideradmin') {

        let org = store.findRecord('provider', org_id);
        return org.then(function(organisation) {
          return store.createRecord('contact-information', {
            organisation,
          })
        })

      }
      return store.createRecord('contact-information');
    },
  },
});
