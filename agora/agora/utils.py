import os
import json
import re
import requests
import logging
from datetime import datetime
from collections import defaultdict
from HTMLParser import HTMLParseError
from bs4 import BeautifulSoup, Comment
from ckeditor_uploader.fields import RichTextUploadingField

from argo_ams_library import ArgoMessagingService, AmsMessage, AmsException

from django.conf import settings
import accounts.models
from agora.permissions import get_rules
from agora.settings import (
    AMS_TOKEN,
    AMS_ENDPOINT,
    AMS_PROJECT,
    AMS_TOPIC,
)
logger = logging.getLogger(__name__)

EOSC_API_URL = getattr(settings, 'EOSC_API_URL', '')
EOSC_CATALOGUE_ID = getattr(settings, 'EOSC_CATALOGUE_ID', '')
CA_BUNDLE = getattr(settings, 'CA_BUNDLE', '/etc/ssl/certs/ca-bundle.crt')

_root_url = None


def rule_to_dict(data, args):
    if len(args) == 1:
        return args[0]

    key = args.pop(0)
    for k in key.split(","):
        k = k.strip()
        data[k] = data[k] if k in data else {}
        partial = {
            k: rule_to_dict(data[k], args)
        }
        data.update(partial)
    return data


def load_permissions():
    PERMISSIONS = defaultdict(lambda: dict)
    for rule in transform_rules(get_rules()):
        rule_to_dict(PERMISSIONS, list(rule))
    return PERMISSIONS


def load_resources():
    with open(os.path.join(settings.PATH_RESOURCES, 'common.json')) \
            as json_file:
        return json.load(json_file)


def djoser_verifier(token):
    user = accounts.models.User.objects.filter(auth_token=token).first()
    if user is None or not user.is_active:
        return None
    return user


def userid_extractor(user, context):
    return user


def transform_rules(rules):
    new_rules = []
    for r in rules:
        el = list(r)
        if el[5] == "*":
            new_l = (el[0], el[1], el[2], el[5], el[4], el[6])
            new_rules.append(new_l)
        else:
            fields = el[5].split(",")
            for f in fields:
                new_l = (el[0], el[1], el[2], f, el[4], el[6])
                new_rules.append(new_l)
    return new_rules


config_file = os.path.join(settings.SETTINGS_DIR, 'deployment.conf')
with open(config_file) as f:
    deploy_config = json.load(f)

_root_url = deploy_config[':root_url']


def get_root_url():
    return _root_url


def publish_message(service, action):
    """
    Send a message using argo messaging service when an action upon a service
    takes place.
    """
    service_id = str(service.get('id'))
    service_name = service.get('name')
    service_data = service.get('data', {})
    ams = ArgoMessagingService(endpoint=AMS_ENDPOINT,
                               project=AMS_PROJECT,
                               token=AMS_TOKEN)
    endpoint = '{0}/api/v2/ext-services/{1}'.format(get_root_url(), service_id)
    # The value of the data property must be unicode in order to be
    # encoded in base64 format in AmsMessage
    data = json.dumps(service_data)

    try:
        if not ams.has_topic(AMS_TOPIC):
            ams.create_topic(AMS_TOPIC)
    except AmsException as e:
        print e
        raise SystemExit(1)

    msg = AmsMessage(data=data,
                     attributes={
                         "method": action,
                         "service_id": service_id,
                         "service_name": service_name,
                         "endpoint": endpoint
                     }).dict()
    try:
        ret = ams.publish(AMS_TOPIC, msg)
        print ret
    except AmsException as e:
        print e


def clean_html_fields(instance):
    class_fields = instance.__class__._meta.get_fields()
    fields_to_clean = [field for field in class_fields
                       if isinstance(field, RichTextUploadingField)]
    for field in fields_to_clean:
        old_value = getattr(instance, field.name)
        setattr(instance, field.name, safe_html(old_value))


