import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr(),
  __api__: {
    path: 'my-providers',
  }

});
