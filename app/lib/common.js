import { CRUDGen } from 'ember-gen/lib/gen';


const AgoraGen = CRUDGen.extend({
  auth: true,
  list: {
    layout: 'table',
    paginate: {
      limits: [ 10, 50, 100 ],
      serverSide: false,
      active: true
    }
  }

});

export {
  AgoraGen
};
