import DS from 'ember-data';
import { shorten } from '../utils/common/common';
import { capitalize } from '../lib/common';
import { countries } from '../resources';
import ENV from '../config/environment';

const {
  get,
  computed,
} = Ember,
  CHOICES = ENV.APP.resources;

const LEGAL_ENTITIES = ENV.APP.legal_entities;


export default DS.Model.extend({
  name: DS.attr({
    label: 'provider.fields.name',
    hint: 'provider.hints.name'
  }),
  description: DS.attr({
    label: 'provider.fields.description',
    hint: 'provider.hints.description'
  }),
  logo: DS.attr({
    label: 'provider.fields.logo',
    hint: 'provider.hints.logo'
  }),
  contact: DS.attr({
    label: 'provider.fields.contact',
    hint: 'provider.hints.contact',
  }),

  epp_bai_id: DS.attr({
    label: 'provider.fields.epp_bai_id',
    hint: 'provider.hints.epp_bai_id',
  }),
  epp_bai_name: DS.attr({
    label: 'provider.fields.epp_bai_name',
    hint: 'provider.hints.epp_bai_name',
  }),
  epp_bai_abbreviation: DS.attr({
    label: 'provider.fields.epp_bai_abbreviation',
    hint: 'provider.hints.epp_bai_abbreviation',
  }),
  epp_bai_website: DS.attr({
    label: 'provider.fields.epp_bai_website',
    hint: 'provider.hints.epp_bai_website',
  }),
  epp_bai_legal_entity: DS.attr({
    type: 'boolean',
    defaultValue: false,
    label: 'provider.fields.epp_bai_legal_entity',
    hint: 'provider.hints.epp_bai_legal_entity',
  }),
  epp_bai_legal_status: DS.belongsTo('legalstatus', {
    autocomplete: true,
    type: 'select',
    displayAttr: 'name',
    label: 'provider.fields.epp_bai_legal_status',
    hint: 'provider.hints.epp_bai_legal_status',
    inverse: null,
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  epp_bai_hosting_legal_entity: DS.attr({
    label: 'provider.fields.epp_bai_hosting_legal_entity',
    hint: 'provider.hints.epp_bai_hosting_legal_entity',
    autocomplete: true,
    type: 'select',
    choices: LEGAL_ENTITIES,
  }),

  // classification information
  epp_cli_scientific_domain: DS.hasMany('domain', {
    label: 'provider.fields.epp_cli_scientific_domain',
    hint: 'provider.hints.epp_cli_scientific_domain',
  }),
  epp_cli_scientific_domain_verbose: DS.attr({
    label: 'provider.fields.domain_names',
  }),
  // TODO: Filter subdomain's ManyArray results according to domain selections
  epp_cli_scientific_subdomain: DS.hasMany('subdomain', {
    label: 'provider.fields.epp_cli_scientific_subdomain',
    hint: 'provider.hints.epp_cli_scientific_subdomain',
  }),
  epp_cli_scientific_subdomain_verbose: DS.attr({
    label: 'provider.fields.subdomain_names',
  }),
  epp_cli_tags: DS.attr({
    label: 'provider.fields.epp_cli_tags',
    hint: 'provider.hints.epp_cli_tags',
  }),
  epp_cli_structure_type: DS.hasMany('structure', {
    label: 'provider.fields.epp_cli_structure_type',
    hint: 'provider.hints.epp_cli_structure_type',
  }),
  epp_cli_structure_type_verbose: DS.attr({
    label: 'provider.fields.structure_names',
  }),
  // location information
  epp_loi_street_name_and_number: DS.attr({
    label: 'provider.fields.epp_loi_street_name_and_number',
    hint: 'provider.hints.epp_loi_street_name_and_number',
  }),
  epp_loi_postal_code: DS.attr({
    label: 'provider.fields.epp_loi_postal_code',
    hint: 'provider.hints.epp_loi_postal_code',
  }),
  epp_loi_city: DS.attr({
    label: 'provider.fields.epp_loi_city',
    hint: 'provider.hints.epp_loi_city',
  }),
  epp_loi_region: DS.attr({
    label: 'provider.fields.epp_loi_region',
    hint: 'provider.hints.epp_loi_region',
  }),
  epp_loi_country_or_territory: DS.attr({
    type: 'select',
    autocomplete: true,
    // Quickly bake an appropriate select-friendly array from original countries resource
    choices: function () {
      let countrySel = []
      for (let country of countries) {
        countrySel.push([country.toLowerCase(), country]);
      }
      return countrySel;
    }(),
    label: 'provider.fields.epp_loi_country_or_territory',
    hint: 'provider.hints.epp_loi_country_or_territory',
  }),
  // marketing information
  epp_mri_description: DS.attr({
    label: 'provider.fields.epp_mri_description',
    hint: 'provider.hints.epp_mri_description',
  }),
  epp_mri_logo: DS.attr({
    label: 'provider.fields.epp_mri_logo',
    hint: 'provider.hints.epp_mri_logo',
  }),
  epp_mri_multimedia: DS.attr({
    label: 'provider.fields.epp_mri_multimedia',
    formComponent: 'multiple-pairs',
    displayComponent: 'multiple-pairs-display',
    formAttrs: {
      actionTitle: 'add_multimedia',
      item1: 'multimedia_name',
      item2: 'multimedia_url',
    }
  }),
  // computed
  short_desc: computed('description', function() {
    return shorten(get(this, 'description'));
  }),
  epp_mti_life_cycle_status: DS.attr({
    type: 'select',
    autocomplete: true,
    choices: ENV.APP.resources.PROVIDER_LIFE_CYCLE_STATUSES,
    label: 'provider.fields.epp_mti_life_cycle_status',
    hint: 'provider.hints.epp_mti_life_cycle_status',
  }),
  // maturity information
  epp_mti_certifications: DS.attr({
    label: 'provider.fields.epp_mti_certifications',
    hint: 'provider.hints.epp_mti_certifications',
  }),
  // contact information
  main_contact: DS.belongsTo('contact-information', {
    autocomplete: true,
    type: 'select',
    label: 'provider.fields.main_contact',
    hint: 'provider.hints.main_contact',
    inverse: null
  }),
  public_contact: DS.belongsTo('contact-information', {
    autocomplete: true,
    type: 'select',
    label: 'provider.fields.public_contact',
    hint: 'provider.hints.public_contact',
    inverse: null
  }),
  // other information
  epp_oth_participating_countries: DS.attr({
    defaultValue: 'Europe (EO)',
    label: 'provider.fields.epp_oth_participating_countries',
    hint: 'provider.hints.epp_oth_participating_countries',
    formComponent: 'agora-chips',
    formAttrs: {
      options: countries,
      exactMatch: true,
    }
  }),
  epp_oth_affiliations: DS.hasMany('affiliation', {
    label: 'provider.fields.epp_oth_affiliations',
    hint: 'provider.hints.epp_oth_affiliations',
  }),
  epp_oth_affiliations_verbose: DS.attr({
    label: 'provider.fields.affiliation_names',
  }),
  epp_oth_networks: DS.hasMany('network', {
    label: 'provider.fields.epp_oth_networks',
    hint: 'provider.hints.epp_oth_networks',
  }),
  epp_oth_networks_verbose: DS.attr({
    label: 'provider.fields.network_names',
  }),
  epp_oth_esfri_domain: DS.hasMany('esfridomain', {
    label: 'provider.fields.epp_oth_esfri_domain',
    hint: 'provider.hints.epp_oth_esfri_domain',
  }),
  epp_oth_esfri_domain_verbose: DS.attr({
    label: 'provider.fields.esfridomain_names',
  }),
  epp_oth_esfri_type: DS.belongsTo('esfritype', {
    autocomplete: true,
    type: 'select',
    label: 'provider.fields.epp_oth_esfri_type',
    hint: 'provider.hints.epp_oth_esfri_type',
    inverse: null,
    formAttrs: {
      optionLabelAttr: 'name',
    },
  }),
  epp_oth_meril_scientific_domain: DS.hasMany('merildomain', {
    label: 'provider.fields.epp_oth_meril_scientific_domain',
    hint: 'provider.hints.epp_oth_meril_scientific_domain',
  }),
  epp_oth_meril_scientific_domain_verbose: DS.attr({
    label: 'provider.fields.merildomain_names',
  }),
  // TODO: Filter meril subdomain's ManyArray results according to domain selections
  epp_oth_meril_scientific_subdomain: DS.hasMany('merilsubdomain', {
    label: 'provider.fields.epp_oth_meril_scientific_subdomain',
    hint: 'provider.hints.epp_oth_meril_scientific_subdomain',
  }),
  epp_oth_meril_scientific_subdomain_verbose: DS.attr({
    label: 'provider.fields.merilsubdomain_names',
  }),
  epp_oth_areas_of_activity: DS.hasMany('activity', {
    label: 'provider.fields.epp_oth_areas_of_activity',
    hint: 'provider.hints.epp_oth_areas_of_activity',
  }),
  epp_oth_areas_of_activity_verbose: DS.attr({
    label: 'provider.fields.activity_names',
  }),
  epp_oth_societal_grand_challenges: DS.hasMany('challenge', {
    label: 'provider.fields.epp_oth_societal_grand_challenges',
    hint: 'provider.hints.epp_oth_societal_grand_challenges',
  }),
  epp_oth_societal_grand_challenges_verbose: DS.attr({
    label: 'provider.fields.challenge_names',
  }),
  epp_oth_national_roadmaps: DS.attr({
    label: 'provider.fields.epp_oth_national_roadmaps',
    hint: 'provider.hints.epp_oth_national_roadmaps',
  }),

  eosc_id: DS.attr(),
  eosc_state: DS.attr({
    autocomplete: true,
    type: 'select',
    choices: CHOICES.EOSC_STATE_PROVIDERS,
  }),

  state: DS.attr({
    type: 'select',
    choices: CHOICES.PROVIDER_STATES,
    defaultValue: 'draft',
    label: 'provider.fields.state',
  }),

  state_verbose: computed('state', function() {
    let state = get(this, 'state');
    return capitalize(state);
  }),

  __api__: {
    serialize: function(hash, _) {
      // do not send readonly keys to backend
      delete hash['epp_oth_affiliations_verbose'];
      delete hash['epp_oth_networks_verbose'];
      delete hash['epp_cli_structure_type_verbose'];
      delete hash['epp_oth_esfri_domain_verbose'];
      delete hash['epp_oth_areas_of_activity_verbose'];
      delete hash['epp_oth_societal_grand_challenges_verbose'];
      delete hash['epp_cli_scientific_domain_verbose'];
      delete hash['epp_cli_scientific_subdomain_verbose'];
      delete hash['epp_oth_meril_scientific_domain_verbose'];
      delete hash['epp_oth_meril_scientific_subdomain_verbose'];
      return hash;
    },
  },




});
