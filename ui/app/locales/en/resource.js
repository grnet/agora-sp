import { EOSC_HINT } from '../../lib/common';
const HOW_ADD_NEW = '<br />Hit <strong>ENTER</strong>  to add a new entry.';
const SEPARATOR = 'New line';

const resource = {
  cards: {
    basic: 'Basic information',
    basic_hint: '',
    marketing: 'Marketing Information',
    geo: 'Geographical and Language Availability Information',
    location: 'Resource Location Information',
    contact: 'Contact Information',
    main_contact: 'Main Contact/Resource Owner',
    public_contact: 'Public Contact',
    other_contact: 'Other Contacts',
    management_information: 'Management Information',
    classification: 'Classification Information',
    classification_hint: '',
    financial: 'Financial Information',
    dependencies: 'Dependencies Information',
    access_order: 'Access and Order Information',
    attribution: 'Attribution Information',
    maturity: 'Maturity Information',
  },
  fields: {
    erp_bai_id: 'ERP.BAI.0 - ID',
    'erp_bai_id.required': 'ERP.BAI.0 - ID *',
    erp_bai_abbreviation: 'ERP.BAI.1 - Abbreviation',
    'erp_bai_abbreviation.required': 'ERP.BAI.1 - Abbreviation *',
    erp_bai_name: 'ERP.BAI.2 - Name',
    'erp_bai_name.required': 'ERP.BAI.2 - Name *',
    erp_bai_service_organisation: 'ERP.BAI.3 - Resource Organisation',
    'erp_bai_service_organisation.required': 'ERP.BAI.3 - Resource Organisation *',
    erp_bai_service_providers: 'ERP.BAI.4 - Resource Providers',
    erp_bai_webpage: 'ERP.BAI.5 - Webpage',
    providers_names: 'ERP.BAI.3 - Service Providers',
    erp_mri_1_description: 'ERP.MRI.1 - Description',
    erp_mri_2_tagline: 'ERP.MRI.2 - Tagline',
    erp_mri_3_logo: 'ERP.MRI.3 - Logo',
    erp_mri_4_multimedia: 'ERP.MRI.4 - Multimedia',
    erp_mri_6_target_customer_tags: 'ERP.MRI.6 - Customer Tags',
    erp_mri_5_use_cases: 'ERP.MRI.5 - Use Cases',
    erp_cli_1_scientific_domain: 'ERP.CLI.1 - Scientific Domain',
    'erp_cli_1_scientific_domain.required': 'ERP.CLI.1 - Scientific Domain *',
    erp_cli_2_scientific_subdomain: 'ERP.CLI.2 - Scientific Subdomain',
    'erp_cli_2_scientific_subdomain.required': 'ERP.CLI.2 - Scientific Subdomain *',
    erp_cli_3_category: 'ERP.CLI.3 - Category',
    'erp_cli_3_category.required': 'ERP.CLI.3 - Category *',
    erp_cli_4_subcategory: 'ERP.CLI.4 - Subcategory',
    'erp_cli_4_subcategory.required': 'ERP.CLI.4 - Subcategory *',
    erp_cli_5_target_users: 'ERP.CLI.5 - Target Users',
    erp_cli_6_access_type: 'ERP.CLI.6 - Access Type',
    erp_cli_7_access_mode: 'ERP.CLI.7 - Access Mode',
    erp_cli_8_tags: 'ERP.CLI.8 - Tags',
    erp_mgi_1_helpdesk_webpage: 'ERP.MGI.1 - Helpdesk Page',
    erp_mgi_2_user_manual: 'ERP.MGI.2 - User Manual',
    erp_mgi_3_terms_of_use: 'ERP.MGI.3 - Terms of Use',
    erp_mgi_4_privacy_policy: 'ERP.MGI.4 - Privacy Policy',
    erp_mgi_5_access_policy: 'ERP.MGI.5 - Access Policy',
    erp_mgi_6_sla_specification: 'ERP.MGI.6 - Resource Level',
    erp_mgi_7_training_information: 'ERP.MGI.7 - Training Information',
    erp_mgi_8_status_monitoring: 'ERP.MGI.8 - Status Monitoring',
    erp_mgi_9_maintenance: 'ERP.MGI.9 - Maintenance',
    erp_gla_1_geographical_availability: 'ERP.GLA.1 - Geographical Availability',
    erp_gla_2_language: 'ERP.GLA.2 - Language Availability',
    erp_rli_1_geographic_location: 'ERP.RLI.1 - Resource Geographic Location',
    erp_aoi_1_order_type: 'ERP.AOI.1 - Order Type',
    erp_aoi_2_order: 'ERP.AOI.2 - Order',
    erp_fni_1_payment_model: 'ERP.FNI.1 - Payment Model',
    erp_fni_2_pricing: 'ERP.FNI.2 - Pricing',
    main_contact: 'Main Contact/Resource Owner',
    public_contact: 'Public Contact',
    erp_mti_1_technology_readiness_level: 'ERP.MTI.1 - Technology Readinness Level',
    erp_mti_2_life_cycle_status: 'ERP.MTI.2 - Life Cycle Status',
    erp_mti_3_certifications: 'ERP.MTI.3 - Certifications',
    erp_mti_4_standards: 'ERP.MTI.4 - Standards',
    erp_mti_5_open_source_technologies: 'ERP.MTI.5 - Open Source Technologies',
    erp_mti_6_version: 'ERP.MTI.6 - Version',
    erp_mti_7_last_update: 'ERP.MTI.7 - Last Update',
    erp_mti_8_changelog: 'ERP.MTI.8 - Changelog',
    erp_dei_1_required_resources: 'ERP.DEI.1 - Required Resources',
    erp_dei_2_related_resources: 'ERP.DEI.2 - Related Resources',
    erp_dei_3_related_platforms: 'ERP.DEI.3 - Related Platforms',
    erp_coi_13_helpdesk_email: 'ERP.COI.13 - Helpdesk Email',
    erp_coi_14_security_contact_email: 'ERP.COI.14 - Security Contact Email',
    erp_ati_1_funding_body: 'ERP.ATI.1 - Funding Body',
    erp_ati_2_funding_program: 'ERP.ATI.2 - Funding Program',
    erp_ati_3_grant_project_name: 'ERP.ATI.3 - Grant/Project Name',
    mc_first_name: 'ERP.COI.1 - First Name',
    mc_last_name: 'ERP.COI.2 - Last Name',
    mc_email: 'ERP.COI.3 - Email',
    mc_phone: 'ERP.COI.4 - Phone',
    mc_position: 'ERP.COI.5 - Position',
    mc_organisation: 'ERP.COI.6 - Organisation',
    pc_first_name: 'ERP.COI.7 - First Name',
    pc_last_name: 'ERP.COI.8 - Last Name',
    pc_email: 'ERP.COI.9 - Email',
    pc_phone: 'ERP.COI.10 - Phone',
    pc_position: 'ERP.COI.11 - Position',
    pc_organisation: 'ERP.COI.12 - Organisation',
    state: 'State',
  },
  hints: {
    erp_bai_id: 'Global <strong>unique and persistent</strong> reference to the Resource . The first part denotes the Resource Provider and the second part the unique identifier of the resource.<br />Example: openaire.foo',
    erp_bai_abbreviation:   `${EOSC_HINT}Abbreviation or Short name of the Resource`,
    erp_bai_name: `${EOSC_HINT}<strong>Unique</strong>, brief and descriptive name of Resource as assigned by the Provider.`,
    erp_bai_service_organisation: `${EOSC_HINT}The name (or abbreviation) of the organisation that manages or delivers the Resource, or that coordinates resource delivery in a federated scenario.`,
    erp_bai_service_providers: 'The name(s) (or abbreviation(s)) of Provider(s) that manage or deliver the Resource in federated scenarios.',
    erp_bai_webpage: `${EOSC_HINT}Webpage with information about the Resource usually hosted and maintained by the Provider.`,
    erp_mri_1_description: EOSC_HINT,
    erp_mri_2_tagline: `${EOSC_HINT}Short catch-phrase for marketing and advertising purposes.`,
    erp_mri_3_logo: `${EOSC_HINT}Link to the logo/visual identity of the Resource. The logo will be visible at the Portal.`,
    erp_mri_4_multimedia: 'Link to video, screenshots or slides showing details of the Resource.',
    erp_mri_5_use_cases: 'Link to use cases supported by this Resource.',
    erp_cli_1_scientific_domain: `${EOSC_HINT}The branch of science, scientific discipline that is related to the service/resource.`,
    erp_cli_2_scientific_subdomain: `${EOSC_HINT}The subbranch of science, scientific subdicipline that is related to the service/resource.`,
    erp_cli_3_category: `${EOSC_HINT}A named group of services/resources that offer access to the same type of resource or capabilities.`,
    erp_cli_4_subcategory: `${EOSC_HINT}A named group of services/resources that offer access to the same type of resource or capabilities, within the defined service category`,
    erp_cli_5_target_users: EOSC_HINT,
    erp_cli_6_access_type: 'The way a user can access the Resource (Remote, Physical, Virtual, etc.)',
    erp_cli_7_access_mode: 'Eligibility/criteria for granting access to users (excellence-based, free-conditionally, free etc.)',
    erp_cli_8_tags: '<strong>Comma separated</strong> keywords associated to the service/resource to simplify search by relevant keywords.',
    erp_mgi_1_helpdesk_webpage: 'The URL to a webpage to ask more information from the Provider about this Resource.',
    erp_mgi_2_user_manual: `${EOSC_HINT}Link to the Resource user manual and documentation.`,
    erp_mgi_3_terms_of_use: `${EOSC_HINT}Webpage describing the rules, Resource conditions and usage policy which one must agree to abide by in order to use the Resource.`,
    erp_mgi_4_privacy_policy: `${EOSC_HINT}Link to the privacy policy applicable to the Resource.`,
    erp_mgi_5_access_policy: 'Information about the access policies that apply.',
    erp_mgi_6_sla_specification: 'Webpage with the information about the levels of performance that a Provider is expected to deliver.',
    erp_mgi_7_training_information: 'Webpage to training information on the Resource.',
    erp_mgi_8_status_monitoring: 'Webpage with monitoring information about this Resource.',
    erp_mgi_9_maintenance: 'Webpage with information about planned maintenance windows for this Resource.',
    erp_gla_1_geographical_availability: `${EOSC_HINT}The countries in which your service is available to the users.<br>If the service is European-wide, please list "Europe".If the service is universal, please list "World".`,
    erp_gla_2_language: `${EOSC_HINT}Add the language codes using the <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" target="_blank">2-letter codes from the ISO</a>.`,
    erp_rli_1_geographic_location: 'List of geographic locations where data is stored and processed.',
    main_contact: `${EOSC_HINT}This info will not be publicly exposed`,
    public_contact: `${EOSC_HINT}This info will be exposed to public API`,
    erp_mti_1_technology_readiness_level: `${EOSC_HINT}The Technology Readiness Level of the Resource uodated in the context of the EOSC.`,
    erp_mti_2_life_cycle_status: 'Phase of the Resource life-cycle.',
    erp_mti_3_certifications: `<strong>${SEPARATOR}</strong> separated list of certifications obtained for the Resource (including the certification body).${HOW_ADD_NEW}`,
    erp_mti_4_standards: `<strong>${SEPARATOR}</strong> separated list of standards supported by the Resource.${HOW_ADD_NEW}`,
    erp_mti_5_open_source_technologies: `<strong>${SEPARATOR}</strong> separated list of open source technologies supported by the Resource.${HOW_ADD_NEW}`,
    erp_mti_6_version: 'Version of the Resource that is in force.',
    erp_mti_7_last_update: 'Date of the latest update of the Resource.',
    erp_mti_8_changelog: `<strong>${SEPARATOR}</strong> separated list of the summary of the Resource features updated from the previous version.${HOW_ADD_NEW}`,
    erp_dei_1_required_resources: 'List of other Resources required to use this Resource.',
    erp_dei_2_related_resources: 'List of other Resources that are commonly used with this Resource.',
    erp_dei_3_related_platforms: '<strong>Comma separated</strong> list of suites or thematic platforms in which the Resource is engaged or Providers (Provider groups) contributing to this Resource.',
    erp_ati_1_funding_body: 'Name of the funding body that supported the development and/or operation of the Resource.',
    erp_ati_2_funding_program: 'Name of the funding program that supported the development and/or operation of the Resource.',
    erp_ati_3_grant_project_name: 'Name of the project that supported the development and/or operation of the Resource.',
    erp_coi_13_helpdesk_email: EOSC_HINT,
    erp_coi_14_security_contact_email: EOSC_HINT,
    erp_aoi_1_order_type: `${EOSC_HINT}Information on the order type (requires an ordering procedure, or no ordering and if fully open or requires authentication)`,
    erp_aoi_2_order: 'Webpage through which an order for the Resource can be placed',
    erp_fni_1_payment_model: 'Webpage with the supported payment models and restrictions that apply to each of them.',
    erp_fni_2_pricing: 'Webpage with the information on the price scheme for this Resource in case the customer is charged for.',
  },
  table: {
    erp_bai_id: 'ID',
    erp_bai_name: 'Name',
    erp_bai_service_organisation: 'Organisation',
    erp_mti_1_technology_readiness_level: 'TRL',
    state_verbose: 'State',
  },
  placeholders: {
    search: 'Search by ID or name',
  },
  menu: 'Resources',
  my_menu: 'My Resources',
  publish: {
    label: 'Publish',
    title: 'Publish Resource',
    ok: 'Publish',
    message: 'When you publish a Resource, its non sensitive data are displayed in resources public api.',
    success: 'Success',
    error: 'Error in publishing resource details'
  },
  unpublish: {
    label: 'Unpublish',
    title: 'Unpublish Resource',
    ok: 'Unpublish',
    message: 'When you unpublish a Resource, its non sensitive data are no longer displayed in resources public api.',
    success: 'Success',
    error: 'Error in publishing resource details'
  }
};

export { resource }
