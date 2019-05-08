# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Add Organisation model exposed in /providers endpoint.
- Add Access Policy model.
- Add Federation Member model.
- Services can belong to organisations.
- Serviceadmins can be assigned to organisations by superadmins.

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
