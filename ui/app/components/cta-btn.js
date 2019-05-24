import Ember from 'ember';

export default Ember.Component.extend({
  init: function() {
    this._super(...arguments);
    const clsNames = Ember.get(this, 'fattrs.classNames');
    const concatCLS = this.classNames.concat(clsNames);
    this.set('classNames', concatCLS);
  },
});
