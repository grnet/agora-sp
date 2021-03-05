import { access_mode } from './access_mode';
import { access_type } from './access_type';
import { activity } from './activity';
import { affiliation } from './affiliation';
import { category } from './category';
import { challenge } from './challenge';
import { common } from './common';
import { contact_information } from './contact_information';
import { custom_user } from './custom_user';
import { domain } from './domain';
import { esfridomain } from './esfridomain';
import { esfritype } from './esfritype';
import { funding_body } from './funding_body';
import { funding_program } from './funding_program';
import { legalstatus } from './legalstatus';
import { login } from './login';
import { merildomain} from './merildomain';
import { merilsubdomain} from './merilsubdomain';
import { network } from './network';
import { order_type } from './order_type';
import { privacy_policy } from './privacy_policy';
import { access_policy } from './access_policy';
import { terms } from './terms';
import { profile } from './profile';
import { provider } from './provider';
import { resource } from './resource';
import { resource_admin } from './resource_admin';
import { resource_lcs } from './resource_lcs';
import { structure } from './structure';
import { subcategory } from './subcategory';
import { subdomain } from './subdomain';
import { supercategory } from './supercategory';
import { target_user } from './target_user';
import { trl } from './trl';
import { user_customer } from './user_customer';
import { user_role } from './user_role';


export default {
  'Service Admin': 'Resource Admin',
  'confirm': common.confirm,
  'file': common.file,
  'form': common.form,
  'group_menu': common.group_menu,
  'list': common.list,
  'message': common.message,
  'row': common.row,
  'search.input.placeholder': 'Search',
  'select': common.select,
  'username': login.default.label,
  'value.not.set': '',
  access_mode,
  access_type,
  activity,
  affiliation,
  category,
  challenge,
  common,
  contact_information,
  custom_user,
  domain,
  esfridomain,
  esfritype,
  funding_body,
  funding_program,
  legalstatus,
  login,
  merildomain,
  merilsubdomain,
  network,
  order_type,
  privacy_policy,
  access_policy,
  terms,
  profile,
  provider,
  resource,
  resource_admin,
  resource_lcs,
  structure,
  subcategory,
  subdomain,
  supercategory,
  target_user,
  trl,
  user_customer,
  user_role,
  'ResourceAdminship Object exists': resource_admin.errors.object_exists,
  'No organisation': resource_admin.errors.no_organisation,
  'Email unique constraint failed': custom_user.errors.unique_email,
  'Username unique constraint failed': custom_user.errors.unique_username,
  'shibboleth_duplicate_email': custom_user.errors.unique_email,
};

