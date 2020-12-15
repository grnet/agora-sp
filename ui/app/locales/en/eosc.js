import ENV from 'agora-admin/config/environment';

const EOSC_PORTAL_API = ENV.APP.eosc_portal.api;

export const eosc = {
  resource: {
    post: {
      title: 'Publish to EOSC Portal',
      ok: 'Publish',
      message: `<div class="eosc-portal-modal"><img src="./assets/logo-eosc-portal.png" /><p>This action will publish the resource to <strong>${EOSC_PORTAL_API}</strong>.<br />Are you sure you want to continue?</p></div>`,
    },
    put: {
      title: 'Update Resource published to EOSC Portal',
      ok: 'Update',
      message: `<div class="eosc-portal-modal"><img src="./assets/logo-eosc-portal.png" /><p>This action will update the resource published to <strong>${EOSC_PORTAL_API}</strong>.<br />Are you sure you want to continue?</p></div>`,
    }
  },
};