def safe_html(html):
    if not html:
        return html

    # remove these tags, complete with contents.
    blacklist = ["script", "style", "audio", "video"]

    whitelist = [
        "div", "span", "p", "br", "pre",
        "table", "tbody", "thead", "tr", "td", "a",
        "blockquote", "code",
        "ul", "li", "ol",
        "b", "em", "i", "strong", "u", "font",
        "h1", "h2", "h3", "h4", "h5", "h6",
        "dl", "dt", "dd",
        "br", "img",
        ]

    whitelist_attrs = [
        "src", "width", "height", "alt",
        "href", "target", "rel",
    ]

    try:
        # BeautifulSoup is catching out-of-order and unclosed tags, so markup
        # can't leak out of comments and break the rest of the page.
        soup = BeautifulSoup(html, 'html.parser')
    except HTMLParseError:
        return html

    # now strip HTML we don't like.
    for tag in soup.findAll():
        if tag.name.lower() in blacklist:
            # blacklisted tags are removed in their entirety
            tag.extract()
        elif tag.name.lower() in whitelist:
            # tag is allowed
            # blacklisted attrs are removed in their entirety
            for attr in [attr for attr in tag.attrs if attr not in whitelist_attrs]:
                del tag[attr]
        else:
            # not a whitelisted tag. I'd like to remove it from the tree
            # and replace it with its children. But that's hard. It's much
            # easier to just replace it with an empty span tag.
            tag.name = "span"
            tag.attrs = []

    # scripts can be executed from comments in some cases
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    return unicode(soup)

def get_contact(contact):
    contact_obj = {
        "firstName": contact.first_name,
        "lastName": contact.last_name,
        "email": contact.email,
        "phone": contact.phone,
        "position": contact.position,
        "organisation": contact.organisation.eosc_id
    }
    return contact_obj


def match_geolocation(geolocation):
    if geolocation != None and len(geolocation)>0:
        return geolocation.split(" ")[-1].replace("(","").replace(")","")
    return ""

def get_match_category(sub_id,categories_ids):
    sub_cat = sub_id.split('-')[1] + '-' + sub_id.split('-')[2]
    for category_id in categories_ids:
        cat = category_id.split('-')[1] + '-' + category_id.split('-')[2]
        if sub_cat == cat:
            return category_id
    return ''

def get_match_subcategory(cat_id,subcategories_ids):
    cat = cat_id.split('-')[1] +'-'+ cat_id.split('-')[2]
    for subcategory_id in subcategories_ids:
        sub_cat = subcategory_id.split('-')[1] +'-'+ subcategory_id.split('-')[2]
        if sub_cat == cat:
            return subcategory_id
    return ''

def get_category(category_id):
    return 'category-'+ category_id.split('-')[1] + '-' + category_id.split('-')[2]

def get_subcategory(category_id):
    cat = category_id.split('-')[1] + '-' + category_id.split('-')[2]
    return 'subcategory-' + cat + '-other'

def unique_list(cat_list):
    unique_cat = []
    for cat in cat_list:
        is_new = True
        dir(cat)
        for uniq in unique_cat:
            if cat['category'] == uniq['category'] and cat['subcategory'] == uniq['subcategory']:
                is_new = False
        if is_new == True:
            unique_cat.append(cat)
    return unique_cat


def unique_list_domains(cat_list):
    unique_cat = []
    for cat in cat_list:
        is_new = True
        dir(cat)
        for uniq in unique_cat:
            if cat['scientificDomain'] == uniq['scientificDomain'] and cat['scientificSubdomain'] == uniq['scientificSubdomain']:
                is_new = False
        if is_new == True:
            unique_cat.append(cat)
    return unique_cat


def unique_list_meril_domains(cat_list):
    unique_cat = []
    for cat in cat_list:
        is_new = True
        dir(cat)
        for uniq in unique_cat:
            if cat['merilScientificDomain'] == uniq['merilScientificDomain'] and cat['merilScientificSubdomain'] == uniq['merilScientificSubdomain']:
                is_new = False
        if is_new == True:
            unique_cat.append(cat)
    return unique_cat


def get_match_domain(sub_id,categories_ids):
    sub_cat = sub_id.split('-')[1]
    for category_id in categories_ids:
        cat = category_id.split('-')[1]
        if sub_cat == cat:
            return category_id
    return ''


def get_match_subdomain(cat_id,subcategories_ids):
    cat = cat_id.split('-')[1]
    for subcategory_id in subcategories_ids:
        sub_cat = subcategory_id.split('-')[1]
        if sub_cat == cat:
            return subcategory_id
    return ''


