import { custom_user } from './custom_user';
import { user_role } from './user_role';
import { user_customer } from './user_customer';
import { provider } from './provider';
import { common } from './common';
import { login } from './login';
import { profile } from './profile';
import { policy } from './policy';
import { resource } from './resource';
import { target_user } from './target_user';
import { contact_information } from './contact_information';
import { resource_admin } from './resource_admin';
import { network } from './network';
import { structure } from './structure';
import { affiliation } from './affiliation';
import { esfridomain } from './esfridomain';
import { esfritype } from './esfritype';
import { activity } from './activity';
import { challenge } from './challenge';
import { domain } from './domain';
import { subdomain } from './subdomain';
import { supercategory } from './supercategory';
import { category } from './category';
import { subcategory } from './subcategory';
import { order_type } from './order_type';
import { funding_program } from './funding_program';
import { funding_body } from './funding_body';
import { access_type } from './access_type';
import { access_mode } from './access_mode';
import { trl } from './trl';
import { resource_lcs } from './resource_lcs';
import { legalstatus } from './legalstatus';
import { merildomain} from './merildomain';
import { merilsubdomain} from './merilsubdomain';


export default {
  'value.not.set': '',
  'file': common.file,
  'message': common.message,
  'custom_user': custom_user,
  'user_role': user_role,
  'user_customer': user_customer,
  'provider': provider,
  'form': common.form,
  'login': login,
  'group_menu': common.group_menu,
  'confirm': common.confirm,
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
  'legalstatus': legalstatus,
  'affiliation': affiliation,
  'network': network,
  'structure': structure,
  'esfridomain': esfridomain,
  'esfritype': esfritype,
  'activity': activity,
  'challenge': challenge,
  'domain': domain,
  'subdomain': subdomain,
  'supercategory': supercategory,
  'category': category,
  'subcategory': subcategory,
  'merildomain': merildomain,
  'merilsubdomain': merilsubdomain,
  'username': login.default.label,
  'search.input.placeholder': 'Search',
  order_type,
  funding_program,
  funding_body,
  access_type,
  access_mode,
  trl,
  resource_lcs,
};

