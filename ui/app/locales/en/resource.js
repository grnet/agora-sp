const resource = {
  cards: {
    basic_information: 'Basic information',
    basic_hint: '',
  },
  fields: {
    rd_bai_0_id: 'RD.BAI.0 - ID',
    rd_bai_1_name: 'RD.BAI.1 - Name',
    rd_bai_2_service_organisation: 'RD.BAI.2 - Service Organisation',
    rd_bai_3_service_providers: 'RD.BAI.3 - Service Providers',
    rd_bai_4_webpage: 'RD.BAI.4 - Webpage',
    providers_names: 'RD.BAI.3 - Service Providers',
    rd_mri_1_description: 'RD.MRI.1 - Description',
    rd_mri_2_tagline: 'RD.MRI.2 - Tagline',
    rd_mri_3_logo: 'RD.MRI.3 - Logo',
    rd_mri_4_mulitimedia: 'RD.MRI.4 - Mulitimedia',
    rd_mri_5_target_users: 'RD.MRI.5 - Target Users',
    rd_mri_6_target_customer_tags: 'RD.MRI.6 - Customer Tags',
    rd_mri_7_use_cases: 'RD.MRI.7 - Use Cases/Case Studies',
  },
  hints: {
    rd_bai_0_id: 'Global unique and persistent identifier of the resource. The first part denotes the Resource Provider and the second part the unique identifier of the resource.<br />Example: openaire.foo',
    rd_bai_1_name: 'Brief and descriptive name of resource',
    rd_bai_2_service_organisation: 'The organisation that manages and delivers the resource, or the organisation which takes lead in coordinating resource delivery and communicates with customers in case of a federated scenario',
    rd_bai_3_service_providers: 'The organisation(s) that participate in resource delivery in case of a federated scenario',
    rd_bai_4_webpage: 'Webpage with information about the resource',
    rd_mri_1_description: '',
    rd_mri_2_tagline: '',
    rd_mri_3_logo: 'Provide URL of the resource, which must be in https, in the form of the shortest possible alias',
    rd_mri_4_mulitimedia: 'Link to video, screenshots or slides showing details of the resource.',
    rd_mri_6_target_customer_tags: 'This field will be used in the search function to prioritise results.<br/>Hit ENTER to register your tag.',
    rd_mri_5_target_users: '',
    rd_mri_7_use_cases: 'Provide either descriptive text or URL of the webpage describing the use case, or both',
  },
  table: {
    rd_bai_0_id: 'ID',
    rd_bai_1_name: 'Name',
    rd_bai_2_service_organisation: 'Organisation',
  },
  placeholders: {
    search: 'Search by ID or Name',
  },
  menu: 'Resources',
};

export { resource }