def get_domain(category_id, category_prefix):
    return category_prefix + category_id.split('-')[1]


def get_subdomain(category_id):
    cat = category_id.split('-')[1]
    if cat == "medical_and_health_sciences":
        return 'scientific_subdomain-' + cat + '-other_medical_sciences'
    elif cat == "other":
        return 'scientific_subdomain-' + cat + '-other'
    elif cat == "engineering_and_technology":
        return 'scientific_subdomain-' + cat + '-other_engineering_and_technology_sciences'
    elif cat == "generic":
        return 'scientific_subdomain-' + cat + '-generic'
    else:
        return 'scientific_subdomain-' + cat + '-other_' + cat

def get_meril_subdomain(category_id):
    cat = category_id.split('-')[1]
    if cat == 'other':
        return 'provider_meril_scientific_subdomain-' + cat + '-other'
    return 'provider_meril_scientific_subdomain-' + cat + '-other_'+cat


def get_list_categories(categories, subcategories):
    categories_list = []
    for subcategory in subcategories.all():
        cat = get_match_category(subcategory.eosc_id,[c.eosc_id for c in categories.all()])
        if len(cat)>0:
            categories_list.append({'category': cat, 'subcategory': subcategory.eosc_id})
        else:
            cat = get_category(subcategory.eosc_id)
            categories_list.append({'category': cat, 'subcategory': subcategory.eosc_id})
    for category in categories.all():
        sub = get_match_subcategory(category.eosc_id,[s.eosc_id for s in subcategories.all()])
        if len(sub)>0:
            categories_list.append({'category': category.eosc_id, 'subcategory': sub})
        else:
            sub = get_subcategory(category.eosc_id)
            categories_list.append({'category': category.eosc_id, 'subcategory': sub})
    return unique_list(categories_list)


def get_list_sci_domains(categories, subcategories):
    categories_list = []
    for subcategory in subcategories.all():
        cat = get_match_domain(subcategory.eosc_id,[c.eosc_id for c in categories.all()])
        if len(cat)>0:
            categories_list.append({'scientificDomain': cat, 'scientificSubdomain': subcategory.eosc_id})
        else:
            cat = get_domain(subcategory.eosc_id, 'scientific_domain-')
            categories_list.append({'scientificDomain': cat, 'scientificSubdomain': subcategory.eosc_id})
    for category in categories.all():
        sub = get_match_subdomain(category.eosc_id,[s.eosc_id for s in subcategories.all()])
        if len(sub)>0:
            categories_list.append({'scientificDomain': category.eosc_id, 'scientificSubdomain': sub})
        else:
            sub = get_subdomain(category.eosc_id)
            categories_list.append({'scientificDomain': category.eosc_id, 'scientificSubdomain': sub})
    return unique_list_domains(categories_list)

def get_list_meril_domains(categories, subcategories):
    categories_list = []
    for subcategory in subcategories.all():
        cat = get_match_domain(subcategory.eosc_id,[c.eosc_id for c in categories.all()])
        if len(cat)>0:
            categories_list.append({'merilScientificDomain': cat, 'merilScientificSubdomain': subcategory.eosc_id})
        else:
            cat = get_domain(subcategory.eosc_id, 'provider_meril_scientific_domain-')
            categories_list.append({'merilScientificDomain': cat, 'merilScientificSubdomain': subcategory.eosc_id})
    for category in categories.all():
        sub = get_match_subdomain(category.eosc_id,[s.eosc_id for s in subcategories.all()])
        if len(sub)>0:
            categories_list.append({'merilScientificDomain': category.eosc_id, 'merilScientificSubdomain': sub})
        else:
            sub = get_meril_subdomain(category.eosc_id)
            categories_list.append({'merilScientificDomain': category.eosc_id, 'merilScientificSubdomain': sub})
    return unique_list_meril_domains(categories_list)


# Return fallback value
def check_eosc_id(eosc_id, fallback_value):
    if eosc_id == None:
        return fallback_value
    elif len(eosc_id.strip())==0:
        return fallback_value
    else:
        return eosc_id


