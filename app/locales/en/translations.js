import { service_trl } from './service_trl';
import { service_item } from './service_item';
import { service_version } from './service_version';
import { service_owner } from './service_owner';
import { service_status } from './service_status';
import { service_area } from './service_area';
import { contact_information } from './contact_information';
import { component } from './component';
import { component_implementation } from './component_implementation';
import { component_implementation_detail } from './component_implementation_detail';
import { cidl } from './component_implementation_detail_link';
import { custom_user } from './custom_user';
import { common } from './common';
import { login } from './login';

export default {
  'service_item': service_item,
  'service_trl': service_trl,
  'service_version': service_version,
  'service_owner': service_owner,
  'service_status': service_status,
  'service_area': service_area,
  'contact_information': contact_information,
  'component': component,
  'component_implementation': component_implementation,
  'component_implementation_detail': component_implementation_detail,
  'cidl': cidl,
  'file': common.file,
  'message': common.message,
  'custom_user': custom_user,
  'form': common.form,
  'login': login,
};

