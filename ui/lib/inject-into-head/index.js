/*jshint node:true*/

module.exports = {
  name: 'inject-into-head',
  contentFor: function(type, config) {
    const title = config.title || 'Agora Admin';
    if (type === 'head') {
      return `<title>${title}</title>`;
    }
  },

};