def get_location(instance):
    location = {}
    location['streetNameAndNumber'] = instance.epp_loi_street_name_and_number
    location['postalCode'] = instance.epp_loi_postal_code
    location['city'] = instance.epp_loi_city
    location['region'] = instance.epp_loi_region
    location['country'] = match_geolocation(instance.epp_loi_country_or_territory).upper()
    return location


def string_to_array(str_field):
    arr_value = str_field.split(",")
    return [x.strip() for x in arr_value]

def create_json_pairs_from_obj(entry,name1,name2):
    # entry is a string json object with key,pair values
    # this function creates an array with [{name1:key,name2:value}] format
    object = json.loads(entry)
    obj_arr = []
    for item in object.items():
        new_obj = {}
        new_obj[name1] = item[0]
        new_obj[name2] = item[1]
        obj_arr.append(new_obj)
    return obj_arr

def create_eosc_api_json_resource(instance):
    resource_json = {}
    if instance.eosc_id != None:
        resource_json['id'] = instance.eosc_id
    resource_json['catalogueId'] = EOSC_CATALOGUE_ID
    resource_json['name'] = instance.erp_bai_name
    resource_json['abbreviation'] = instance.erp_bai_abbreviation
    if instance.erp_bai_organisation != None:
        resource_json['resourceOrganisation'] = instance.erp_bai_organisation.eosc_id
    resource_json['resourceProviders'] = [o.eosc_id for o in instance.erp_bai_providers.all()]
    resource_json['webpage'] = instance.erp_bai_webpage
    resource_json['description'] = instance.erp_mri_description
    resource_json['tagline'] = instance.erp_mri_tagline
    resource_json['logo'] = instance.erp_mri_logo
    if instance.erp_mri_multimedia != None:
        resource_json['multimedia'] = create_json_pairs_from_obj(instance.erp_mri_multimedia, 'multimediaName', 'multimediaURL')
    if instance.erp_mri_use_cases != None:
        resource_json['useCases'] = create_json_pairs_from_obj(instance.erp_mri_multimedia, 'useCaseName', 'useCaseURL')
    resource_json['scientificDomains'] = get_list_sci_domains(instance.erp_cli_scientific_domain, instance.erp_cli_scientific_subdomain)
    resource_json['categories'] = get_list_categories(instance.erp_cli_category, instance.erp_cli_subcategory)
    resource_json['targetUsers'] = [check_eosc_id(o.eosc_id, 'target_user-other') for o in instance.erp_cli_target_users.all()]
    resource_json['accessTypes'] = [check_eosc_id(o.eosc_id, 'access_type-other') for o in instance.erp_cli_access_type.all()]
    resource_json['accessModes'] = [check_eosc_id(o.eosc_id, 'access_mode-other') for o in instance.erp_cli_access_mode.all()]
    if instance.erp_cli_tags != None:
        resource_json['tags'] = string_to_array(instance.erp_cli_tags)
    resource_json['helpdeskPage'] = instance.erp_mgi_helpdesk_webpage
    resource_json['userManual'] = instance.erp_mgi_user_manual
    resource_json['termsOfUse'] = instance.erp_mgi_terms_of_use
    resource_json['privacyPolicy'] = instance.erp_mgi_privacy_policy
    resource_json['accessPolicy'] = instance.erp_mgi_access_policy
    resource_json['serviceLevel'] = instance.erp_mgi_sla_specification
    resource_json['trainingInformation'] = instance.erp_mgi_training_information
    resource_json['statusMonitoring'] = instance.erp_mgi_status_monitoring
    resource_json['maintenance'] = instance.erp_mgi_maintenance
    if instance.erp_gla_geographical_availability != None:
        resource_json['geographicalAvailabilities'] = [ match_geolocation(o.strip()) for o in instance.erp_gla_geographical_availability.split(",")]
    if instance.erp_gla_language != None:
        resource_json['languageAvailabilities'] = instance.erp_gla_language.replace(" ","").split(",")
    if instance.erp_rli_geographic_location != None:
        resource_json['resourceGeographicLocations'] = [ match_geolocation(o.strip()) for o in instance.erp_rli_geographic_location.split(",")]
    if instance.main_contact != None:
        resource_json['mainContact'] = get_contact(instance.main_contact)
    if instance.public_contact != None:
        resource_json['publicContacts'] = [get_contact(instance.public_contact)]
    resource_json['helpdeskEmail'] = instance.erp_coi_helpdesk_email
    resource_json['securityContactEmail'] = instance.erp_coi_security_contact_email
    if instance.erp_mti_technology_readiness_level != None:
        resource_json['trl'] = check_eosc_id(instance.erp_mti_technology_readiness_level.eosc_id, 'trl-1')
    if instance.erp_mti_life_cycle_status != None:
        resource_json['lifeCycleStatus'] = check_eosc_id(instance.erp_mti_life_cycle_status.eosc_id,'life_cycle_status-other')
    if instance.erp_mti_certifications != None:
        resource_json['certifications'] = instance.erp_mti_certifications.split('\n')
    if instance.erp_mti_standards != None:
        resource_json['standards'] = instance.erp_mti_standards.split('\n')
    if instance.erp_mti_open_source_technologies != None:
        resource_json['openSourceTechnologies'] = instance.erp_mti_open_source_technologies.split('\n')
    resource_json['version'] = instance.erp_mti_version
    resource_json['lastUpdate'] = instance.erp_mti_last_update
    if instance.erp_mti_changelog != None:
        resource_json['changeLog'] = instance.erp_mti_changelog.split('\n')
    if instance.erp_dei_related_platforms != None:
        resource_json['relatedPlatforms'] = string_to_array(instance.erp_dei_related_platforms)
    resource_json['fundingBody'] = [check_eosc_id(o.eosc_id,'funding_body-other') for o in instance.erp_ati_funding_body.all()]
    resource_json['fundingPrograms'] = [check_eosc_id(o.eosc_id,'funding_program-other') for o in instance.erp_ati_funding_program.all()]
    resource_json['grantProjectNames'] = [instance.erp_ati_grant_project_name]
    if instance.erp_aoi_order_type != None:
        resource_json['orderType'] = check_eosc_id(instance.erp_aoi_order_type.eosc_id, 'order_type-other')
    resource_json['order'] = instance.erp_aoi_order
    resource_json['paymentModel'] = instance.erp_fni_payment_model
    resource_json['pricing'] = instance.erp_fni_pricing
    resource_json['requiredResources'] = [o.eosc_id for o in instance.required_resources.all()]
    resource_json['relatedResources'] = [o.eosc_id for o in instance.related_resources.all()]
    return resource_json


