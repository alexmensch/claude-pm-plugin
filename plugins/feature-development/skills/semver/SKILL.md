---
name: semver
description: Defines what constitutes a major, minor, and patch version change according to semantic versioning conventions. Use this when determining how to bump a project's version number.
---

When a project uses semantic versioning, version numbers follow the format `MAJOR.MINOR.PATCH`. Use this skill to determine the correct version bump for a given set of changes. When a PR contains changes across multiple categories, always use the **highest applicable level**.

---

## Major version — breaking changes

Increment the major version when changes are **incompatible with the previous version**, meaning existing consumers must make changes on their end to continue working correctly.

- Removing a public API endpoint, function, method, or exported field that was previously available
  - e.g. deleting `GET /api/users/:id` that clients depend on
  - e.g. removing an exported function `formatDate()` from a public library
- Changing the signature of a public function in a way that breaks existing callers
  - e.g. removing a parameter, reordering parameters, or changing a parameter's type
  - e.g. changing a function from synchronous to asynchronous without a compatibility shim
- Changing the shape of a public data structure in a way existing consumers cannot handle
  - e.g. renaming a field in an API response from `user_id` to `userId`
  - e.g. changing a field's type from a string to an object
- Removing or renaming a CLI command, subcommand, or flag
  - e.g. renaming `--verbose` to `--log-level`
  - e.g. removing the `init` subcommand
- Changing authentication or authorisation behaviour incompatibly
  - e.g. requiring a new mandatory header on all requests
  - e.g. changing token format in a way that invalidates existing tokens
- Dropping support for a runtime, language version, or platform
  - e.g. dropping Node.js 18 support
  - e.g. removing support for a previously supported operating system
- Changing a configuration file format in a way that old configs no longer work
  - e.g. changing a flat config structure to a nested one without migration support

---

## Minor version — new backward-compatible functionality

Increment the minor version when **new functionality is added** without breaking existing consumers.

- Adding a new public API endpoint, function, method, or exported field
  - e.g. adding `GET /api/users/:id/preferences`
  - e.g. exporting a new helper function `truncateText()`
- Adding a new optional parameter to an existing function
  - e.g. adding an optional `locale` argument to a formatting function
- Adding a new CLI command, subcommand, or optional flag
  - e.g. adding a `--dry-run` flag to an existing command
  - e.g. adding a new `export` subcommand
- Adding new configuration options that have sensible defaults
  - e.g. adding an optional `timeout` field to a config file
- Introducing a new feature or capability users can opt into
  - e.g. adding dark mode support
  - e.g. adding support for a new file format
- Deprecating existing functionality (without removing it)
  - e.g. marking a function as deprecated in documentation and logs, with the replacement noted

---

## Patch version — backward-compatible bug fixes

Increment the patch version when **bugs are fixed** or **internal improvements** are made without changing the public interface.

- Fixing incorrect behaviour that caused wrong results, crashes, or errors
  - e.g. fixing an off-by-one error in a date range calculation
  - e.g. fixing a crash when an empty array is passed to a function
- Fixing a security vulnerability without changing the public interface
  - e.g. sanitising user input that was previously passed through unescaped
- Improving performance without changing observable behaviour
  - e.g. caching an expensive database query
  - e.g. reducing bundle size through code splitting
- Fixing a typo in an error message, log line, or UI label
- Internal refactoring with no observable effect on consumers
  - e.g. extracting a helper function, renaming an internal variable
- Updating a dependency to a newer patch version with no breaking changes

---

## When in doubt

If you are uncertain whether a change is breaking, treat it as **major**. It is always safer to signal a breaking change than to silently break a consumer.

If you are not certain whether the version should be updated at all, ask the user before proceeding using `AskUserQuestion` to ask them to make a decision.
