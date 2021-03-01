# -*- coding: UTF-8 -*-
import requests
import logging
from datetime import datetime
from django.conf import settings
import json
from datetime import datetime
from django.utils import timezone
from apimas.errors import ValidationError

EOSC_API_URL = getattr(settings, 'EOSC_API_URL', '')
EOSC_TOKEN = getattr(settings, 'EOSC_TOKEN', '')
logger = logging.getLogger(__name__)


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


def create_eosc_api_json(instance):
    resource_json = {}
    if instance.erp_bai_1_name != None:
        resource_json['name'] = instance.erp_bai_1_name
    if instance.erp_bai_2_organisation.eosc_id != None:
        resource_json['resourceOrganisation'] = instance.erp_bai_2_organisation.eosc_id
    if len(instance.erp_bai_3_providers.all())> 0:
        resource_json['resourceProviders'] = [o.eosc_id for o in instance.erp_bai_3_providers.all()]
    if instance.erp_bai_4_webpage != None:
        resource_json['webpage'] = instance.erp_bai_4_webpage
    if instance.erp_mri_1_description != None:
        resource_json['description'] = instance.erp_mri_1_description
    if instance.erp_mri_2_tagline != None:
        resource_json['tagline'] = instance.erp_mri_2_tagline
    if instance.erp_mri_3_logo != None:
        resource_json['logo'] = instance.erp_mri_3_logo
    if instance.erp_mri_4_mulitimedia != None:
        resource_json['multimedia'] = [instance.erp_mri_4_mulitimedia]
    if instance.erp_mri_5_use_cases != None:
        resource_json['useCases'] = [instance.erp_mri_5_use_cases]
    if instance.erp_cli_1_scientific_domain != None:
        resource_json['scientificDomains'] = get_list_sci_domains(instance.erp_cli_1_scientific_domain, instance.erp_cli_2_scientific_subdomain)
    if instance.erp_cli_3_category != None:
        resource_json['categories'] = get_list_categories(instance.erp_cli_3_category, instance.erp_cli_4_subcategory)
    if len(instance.erp_cli_5_target_users.all())> 0:
        resource_json['targetUsers'] = [o.eosc_id for o in instance.erp_cli_5_target_users.all()]
    if len(instance.erp_cli_6_access_type.all())> 0:
        resource_json['accessTypes'] = [o.eosc_id for o in instance.erp_cli_6_access_type.all()]
    if len(instance.erp_cli_7_access_mode.all())> 0:
        resource_json['accessModes'] = [o.eosc_id for o in instance.erp_cli_7_access_mode.all()]
    if instance.erp_cli_8_tags != None:
        resource_json['tags'] = instance.erp_cli_8_tags.replace(" ","").split(",")
    if instance.erp_mgi_1_helpdesk_webpage != None:
        resource_json['helpdeskPage'] = instance.erp_mgi_1_helpdesk_webpage
    if instance.erp_mgi_2_user_manual != None:
        resource_json['userManual'] = instance.erp_mgi_2_user_manual
    if instance.erp_mgi_3_terms_of_use != None:
        resource_json['termsOfUse'] = instance.erp_mgi_3_terms_of_use
    if instance.erp_mgi_4_privacy_policy != None:
        resource_json['privacyPolicy'] = instance.erp_mgi_4_privacy_policy
    if instance.erp_mgi_5_access_policy != None:
        resource_json['accessPolicy'] = instance.erp_mgi_5_access_policy
    if instance.erp_mgi_6_sla_specification != None:
        resource_json['serviceLevel'] = instance.erp_mgi_6_sla_specification
    if instance.erp_mgi_7_training_information != None:
        resource_json['trainingInformation'] = instance.erp_mgi_7_training_information
    if instance.erp_mgi_8_status_monitoring != None:
        resource_json['statusMonitoring'] = instance.erp_mgi_8_status_monitoring
    if instance.erp_mgi_9_maintenance != None:
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
    if instance.erp_coi_13_helpdesk_email != None:
        resource_json['helpdeskEmail'] = instance.erp_coi_13_helpdesk_email
    if instance.erp_coi_14_security_contact_email != None:
        resource_json['securityContactEmail'] = instance.erp_coi_14_security_contact_email
    if instance.erp_mti_1_technology_readiness_level.eosc_id != None:
        resource_json['trl'] = instance.erp_mti_1_technology_readiness_level.eosc_id
    if instance.erp_mti_2_life_cycle_status.eosc_id != None:
        resource_json['lifeCycleStatus'] = instance.erp_mti_2_life_cycle_status.eosc_id
    if instance.erp_mti_3_certifications != None:
        resource_json['certifications'] = instance.erp_mti_3_certifications.split('\n')
    if instance.erp_mti_4_standards != None:
        resource_json['standards'] = instance.erp_mti_4_standards.split('\n')
    if instance.erp_mti_5_open_source_technologies != None: 
        resource_json['openSourceTechnologies'] = instance.erp_mti_5_open_source_technologies.split('\n')
    if instance.erp_mti_6_version != None:
        resource_json['version'] = instance.erp_mti_6_version
    if instance.erp_mti_7_last_update != None:
        resource_json['lastUpdate'] = instance.erp_mti_7_last_update
    if instance.erp_mti_8_changelog != None:
        resource_json['changeLog'] = instance.erp_mti_8_changelog.split('\n')
    if instance.erp_dei_3_related_platforms != None:
        resource_json['relatedPlatforms'] = instance.erp_dei_3_related_platforms.replace(" ","").split(",")
    if len(instance.erp_ati_1_funding_body.all())> 0:
        resource_json['fundingBody'] = [o.eosc_id for o in instance.erp_ati_1_funding_body.all()]
    if len(instance.erp_ati_2_funding_program.all())> 0:
        resource_json['fundingPrograms'] = [o.eosc_id for o in instance.erp_ati_2_funding_program.all()]
    if instance.erp_ati_3_grant_project_name != None:
        resource_json['grantProjectNames'] = [instance.erp_ati_3_grant_project_name]
    if instance.erp_aoi_1_order_type.eosc_id != None:
        resource_json['orderType'] = instance.erp_aoi_1_order_type.eosc_id
    if instance.erp_aoi_2_order != None:
        resource_json['order'] = instance.erp_aoi_2_order
    if instance.erp_fni_1_payment_model != None:
        resource_json['paymentModel'] = instance.erp_fni_1_payment_model
    if instance.erp_fni_2_pricing != None:
        resource_json['pricing'] = instance.erp_fni_2_pricing
    if len(instance.required_resources.all())> 0:
        resource_json['requiredResources'] = [o.eosc_id for o in instance.required_resources.all()]
    if len(instance.related_resources.all())> 0:
        resource_json['relatedResources'] = [o.eosc_id for o in instance.related_resources.all()]
    print(json.dumps(resource_json))
    return resource_json


def resource_post_eosc(backend_input, instance, context):
    eosc_req = create_eosc_api_json(instance)
    url = EOSC_API_URL+'resource'
    id  = str(instance.id)
    username = context['auth/user'].username
    headers = {
        'Authorization': EOSC_TOKEN,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    logger.info('EOSC PORTAL API call to POST resource \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.post(url, headers=headers,json=eosc_req)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_state = "Published"
        instance.eosc_id = response.json()['id']
        instance.eosc_published_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
        instance.eosc_state = "Error"
        raise ValidationError(response.json()['error'])
    instance.save()
    return instance