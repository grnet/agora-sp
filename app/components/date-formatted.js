import Ember from 'ember';
import moment from 'moment';

const { get, computed } = Ember;

export default Ember.Component.extend({
  date: computed('value', function() {
    var raw_date = get(this, 'value');
    if (raw_date) {
      return moment(raw_date).format('dddd, D MMMM, YYYY');
    } else {
      return '-';
    }
  }),
});
