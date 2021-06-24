import ENV from 'agora-admin/config/environment';

const EOSC_PORTAL_API = ENV.APP.eosc_portal.api_docs_url;
const ROOT_URL = ENV.rootURL;

export const eosc = {
  resource: {
    post: {
      title: 'Publish to EOSC Portal',
      label: 'Publish to EOSC Portal',
      ok: 'Publish',
      message: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>This action will publish the resource to <strong>${EOSC_PORTAL_API}</strong>.<br />Are you sure you want to continue?</p></div>`,
      message_missing: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>In order to publish the resource to <strong>${EOSC_PORTAL_API}</strong>,<br /> you need to fill the following fields:</p>{{{list_missing}}}</div>`,
      error: 'The action could not be successfully performed',
      success: 'The resource has been successfully published to EOSC Portal',
    },
    put: {
      title: 'Update Resource published to EOSC Portal',
      label: 'Update Resource to EOSC Portal',
      ok: 'Update',
      message: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>This action will update the resource published to <strong>${EOSC_PORTAL_API}</strong>.<br />Are you sure you want to continue?</p></div>`,
      message_missing: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>In order to update the resource published to <strong>${EOSC_PORTAL_API}</strong>,<br /> you need to fill the following fields:</p>{{{list_missing}}}</div>`,
      error: 'The action could not be successfully performed',
      success: 'The resource has been successfully updated to EOSC Portal',
    },
  },
  provider: {
    post: {
      title: 'Publish to EOSC Portal',
      label: 'Publish to EOSC Portal',
      ok: 'Publish',
      message: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>This action will publish the provider to <strong>${EOSC_PORTAL_API}</strong>.<br />Are you sure you want to continue?</p></div>`,
      message_missing: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>In order to publish the provider to <strong>${EOSC_PORTAL_API}</strong>,<br /> you need to fill the following fields:</p>{{{list_missing}}}</div>`,
      error: 'The action could not be successfully performed',
      success: 'The provider has been successfully published to EOSC Portal',
    },
    put: {
      title: 'Update Provider published to EOSC Portal',
      label: 'Update Provider to EOSC Portal',
      ok: 'Update',
      message: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>This action will update the provider published to <strong>${EOSC_PORTAL_API}</strong>.<br />Are you sure you want to continue?</p></div>`,
      message_missing: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>In order to update the provider published to <strong>${EOSC_PORTAL_API}</strong>,<br /> you need to fill the following fields:</p>{{{list_missing}}}</div>`,
      error: 'The action could not be successfully performed',
      success: 'The provider has been successfully updated to EOSC Portal',
    },
    approve: {
      title: 'Approve Provider for EOSC Portal',
      label: 'Approve Provider for EOSC Portal',
      ok: 'Approve',
      message: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>This action will approve the provider for <strong>${EOSC_PORTAL_API}</strong>.<p>Please note that the approved Provider will be set to state <i>"pending template submission"</i> until<br /> you have approved at least one Resource beloning to this Provider.</p><p>Are you sure you want to continue?</p></div>`,
      message_resource: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>This action will approve the provider for <strong>${EOSC_PORTAL_API}</strong>.<p>Please note that the Provider will be approved only if there is one resource published.</p><p>Are you sure you want to continue?</p></div>`,
      error: 'The action could not be successfully performed',
      success: 'The provider has been successfully approved for EOSC Portal',
    },
    reject: {
      title: 'Reject Provider for EOSC Portal',
      label: 'Reject Provider for EOSC Portal',
      ok: 'Reject',
      message: `<div class="eosc-portal-modal"><img src="${ROOT_URL}assets/logo-eosc-portal.png" /><p>This action will reject the provider for <strong>${EOSC_PORTAL_API}</strong>.<p>Please note that the approved Provider will be set to state <i>"pending initial approval"</i> until<br /> it is finally approved.</p><p>Are you sure you want to continue?</p></div>`,
      error: 'The action could not be successfully performed',
      success: 'The provider has been successfully rejected for EOSC Portal',
    },
  },
};
