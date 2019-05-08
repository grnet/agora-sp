# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Enable multiple themes functionality.
- Add Provider resource.
- Add Federation Members resource.
- Add Access Policy resource.
- Serviceadmins can be assigned to providers by superadmins.
- A Service can optionally belong to one or many providers.
- New date-formatted component.


### Changed
- Rename Service Area to Service Category.
- A Service can belong to many Service Categories.
- Add/remove fields to models according to new guidelines.

## [v0.9.8](https://github.com/grnet/agora-sp-admin/compare/v0.9.7...v0.9.8) - 2019-03-05

### Added
- Serviceadmins can create component related resources.
- Serviceadmins can create/edit Connections for services they own.
- Serviceadmins can create/edit Service Versions for services they own.

## [v0.9.7](https://github.com/grnet/agora-sp-admin/compare/v0.9.6...v0.9.7) - 2019-02-07

### Added
- Validations in service-version forms.

### Changed
- Include external/internal contact information in Service view.
- Remove contact information from sidebar navigation.
- Use PATCH in all update actions.

### Fixed
- Use default values for some fields in service-version model to ensure API
compatibility.

## [v0.9.6](https://github.com/grnet/agora-sp-admin/compare/v0.9.5...v0.9.6) - 2019-01-03

### Fixed
- Improve sorting, filtering and searching in list views.

## [v0.9.5](https://github.com/grnet/agora-sp-admin/compare/v0.9.4...v0.9.5) - 2018-11-30

### Added
- Add visible_to_marketplace field to Service Model.

### Deprecated
- Migrate away from bower.

### Changed
- Enable filtering of service versions by is_in_catalogue.

## [v0.9.4](https://github.com/grnet/agora-sp-admin/compare/v0.9.3...v0.9.4) - 2018-08-28

### Added
- "View source" mode in textarea fields.

### Changed

- Add field "service_type" in CIDL model.
- Update menu labels in "Service Components" section.

### Fixed
- Remove duplicate code from CIDL.
- Eslint fixes.
- Bug concerning user creation.

## [v0.9.3](https://github.com/grnet/agora-sp-admin/compare/v0.9.2...v0.9.3) - 2018-07-06

### Added
- Allow custom-user create/edit.
- Add role serviceowner.
- Implement service ownership functionality.

### Changed
- Use PATCH to upload image to backend

### Fixed
- Fix typos

## [v0.9.2](https://github.com/grnet/agora-sp-admin/compare/v0.9.1...v0.9.2) - 2018-04-11

### Added
- Allow service-item logo upload.
- Add role field to custom-user.
- Add superadmin/admin roles.
- Add customer_facing/external attributes to services.

### Changed
- Replace froala text editor with tinyMCE

## [v0.9.1](https://github.com/grnet/agora-sp-admin/releases/tag/v0.9.1) - 2018-01-26

### Added
- Initial version
- Implement file upload
- Enable shibboleth login
