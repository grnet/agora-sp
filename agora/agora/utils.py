import os
import json
import re
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
    if geolocation != 'Other' and geolocation!='Europe':
        return geolocation.split(" ")[-1].replace("(","").replace(")","")
    elif geolocation == 'Europe':
        return "EU"
    elif geolocation == 'Other':
        return "WW"
    return "WW"

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

def get_domain(category_id):
    return 'scientific_domain-'+ category_id.split('-')[1]

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

def get_list_sci_domains(categories, subcategories):
    categories_list = []
    for subcategory in subcategories.all():
        cat = get_match_domain(subcategory.eosc_id,[c.eosc_id for c in categories.all()])
        if len(cat)>0:
            categories_list.append({'scientificDomain': cat, 'scientificSubdomain': subcategory.eosc_id})
        else:
            cat = get_domain(subcategory.eosc_id)
            categories_list.append({'scientificDomain': cat, 'scientificSubdomain': subcategory.eosc_id})
    for category in categories.all():
        sub = get_match_subdomain(category.eosc_id,[s.eosc_id for s in subcategories.all()])
        if len(sub)>0:
            categories_list.append({'scientificDomain': category.eosc_id, 'scientificSubdomain': sub})
        else:
            sub = get_subdomain(category.eosc_id)
            categories_list.append({'scientificDomain': category.eosc_id, 'scientificSubdomain': sub})
    return unique_list_domains(categories_list)

# Return fallback value
def check_eosc_id(eosc_id, fallback_value):
    if eosc_id == None:
        return fallback_value
    elif len(eosc_id.strip())==0:
        return fallback_value
    else:
        return eosc_id


