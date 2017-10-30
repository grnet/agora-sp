import { AgoraGen } from '../lib/common';

export default AgoraGen.extend({
  modelName: 'contact-information',
  path: 'contact-information',
  resourceName: 'api/v2/contact-information',
  list: {
    layout: 'table',
    page: {
      title: 'Contact Information'
    },
    menu: {
      label: 'Contact Information',
      group: 'user-information'
    },
  }
});
