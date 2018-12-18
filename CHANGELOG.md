# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

| Change Type   | Description                            |
| :------------ | :------------------------------------- |
| Added         | for new features.                      |
| Changed       | for changes in existing functionality. |
| Deprecated    | for soon-to-be removed features.       |
| Removed       | for now removed features.              |
| Fixed         | for any bug fixes.                     |
| Security      | in case of vulnerabilities.            |

## [Unreleased]

- Added exposed and published ports to molecule for interactive web testing

## [3.0.0] - 2018-11-15

### Added

- Added testing of requirements.yml for other roles

### Changed

- Travis now uses a matrix of tests for each tox scenario
- Moved .yamllint into molecule scenario
- Updated README
- Changed Vagrantfile to use most recent ansible and docker-compose
- Molecule default scenario will build platforms based on environmental variables set in tox ( MOLECULE_DISTRO & MOLECULE_DOCKER_COMMAND )
- Updated Tox to test operating systems and ansible versions

### Removed

- Removed building docker container within repository
- Removed static molecule create/destroy/prepare files

### Fixed

- Fixed various idempotence issues

## [2.0.0] - 2018-10-17

### Changed

- Separated variables for configuring SnipeIT's `.env` file

[Unreleased]: https://github.com/joshuacherry/ansible-role-snipeit/compare/2.0.1...HEAD
[2.0.1]: https://github.com/joshuacherry/ansible-role-snipeit/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/joshuacherry/ansible-role-snipeit/compare/1.0.0...2.0.0
