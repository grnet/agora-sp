# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- Correct Croatia 2 letter country code.

### Changed
- Expose epp_loi_5_country_or_territory field as capitalized instead of lowercase.

## [1.1.1](https://github.com/grnet/agora-sp/compare/v1.1.0...v1.1.1) - 2020-12-11

### Fixed
- Minor fixes to selenium tests

## [1.1.0](https://github.com/grnet/agora-sp/compare/v1.0.8...v1.1.0) - 2020-12-09

### Changed
- Strip rich html textfields from non essential attributes.
- Do not allow delete of Providers with related entities.

### Fixed
- Upgrade tinyMCE to version 5 to fix version 4 EOL alerts.


## [1.0.8](https://github.com/grnet/agora-sp/compare/v1.0.7...v1.0.8) - 2020-12-01

### Fixed

- Fixed bug with shibboleth users not being able to login.


## [1.0.7](https://github.com/grnet/agora-sp/compare/v1.0.6...v1.0.7) - 2020-11-25

###  Added
- Add public api for providers under /api/v2/public/providers endpoint.
- Add public api for resources under /api/v2/public/resources endpoint.
- Add publish/unpublish functionality for providers and resources.


## [1.0.6](https://github.com/grnet/agora-sp/compare/v1.0.5...v1.0.6) - 2020-09-23

### Changed

- Update default theme.
- Use better exception handling for user-add management command.

### Fixed
- Fix bugs regarding selenium testing.


## [1.0.5](https://github.com/grnet/agora-sp/compare/v1.0.4...v1.0.5) - 2020-09-15

###  Added
- Add Privacy Policy in dialog.


## [1.0.4](https://github.com/grnet/agora-sp/compare/v1.0.3...v1.0.4) - 2020-09-11

### Added
- Introduce Provider Admin role.
- Add Cookie Policy in dialog.
- Add Agora Documentation.

### Changed
- Improve error messages on ResourceAdminship creation.

### Removed
- Delete Admin role.

### Fixed
- Fix bugs regarding selenium testing.

## [1.0.3](https://github.com/grnet/agora-sp/compare/v1.0.2...v1.0.3) - 2020-07-27

### Removed
- Delete unused options and component Django apps.
- Remove unused code from project.
- Remove unused models from project.

## [1.0.2](https://github.com/grnet/agora-sp/compare/v1.0.1...v1.0.2) - 2020-07-24

### Added
- Add Privacy Policy pdf.
- Add filtering/searching/sorting options where they apply.

### Changed
- Users with role serviceadmin can edit/create Contacts belonging only to their organisation.
- Resource contacts now belong to the Resource Organisation.
- Better waits and improvements for selenium tests.

### Removed
- Delete unused organisations fixture.

### Fixed
- Fix bug with observer profile

## [1.0.1](https://github.com/grnet/agora-sp/compare/v1.0...v1.0.1) - 2020-07-02

### Added
- Add themes for EUDAT, NI4OS, and EGI.
- Add customisation option for logo.

### Fixed
- Fix bug with provider name not showing.

### Changed
- Move fixtures/users separately from populate.db script.

### Security
- Update Django version to fix vulnerability issues.
- Update node packages to fix vulnerability issues.

## [1.0](https://github.com/grnet/agora-sp/compare/v0.9.17...v1.0) - 2020-06-22

###  Added
- Add Resource model.
- Add fields according to SDTv3.0.
- Add support models for Resource and Provider.

### Changed
- Replace Service and ServiceDetails models with Resource.
- A serviceadmin can belong to just one Organisation.
- Use Provider instead of Organisation.
- Rearrange sidebar menu.

### Fixed
- Fix bug with select not working well with ember-chips.

### Removed
- Remove unused /api/v2/ endpoints.

## [0.9.17](https://github.com/grnet/agora-sp/compare/v0.9.16...v0.9.17) - 2019-12-09

###  Added
- Add footer.
- Add services-in-marketplace & services-in-catalogue endpoints.
- Add material-ui chips component.

### Changed
- Add created_at/updated_at fields to service version model.
- Add created_at/updated_at fields to service model.

### Fixed
- Fix bug with safari rendering flexbox.

## [0.9.16](https://github.com/grnet/agora-sp/compare/v0.9.15...v0.9.16) - 2019-08-27

### Added
- Expose components to anonymous users.
- Expose component connections to service versions to anonymous users.
- Basic setup of e2e testing using Cypress.
- Provide dummy user data for Dockerfile.
- Messages using Argo Messaging Service contain more information.
- Add new menu item "My Services" for serviceadmin users.
- Add icons to navigation menu items.
- Add profile page.

### Removed
- Remove unused /api/v2/my-services endpoint.
- Hide "Service Versions" from sidebar menu for serviceadmin users.

