# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Add service-types endpoint.
- Push messages using Argo Messaging Service.

### Changed
- Expose funders_for_service to api/v1.
- Enable filtering of service versions by is_in_catalogue.

### Security
- Upgrade Django to 1.11.16.

## [0.9.6] - 2018-09-25

### Added
- Clean html feature for rich text textarea fields.


## [0.9.5] - 2018-08-28

### Changed
- Add field "service_type" in CIDL model.

### Fixed
- Add forgotten migration file.
