import { service_trl } from './service_trl';
import { service_item } from './service_item';
import { service_version } from './service_version';
import { service_admin } from './service_admin';
import { service_status } from './service_status';
import { service_category } from './service_category';
import { component } from './component';
import { component_implementation } from './component_implementation';
import { component_implementation_detail } from './component_implementation_detail';
import { cidl } from './component_implementation_detail_link';
import { custom_user } from './custom_user';
import { user_role } from './user_role';
import { user_customer } from './user_customer';
import { institution } from './institution';
import { provider } from './provider';
import { access_policy } from './access_policy';
import { federation_member } from './federation_member';
import { common } from './common';
import { login } from './login';
import { profile } from './profile';
import { policy } from './policy';
import { resource } from './resource';
import { target_user } from './target_user';
import { contact_information } from './contact_information';
import { resource_admin } from './resource_admin';

export default {
  'service_item': service_item,
  'service_trl': service_trl,
  'service_version': service_version,
  'service_admin': service_admin,
  'service_status': service_status,
  'service_category': service_category,
  'component': component,
  'component_implementation': component_implementation,
  'component_implementation_detail': component_implementation_detail,
  'cidl': cidl,
  'file': common.file,
  'message': common.message,
  'custom_user': custom_user,
  'user_role': user_role,
  'user_customer': user_customer,
  'institution': institution,
  'provider': provider,
  'federation_member': federation_member,
  'access_policy': access_policy,
  'form': common.form,
  'login': login,
  'network': network,
  'group_menu': common.group_menu,
  'confirm': common.confirm,
  'Service_type should be unique': cidl.errors.service_type_unique,
  'list': common.list,
  'select': common.select,
  'row': common.row,
  'common': common,
  'profile': profile,
  'policy': policy,
  resource,
  target_user,
  contact_information,
  'Service Admin': 'Resource Admin',
  resource_admin,
};

