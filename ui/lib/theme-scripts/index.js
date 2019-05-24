/* jshint node: true */

module.exports = {
  name: 'theme-scripts',
  contentFor: function(type, config) {
    if (type === 'head-footer' && config.theme) {
      return `<link rel="stylesheet" href="${config.rootURL}assets/${ config.theme }.css">`;
    }
  },
};
