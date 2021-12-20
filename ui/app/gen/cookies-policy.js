import gen from 'ember-gen/lib/gen';

export default gen.GenRoutedObject.extend({
  name: 'cookies-policy',
  resourceName: '',
  templateName: 'layout-toolbar',
  path: 'cookies-policy',
  page: {
    title: 'cookies_policy.page.title',
  },
  menu: {
    display: false,
  },
  content: 'cookies-content',
});
