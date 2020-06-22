// UNUSED
import Ember from 'ember';
import gen from 'ember-gen/lib/gen';


let policy = gen.GenRoutedObject.extend({
  auth: null,
  name: 'policy',
  resourceName: '',
  templateName: 'policy',
  path: 'policy',
  menu: {
    display: false,
  },
});

export default gen.GenRoutedObject.extend({
  name: 'policy',
  gens: { policy },
})
