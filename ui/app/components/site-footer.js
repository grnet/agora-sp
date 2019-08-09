import Ember from 'ember';
import ENV from '../config/environment';

const {
  computed,
} = Ember;

export default Ember.Component.extend({
  tagName: 'footer',
  classNames: ['flex', 'layout-column', 'layout-align-end'],
  policy_url: ENV.APP.footer['policy_url'],
  policy_text: ENV.APP.footer['policy_text'],

  logos: computed('', function(){
    let logos = ENV.APP.footer.logos || [];
    let images = '';

    for (var logo of logos) {
      let img = `<img src="${logo['url']}" alt="${logo['alt']}" />`;

      images = images + img;
    }

    return images;
  }),

  version_contact: computed('', function(){
    let contact = ENV.APP.footer.contact;
    let version = ENV.APP.version;

    if (contact) {
      return `<span>v${version} | ${contact}</span>`;
    } else {
      return `<span>v${version}</span>`;
    }
  }),

  info: computed('', function() {
    let info = ENV.APP.footer.info;

    if (info) {
      return `<span>${info}</span>`;
    }
  }),
  copyright: computed('', function(){
    let copyright_years = ENV.APP.footer.copyright_years;

    if (copyright_years) {
      return `<span>Copyright © ${copyright_years}</span> `;
    }
  }),
});
