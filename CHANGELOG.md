# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
