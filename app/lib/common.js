//import Ember from 'ember';
import { CRUDGen } from 'ember-gen/lib/gen';


//const {
//    computed: { reads },
//} = Ember;

const AgoraGen = CRUDGen.extend({
  auth: true
});

export {
  AgoraGen
};
