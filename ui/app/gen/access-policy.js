import gen from 'ember-gen/lib/gen';

export default gen.GenRoutedObject.extend({
  name: 'access-policy',
  resourceName: '',
  templateName: 'layout-toolbar',
  path: 'access-policy',
  page: {
    title: 'access_policy.page.title',
  },
  menu: {
    display: false,
  },
  content: 'access-policy-content',
});
