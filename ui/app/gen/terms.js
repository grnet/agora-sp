import gen from 'ember-gen/lib/gen';

export default gen.GenRoutedObject.extend({
  name: 'terms',
  resourceName: '',
  templateName: 'layout-toolbar',
  path: 'terms-of-use',
  page: {
    title: 'terms.page.title',
  },
  menu: {
    display: false,
  },
  content: 'terms-content',
});
