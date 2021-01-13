module.exports = {
  title: 'AGORA-SP Documentation',
  tagline: 'Learn how the service protofolio management tool works',
  url: 'https://grnet.github.io',
  baseUrl: '/agora-sp/',
  onBrokenLinks: 'throw',
  favicon: 'img/favicon.ico',
  organizationName: 'GRNET', // Usually your GitHub org/user name.
  projectName: 'agora-sp', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'AGORA-SP',
      logo: {
        alt: 'agora-sp logo',
        src: 'img/agora.png',
      },
      items: [
        {
          to: 'docs/',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        {
          href: 'https://github.com/GRNET/agora-sp',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: ' ',
          items: [
            {
              label: ' ',
              to: 'docs/',
            },
          ],
        },
        {
          title: ' ',
          items: [
            {
              label: ' ',
              href: 'https://github.com/GRNET/agora-sp',
            }
          ],
        },
        {
          title: ' ',
          items: [
            {
              label: ' ',
              href: 'https://github.com/GRNET/agora-sp',
            },
          ],
        },
      ],
      copyright: `<img alt="grnet" src="/img/grnet-logo.png" height="50px"> </a> <br /> Copyright © ${new Date().getFullYear()} <a href="http://www.grnet.gr/"> GRNET </a>`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          // It is recommended to set document id as docs home page (`docs/` path).
          homePageId: 'authenticate',
          sidebarPath: require.resolve('./sidebars.js'),
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