def get_life_cycle_status(status):
    if status == 'Under Construction':
        return 'provider_life_cycle_status-under_construction'
    elif status == 'Being Upgraded':
        return 'provider_life_cycle_status-being_upgraded'
    elif status == 'Other':
        return 'provider_life_cycle_status-other'
    elif status == 'Operational':
        return 'provider_life_cycle_status-operational'
    else:
        return 'provider_life_cycle_status-other'

def get_provider_admins(org_id, provider_mail):
    users = accounts.models.User.objects.filter(organisation_id=org_id).all()
    provider = accounts.models.User.objects.get(email=provider_mail)
    provider_users = [{"name": provider.first_name, "surname": provider.last_name, "email": provider.email}]
    for user in users:
        if user.email != provider.email:
            provider_users.append({"name": user.first_name, "surname": user.last_name, "email": user.email})
    return provider_users

def create_eosc_api_json_provider(instance, provider_email):
    admins = get_provider_admins(instance.id, provider_email)
    resource_json = {}
    if instance.eosc_id != None:
        resource_json['id'] = instance.eosc_id
    resource_json['name'] = instance.epp_bai_name
    resource_json['catalogueId'] = EOSC_CATALOGUE_ID
    resource_json['abbreviation'] = instance.epp_bai_abbreviation
    resource_json['website'] = instance.epp_bai_website
    resource_json['legalEntity'] = instance.epp_bai_legal_entity
    if instance.epp_bai_legal_status != None:
        resource_json['legalStatus'] = check_eosc_id( instance.epp_bai_legal_status.eosc_id, 'provider_legal_status-other')
    resource_json['description'] = instance.epp_mri_description
    resource_json['logo'] = instance.epp_mri_logo
    if instance.epp_mri_multimedia != None:
        resource_json['multimedia'] = create_json_pairs_from_obj(instance.epp_mri_multimedia, 'multimediaName', 'multimediaURL')
    resource_json['scientificDomains'] = get_list_sci_domains(instance.epp_cli_scientific_domain, instance.epp_cli_scientific_subdomain)
    if instance.epp_cli_tags != None:
        resource_json['tags'] = string_to_array(instance.epp_cli_tags)
    if instance.epp_cli_structure_type != None:
       resource_json['structureTypes'] = [ check_eosc_id(o.eosc_id, 'provider_structure_type-other') for o in instance.epp_cli_structure_type.all()]
    resource_json['location'] = get_location(instance)
    if instance.main_contact != None:
        resource_json['mainContact'] = get_contact(instance.main_contact)
    if instance.public_contact != None:
        resource_json['publicContacts'] = [get_contact(instance.public_contact)]
    if instance.epp_mti_life_cycle_status != None:
        resource_json['lifeCycleStatus'] = get_life_cycle_status(instance.epp_mti_life_cycle_status)
    if instance.epp_mti_certifications != None:
        resource_json['certifications'] = instance.epp_mti_certifications.split('\n')
    if instance.epp_bai_hosting_legal_entity != None:
        if instance.epp_bai_hosting_legal_entity == "Other":
            resource_json['hostingLegalEntity'] = None
        else:
            resource_json['hostingLegalEntity'] = instance.epp_bai_hosting_legal_entity
    if instance.epp_oth_participating_countries != None:
        resource_json['participatingCountries'] = [ match_geolocation(o.strip()) for o in instance.epp_oth_participating_countries.split(",")]
    if instance.epp_oth_affiliations_verbose != None:
        resource_json['affiliations'] = [ o for o in instance.epp_oth_affiliations_verbose.split(",")]
    if instance.epp_oth_networks != None:
        resource_json['networks'] = [ check_eosc_id(o.eosc_id, 'provider_network-other') for o in instance.epp_oth_networks.all()]
    if instance.epp_oth_esfri_domain != None:
       resource_json['esfriDomains'] = [ check_eosc_id(o.eosc_id, 'provider_esfri_domain-other') for o in instance.epp_oth_esfri_domain.all()]
    if instance.epp_oth_esfri_type != None:
        resource_json['esfriType'] = check_eosc_id(instance.epp_oth_esfri_type.eosc_id, 'provider_esfri_type-other')
    resource_json['merilScientificDomains'] = get_list_meril_domains(instance.epp_oth_meril_scientific_domain, instance.epp_oth_meril_scientific_subdomain)
    if instance.epp_oth_areas_of_activity != None:
       resource_json['areasOfActivity'] = [ check_eosc_id(o.eosc_id, 'provider_area_of_activity-other') for o in instance.epp_oth_areas_of_activity.all()]
    if instance.epp_oth_societal_grand_challenges != None:
       resource_json['societalGrandChallenges'] = [ check_eosc_id(o.eosc_id, 'provider_societal_grand_challenge-other') for o in instance.epp_oth_societal_grand_challenges.all()]
    if instance.epp_oth_national_roadmaps != None:
        resource_json['nationalRoadmaps'] = [ o for o in instance.epp_oth_national_roadmaps.split(",")]
    resource_json['users'] = admins
    return resource_json

def get_resource_eosc_state( eosc_id, headers):
    url = EOSC_API_URL + 'infraService/' + eosc_id
    logger.info('EOSC PORTAL API call to GET resource status \
        with id %s to %s has been made at %s \
        ' %(eosc_id, url, datetime.now()))
    try:
        response = requests.get(url, headers=headers, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        return response.json()['status']
    except requests.exceptions.RequestException as err:
        try:
            logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
        except:
            logger.info('Response status code: %s, %s, %s' % (url, err, response.text))
    return "pending resource"


RESOURCES = load_resources()
USER_ROLES = RESOURCES['USER_ROLES']
LIFECYCLE_STATUSES = RESOURCES["PROVIDER_LIFE_CYCLE_STATUSES"]
SERVICE_ADMINSHIP_STATES = RESOURCES['SERVICE_ADMINSHIP_STATES']
PROVIDER_STATES = RESOURCES['PROVIDER_STATES']
RESOURCE_STATES = RESOURCES['RESOURCE_STATES']
