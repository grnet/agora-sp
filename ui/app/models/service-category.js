import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr(),
  icon: DS.attr(),
  description: DS.attr(),
  icon_filename: Ember.computed('icon', function(){
    return this.get('icon').split('/').pop();
  })
});
