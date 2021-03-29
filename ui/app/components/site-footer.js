import Ember from "ember";
import ENV from "../config/environment";


const { get, set, computed } = Ember;

export default Ember.Component.extend({
  tagName: "footer",
  classNames: ["layout-align-end"],
  cookies_policy: ENV.APP.footer["cookies_policy"],
  cookies_text: ENV.APP.footer["cookies_title"],
  privacy_policy: ENV.APP.footer["privacy_policy"],
  privacy_text: ENV.APP.footer["privacy_title"],
  access_policy: ENV.APP.footer["access_policy"],
  terms: ENV.APP.footer["terms"],

  logos: computed("", function () {
    let logos = ENV.APP.footer.logos || [];
    let images = "";

    for (var logo of logos) {
      let img = `<img src="${logo["url"]}" alt="${logo["alt"]}" />`;

      images = images + img;
    }

    return images;
  }),

  version_contact: computed("", function () {
    let contact = ENV.APP.footer.contact;
    let version = ENV.APP.version;

    if (contact) {
      return `<span>v${version} | ${contact}</span>`;
    } else {
      return `<span>v${version}</span>`;
    }
  }),

  info: computed("", function () {
    let info = ENV.APP.footer.info;

    if (info) {
      return `<span>${info}</span>`;
    }
  }),
  copyright: computed("", function () {
    let copyright_years = ENV.APP.footer.copyright_years;

    if (copyright_years) {
      return `<span>Copyright © ${copyright_years}</span> `;
    }
  }),

  // Dialog
  dialogVisible: false,
  dialogTitle: null,
  dialogContent: null,

  actions: {
    openDialog(type) {
      set(this, "dialogVisible", true);
      let title, content;
      if (type === 'cookies') {
        title = get(this, 'cookies_text');
        content = 'cookies-content';
      }
      if (type === 'privacy') {
        title = get(this, 'privacy_text');
        content = 'privacy-content';
      }
      set(this, "dialogTitle", title);
      set(this, "dialogContent", content);
    },
    closeDialog() {
      set(this, "dialogVisible", false);
      set(this, "dialogTitle", null);
      set(this, "dialogContent", null);
    }
  }
});