def create_eosc_api_json(instance):
    resource_json = {}
    if instance.eosc_id != None:
        resource_json['id'] = instance.eosc_id
    resource_json['name'] = instance.erp_bai_1_name
    if instance.erp_bai_2_organisation != None:
        resource_json['resourceOrganisation'] = instance.erp_bai_2_organisation.eosc_id
    resource_json['resourceProviders'] = [o.eosc_id for o in instance.erp_bai_3_providers.all()]
    resource_json['webpage'] = instance.erp_bai_4_webpage
    resource_json['description'] = instance.erp_mri_1_description
    resource_json['tagline'] = instance.erp_mri_2_tagline
    resource_json['logo'] = instance.erp_mri_3_logo
    resource_json['multimedia'] = [instance.erp_mri_4_mulitimedia]
    resource_json['useCases'] = [instance.erp_mri_5_use_cases]
    resource_json['scientificDomains'] = get_list_sci_domains(instance.erp_cli_1_scientific_domain, instance.erp_cli_2_scientific_subdomain)
    resource_json['categories'] = get_list_categories(instance.erp_cli_3_category, instance.erp_cli_4_subcategory)
    resource_json['targetUsers'] = [check_eosc_id(o.eosc_id, 'target_user-other') for o in instance.erp_cli_5_target_users.all()]
    resource_json['accessTypes'] = [check_eosc_id(o.eosc_id, 'access_type-other') for o in instance.erp_cli_6_access_type.all()]
    resource_json['accessModes'] = [check_eosc_id(o.eosc_id, 'access_mode-other') for o in instance.erp_cli_7_access_mode.all()]
    if instance.erp_cli_8_tags != None:
        resource_json['tags'] = instance.erp_cli_8_tags.replace(" ","").split(",")
    resource_json['helpdeskPage'] = instance.erp_mgi_1_helpdesk_webpage
    resource_json['userManual'] = instance.erp_mgi_2_user_manual
    resource_json['termsOfUse'] = instance.erp_mgi_3_terms_of_use
    resource_json['privacyPolicy'] = instance.erp_mgi_4_privacy_policy
    resource_json['accessPolicy'] = instance.erp_mgi_5_access_policy
    resource_json['serviceLevel'] = instance.erp_mgi_6_sla_specification
    resource_json['trainingInformation'] = instance.erp_mgi_7_training_information
    resource_json['statusMonitoring'] = instance.erp_mgi_8_status_monitoring
    resource_json['maintenance'] = instance.erp_mgi_9_maintenance
    if instance.erp_gla_1_geographical_availability != None:
        resource_json['geographicalAvailabilities'] = [ match_geolocation(o.strip()) for o in instance.erp_gla_1_geographical_availability.split(",")]
    if instance.erp_gla_2_language != None:
        resource_json['languageAvailabilities'] = instance.erp_gla_2_language.replace(" ","").split(",")
    if instance.erp_rli_1_geographic_location != None:
        resource_json['resourceGeographicLocations'] = [ match_geolocation(o.strip()) for o in instance.erp_rli_1_geographic_location.split(",")]
    if instance.main_contact != None:
        resource_json['mainContact'] = get_contact(instance.main_contact)
    if instance.public_contact != None:
        resource_json['publicContacts'] = [get_contact(instance.public_contact)]
    resource_json['helpdeskEmail'] = instance.erp_coi_13_helpdesk_email
    resource_json['securityContactEmail'] = instance.erp_coi_14_security_contact_email
    if instance.erp_mti_1_technology_readiness_level != None:
        resource_json['trl'] = check_eosc_id(instance.erp_mti_1_technology_readiness_level.eosc_id, 'trl-1')
    if instance.erp_mti_2_life_cycle_status != None:
        resource_json['lifeCycleStatus'] = check_eosc_id(instance.erp_mti_2_life_cycle_status.eosc_id,'life_cycle_status-other')
    if instance.erp_mti_3_certifications != None:
        resource_json['certifications'] = instance.erp_mti_3_certifications.split('\n')
    if instance.erp_mti_4_standards != None:
        resource_json['standards'] = instance.erp_mti_4_standards.split('\n')
    if instance.erp_mti_5_open_source_technologies != None:
        resource_json['openSourceTechnologies'] = instance.erp_mti_5_open_source_technologies.split('\n')
    resource_json['version'] = instance.erp_mti_6_version
    resource_json['lastUpdate'] = instance.erp_mti_7_last_update
    if instance.erp_mti_8_changelog != None:
        resource_json['changeLog'] = instance.erp_mti_8_changelog.split('\n')
    if instance.erp_dei_3_related_platforms != None:
        resource_json['relatedPlatforms'] = instance.erp_dei_3_related_platforms.replace(" ","").split(",")
    resource_json['fundingBody'] = [check_eosc_id(o.eosc_id,'funding_body-other') for o in instance.erp_ati_1_funding_body.all()]
    resource_json['fundingPrograms'] = [check_eosc_id(o.eosc_id,'funding_program-other') for o in instance.erp_ati_2_funding_program.all()]
    resource_json['grantProjectNames'] = [instance.erp_ati_3_grant_project_name]
    if instance.erp_aoi_1_order_type != None:
        resource_json['orderType'] = check_eosc_id(instance.erp_aoi_1_order_type.eosc_id, 'order_type-other')
    resource_json['order'] = instance.erp_aoi_2_order
    resource_json['paymentModel'] = instance.erp_fni_1_payment_model
    resource_json['pricing'] = instance.erp_fni_2_pricing
    resource_json['requiredResources'] = [o.eosc_id for o in instance.required_resources.all()]
    resource_json['relatedResources'] = [o.eosc_id for o in instance.related_resources.all()]
    return resource_json


RESOURCES = load_resources()
USER_ROLES = RESOURCES['USER_ROLES']
LIFECYCLE_STATUSES = RESOURCES["PROVIDER_LIFE_CYCLE_STATUSES"]
SERVICE_ADMINSHIP_STATES = RESOURCES['SERVICE_ADMINSHIP_STATES']
PROVIDER_STATES = RESOURCES['PROVIDER_STATES']
RESOURCE_STATES = RESOURCES['RESOURCE_STATES']
