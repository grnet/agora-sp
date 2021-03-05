import gen from 'ember-gen/lib/gen';

export default gen.GenRoutedObject.extend({
  name: 'privacy-policy',
  resourceName: '',
  templateName: 'layout-toolbar',
  path: 'privacy-policy',
  page: {
    title: 'privacy_policy.page.title',
  },
  menu: {
    display: false,
  },
  content: 'privacy-content',
});
