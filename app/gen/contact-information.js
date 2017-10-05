import gen from 'ember-gen/lib/gen';

export default gen.CRUDGen.extend({
  modelName: 'contact-information',
  auth: true,
  path: 'contact-information',
  resourceName: 'contact-information',
  list: {
    layout: 'table',
    page: {
      title: 'Contact Information'
    },
    menu: {
      label: 'Contact Information'
    },
  }
});
