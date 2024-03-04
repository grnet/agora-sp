// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

const copyrightMessage = `
<p xmlns:cc="http://creativecommons.org/ns#">
   This work by
   <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.grnet.gr">
      National Infrastructures for Research and Technology - GRNET S.A.</a> is licensed under
   <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank"
      rel="license noopener noreferrer" style="display:inline-block;">
      CC BY 4.0
      <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"
         src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1">
      <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"
         src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">
   </a>
</p>
`

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AGORA-SP Documentation',
  tagline: 'Learn how the service protofolio management tool works',
  url: 'https://grnet.github.io',
  baseUrl: '/agora-sp/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'GRNET', // Usually your GitHub org/user name.
  projectName: 'agora-sp', // Usually your repo name.

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl:
          //   'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
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
        style: 'light',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Explore AGORA Docs',
                to: 'docs/',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Github',
                href: 'https://github.com/GRNET/agora-sp',
              }
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Github',
                href: 'https://github.com/GRNET/agora-sp',
              }
            ],
          },
        ],
        copyright: copyrightMessage,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
    themes: [
      [
        "@easyops-cn/docusaurus-search-local",
        {
          hashed: true,
          language: ["en", "zh"],
          highlightSearchTermsOnTargetPage: true,
          explicitSearchResultPath: true,
          indexBlog: false,
        },
      ],
    ],
};

module.exports = config;