## [0.9.15](https://github.com/grnet/agora-sp/compare/v0.9.14...v0.9.15) - 2019-06-19

### Fixed
- Correct redirect url when connecting a component to a service version and a version to a service.

### Removed
- Remove unused code, mainly referring to api/v1.

## [0.9.14](https://github.com/grnet/agora-sp/compare/v0.9.13...v0.9.14) - 2019-06-12

### Changed
- Do not expose sensitive data (service owner, security  and support contact info) in public api.

### Fixed
- Fix bug preventing service providers from saving.

## [0.9.13](https://github.com/grnet/agora-sp/compare/v0.9.12...v0.9.13) - 2019-06-03

### Added
- Provide UI for Agora by merging [agora-admin](https://github.com/grnet/agora-sp-admin) repository. 

## [0.9.12](https://github.com/grnet/agora-sp/compare/v0.9.11...v0.9.12) - 2019-05-23

### Added
- Add Organisation model exposed in /providers endpoint.
- Add Access Policy model.
- Add Federation Member model.
- Services can belong to organisations.
- Serviceadmins can be assigned to organisations by superadmins.
- Add related/required services to Service model.

### Changed
- Upgrade apimas to 0.4a4.
- Extract ServiceDetails permission fields dynamically.
- Rename Service Area -> Service Category.
- A Service can belong to many service categories.
- Add/remove fields to models according to new guidelines.
- Models altered are:  Service, ServiceDetails, ServiceStatus, User.

### Fixed
- Various pep8 fixes.

## [0.9.11](https://github.com/grnet/agora-sp/compare/v0.9.10...v0.9.11) - 2019-03-05

### Added
- Serviceadmins can create components related resources.
- Serviceadmins can create/edit CIDL for services they own.
- Serviceadmins can create/edit Service Versions for services they own.

### Fixed
- Trim Service name before saving.

### Security
- Update Django version to fix vulnerability issues.

## [0.9.10](https://github.com/grnet/agora-sp/compare/v0.9.9...v0.9.10) - 2019-02-12

### Fixed
- Enable partial update actions for admins/serviceadmins.

## [0.9.9](https://github.com/grnet/agora-sp/compare/v0.9.8...v0.9.9) - 2019-02-07

### Changed
- Upgrade apimas to 0.4a3.
- Use specular instead of docular.
- Update testing code to match latest pytest deprecation notes.
- Expose Service external/internal contact information as struct.

### Fixed
- Use default values in spec for not nullable fields in model.

### Security
- Update Django version to fix vulnerability issues.

## [0.9.8](https://github.com/grnet/agora-sp/compare/v0.9.7...v0.9.8) - 2019-01-03

### Added
- Expose more fields to service-types endpoint.

### Fixed
- Enable sorting, searching and ordering of more fields.

## [0.9.7](https://github.com/grnet/agora-sp/compare/v0.9.6...v0.9.7) - 2018-11-30

### Added
- Add service-types endpoint.
- Push messages using Argo Messaging Service.
- Setup Travis CI.
- Add visible_to_marketplace field to Service Version model.

### Changed
- Expose funders_for_service to api/v1.
- Enable filtering of service versions by is_in_catalogue.

### Security
- Upgrade Django to 1.11.16.

## [0.9.6](https://github.com/grnet/agora-sp/compare/v0.9.5...v0.9.6) - 2018-09-25

### Added
- Clean html feature for rich text textarea fields.


## [v0.9.5](https://github.com/grnet/agora-sp/compare/v0.9.4...v0.9.5) - 2018-08-28

### Changed
- Add field "service_type" in CIDL model.

### Fixed
- Add forgotten migration file.

## [v0.9.4](https://github.com/grnet/agora-sp/compare/v0.9.3...v0.9.4) - 2018-07-06

### Changed
- Upgrade APIMAS.
- Update spec and permissions file according to new APIMAS.

### Added
- Add serviceowner role.
- Add service ownership functionality.
- Allow service filtering for user customers.
- Expose service customer_facing/internal attributes. 
- Expose external services in api.

### Fixed
- Remove duplicate code from spec.
- Enable custom user creation from UI.


## [v0.9.3](https://github.com/grnet/agora-sp/compare/v0.9.2...v0.9.3) - 2018-04-11

### Added
- Add superadmin role.
- Enable service logo upload.
- Dockerize app.
- Add tests.

### Changed
- Properly set up permissions for admin/observers.


### Fixed
- Remove unused settings.

## [v0.9.2](https://github.com/grnet/agora-sp/releases/tag/v0.9.2) - 2018-01-31

### Fixed
- Clean up unsafe code

### Added
- Enable user login via shibboleth.
- Send email when a new user is created.
- Expose shibboleth_id in api.
- Expose component-implementation-detail-link endpoint.
- Expose service component in api.

### Changed
- Expose user shibboleth_id in api.
- Allow filtering of resources.
