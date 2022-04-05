
About Selenium
===============
Selenium is a free (open-source) automated testing framework used to validate web applications across different browsers and platforms.
You can use multiple programming languages like Java, C#, Python etc to create Selenium Test Scripts. Testing done using the Selenium tool is usually referred to as Selenium Testing.

Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers.
Selenium is many things but at its core, it is a toolset for web browser automation that uses the best techniques available to remotely control browser instances and emulate a user’s interaction with the browser.
It allows users to simulate common activities performed by end-users; entering text into fields, selecting drop-down values and checking boxes, and clicking links in documents. It also provides many other controls such as mouse movement, arbitrary JavaScript execution, and much more.


Functional end-user tests such as Selenium tests are **expensive** to run, however. Furthermore, **they typically require substantial infrastructure to be in place to be run effectively**.
It is a good rule to always ask yourself if what you want to test can be done using more lightweight test approaches such as unit tests or with a lower-level approach.


Browser automation has the reputation of being “***flaky***”, but in reality, that is because users frequently demand too much of it.

A distinct advantage of Selenium tests is their inherent ability to test all components of the application, from backend to frontend, from a user’s perspective. So in other words, whilst functional tests may be expensive to run, they also encompass large business-critical portions at one time.

* [More about Selenium...](https://www.selenium.dev/documentation/en/introduction/)
* [Medium: Cypress vs Selenium WebDriver: Better, Or Just Different?](https://medium.com/@applitools/cypress-vs-selenium-webdriver-better-or-just-different-2dc76906607d)

-------------------------------------------------------------------------------------------------------------------




Agora-sp Selenium tests
======================
The Selenium tests carry out validity tests on the capabilities offered by **Agora-sp**.
It is responsible for verifying that the following functionalities exist and work properly:

* Basic user authentication.
* Create/Search/Delete a Resource.
* Create/Search/Delete a Provider.
* Create/Search/Delete a Contact Information.
* Validate mandatory fields from all the above forms.
* Verify that exists specific Edit and Details page for above main objects.

At each step of Selenium tests, indicate exactly which page and field is being tested and whether the test was successful or not.




Prerequisites
==============
The only prerequisites for running the Selenium tests are the following:

* Python >= **3.5.3**
* Selenium == **3.141.0**

The tests have been written in Python 3 and tested with `Python 3.5.3`, `Python 3.7.3` and `Python 3.7.7`.
Using the latest current version of [Selenium (3.141.0) Python bindings](https://pypi.org/project/selenium/). Which is set to the [`requirements.txt` file](requirements.txt).

> Note: We strongly recommend that you install all the required packages within a Python virtual environment and run the tests through it.
>
> There are many options for creating a Python virtual environment. Here we present the simplest:
> ```bash
> python3 -m venv /path/to/a_env_directory
> ```

To install the required python packages, you need to run the following command:
```bash
pip install -r requirements.txt
```




How to run
===========
Once you have the required packages installed, just run:
```bash
python agora_ui_tests.py --url https://agora.example.com/
```

### Parameters.
`--url` : Mandatory parameter that specifies on which agora-sp page (instance) where the tests will be executed.

> Important notes:
> 1. The slash (`/`) at the end of URL the, is mandatory.
> 2. The Agora-sp instances which the tests will be executed must have the corresponding superuser which [is used by Selenium tests](agora/Agora.py#L82-83).

#### Results.

This is a sample of the results.

<details>
  <summary> Output </summary>

```
# Validations in the Contact form.
[Email]                              Email Input Validation     Success
[Phone]                              Phone Input Validation     Success
[Saving form status]                     Form Invalid           Success

# Validations in the Provider form.
[EPP.BAI.3]                          URL Input Validation   Success
[EPP.MRI.2]                          URL Input Validation   Success
[EPP.MRI.3]                          URL Input Validation   Success
[Saving form status]                     Form Invalid       Success

# Validations in the Resource form.
[ERP.BAI.4]                          URL Input Validation   Success
[ERP.MRI.3]                          URL Input Validation   Success
[ERP.MRI.4]                          URL Input Validation   Success
[ERP.MRI.5]                          URL Input Validation   Success
[ERP.MGI.1]                          URL Input Validation   Success
[ERP.MGI.2]                          URL Input Validation   Success
[ERP.MGI.3]                          URL Input Validation   Success
[ERP.MGI.4]                          URL Input Validation   Success
[ERP.MGI.5]                          URL Input Validation   Success
[ERP.MGI.6]                          URL Input Validation   Success
[ERP.MGI.7]                          URL Input Validation   Success
[ERP.MGI.8]                          URL Input Validation   Success
[ERP.MGI.9]                          URL Input Validation   Success
[ERP.AOI.2]                          URL Input Validation   Success
[ERP.FNI.1]                          URL Input Validation   Success
[ERP.FNI.2]                          URL Input Validation   Success
[ERP.COI.13]                         Email Input Validation     Success
[ERP.COI.14]                         Email Input Validation     Success
[Saving form status]                     Form Invalid       Success

# Edit a contact record.
[Edit page]                              Found and visited  Success

# Details of a contact record.
[Details page]                           Found and visited  Success

# Edit a provider record.
[Edit page]                              Found and visited  Success

# Details of a contact record.
[Details page]                           Found and visited  Success

# Edit a resources record.
[Edit page]                              Found and visited  Success

# Details of a contact record.
[Details page]                           Found and visited  Success

# Create a new contact.
[first_name]                             Found and filled   Success
[last_name]                              Found and filled   Success
[email]                                  Found and filled   Success
[phone]                                  Found and filled   Success
[position]                               Found and filled   Success
[organisation]                           Found and filled   Success
[Saving form status]                     Form Saved         Success
[Search]                                 Found 1 record     Success
[Delete form status]                     Form Saved         Success

# Create a new provider.
[epp_bai_id]                           Found and filled   Success
[epp_bai_name]                         Found and filled   Success
[epp_bai_abbreviation]                 Found and filled   Success
[epp_bai_website]                      Found and filled   Success
[epp_bai_legal_entity]                 Found and filled   Success
[epp_bai_legal_status]                 Found and filled   Success
[epp_cli_1_scientific_domain]            Found and filled   Success
[epp_cli_2_scientific_subdomain]         Found and filled   Success
[epp_cli_3_tags]                         Found and filled   Success
[epp_loi_1_street_name_and_number]       Found and filled   Success
[epp_loi_2_postal_code]                  Found and filled   Success
[epp_loi_3_city]                         Found and filled   Success
[epp_loi_5_country_or_territory]         Found and filled   Success
[epp_loi_4_region]                       Found and filled   Success
[epp_mri_description]                  Found and filled   Success
[epp_mri_logo]                         Found and filled   Success
[epp_mri_multimedia]                   Found and filled   Success
[epp_mti_1_life_cycle_status]            Found and filled   Success
[epp_mti_2_certifications]               Found and filled   Success
[main_contact]                           Found and filled   Success
[public_contact]                         Found and filled   Success
[epp_bai_hosting_legal_entity]         Found and filled   Success
[epp_oth_participating_countries]      Found and filled   Success
[epp_oth_affiliations]                 Found and filled   Success
[epp_oth_networks]                     Found and filled   Success
[epp_oth_structure_type]               Found and filled   Success
[epp_oth_esfri_domain]                 Found and filled   Success
[epp_oth_esfri_type]                   Found and filled   Success
[epp_oth_meril_scientific_domain]      Found and filled   Success
[epp_oth_meril_scientific_subdomain]   Found and filled   Success
[epp_oth_areas_of_activity]           Found and filled   Success
[epp_oth_societal_grand_challenges]   Found and filled   Success
[epp_oth_national_roadmaps]           Found and filled   Success
[Saving form status]                     Form Saved         Success
[Search]                                 Found 1 record     Success
[Delete form status]                     Form Saved         Success

# Create a new resource.
[erp_bai_0_id]                           Found and filled   Success
[erp_bai_1_name]                         Found and filled   Success
[erp_bai_2_service_organisation]         Found and filled   Success
[erp_bai_3_service_providers]            Found and filled   Success
[erp_bai_4_webpage]                      Found and filled   Success
[erp_cli_1_scientific_domain]            Found and filled   Success
[erp_cli_2_scientific_subdomain]         Found and filled   Success
[erp_cli_3_category]                     Found and filled   Success
[erp_cli_4_subcategory]                  Found and filled   Success
[erp_cli_5_target_users]                 Found and filled   Success
[erp_cli_6_access_type]                  Found and filled   Success
[erp_cli_7_access_mode]                  Found and filled   Success
[erp_cli_8_tags]                         Found and filled   Success
[erp_mri_1_description]                  Found and filled   Success
[erp_mri_2_tagline]                      Found and filled   Success
[erp_mri_3_logo]                         Found and filled   Success
[erp_mri_4_mulitimedia]                  Found and filled   Success
[erp_mri_5_use_cases]                    Found and filled   Success
[erp_mgi_1_helpdesk_webpage]             Found and filled   Success
[erp_mgi_2_user_manual]                  Found and filled   Success
[erp_mgi_3_terms_of_use]                 Found and filled   Success
[erp_mgi_4_privacy_policy]               Found and filled   Success
[erp_mgi_5_access_policy]                Found and filled   Success
[erp_mgi_6_sla_specification]            Found and filled   Success
[erp_mgi_7_training_information]         Found and filled   Success
[erp_mgi_8_status_monitoring]            Found and filled   Success
[erp_mgi_9_maintenance]                  Found and filled   Success
[erp_gla_1_geographical_availability]    Found and filled   Success
[erp_gla_2_language]                     Found and filled   Success
[erp_rli_1_geographic_location]          Found and filled   Success
[main_contact]                           Found and filled   Success
[public_contact]                         Found and filled   Success
[erp_coi_13_helpdesk_email]              Found and filled   Success
[erp_coi_14_security_contact_email]      Found and filled   Success
[erp_mti_1_technology_readiness_level]   Found and filled   Success
[erp_mti_2_life_cycle_status]            Found and filled   Success
[erp_mti_3_certifications]               Found and filled   Success
[erp_mti_4_standards]                    Found and filled   Success
[erp_mti_5_open_source_technologies]     Found and filled   Success
[erp_mti_6_version]                      Found and filled   Success
[erp_mti_7_last_update]                  Found and filled   Success
[erp_mti_8_changelog]                    Found and filled   Success
[required_resources]                     Found and filled   Success
[related_resources]                      Found and filled   Success
[erp_dei_3_related_platforms]            Found and filled   Success
[erp_ati_1_funding_body]                 Found and filled   Success
[erp_ati_2_funding_program]              Found and filled   Success
[erp_ati_3_grant_project_name]           Found and filled   Success
[erp_aoi_1_order_type]                   Found and filled   Success
[erp_aoi_2_order]                        Found and filled   Success
[erp_fni_1_payment_model]                Found and filled   Success
[erp_fni_2_pricing]                      Found and filled   Success
[Saving form status]                     Form Saved         Success
[Search]                                 Found 1 record     Success
[Delete form status]                     Form Saved         Success

Execution time of the Selenium UI tests is : 00:02:50
```
</details>




----------------------------------------------------------------

# References.

* [Selenium with Python](https://selenium-python.readthedocs.io/)

