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
  },
  hints: {
    rd_bai_0_id: 'Global unique and persistent identifier of the resource. The first part denotes the Resource Provider and the second part the unique identifier of the resource.<br />Example: openaire.foo',
    rd_bai_1_name: 'Brief and descriptive name of resource',
    rd_bai_2_service_organisation: 'The organisation that manages and delivers the resource, or the organisation which takes lead in coordinating resource delivery and communicates with customers in case of a federated scenario',
    rd_bai_3_service_providers: 'The organisation(s) that participate in resource delivery in case of a federated scenario',
    rd_bai_4_webpage: 'Webpage with information about the resource',
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

export { resource };
