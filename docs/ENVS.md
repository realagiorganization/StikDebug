# Environment Variables

The app itself currently relies more on bundle configuration, entitlements, and `UserDefaults` than shell environment variables. The variables below matter for development and CI around this repository.

## Mandatory

- `GITHUB_TOKEN`
  - Required in GitHub Actions for release creation and for the source-update workflow to push changes.
  - Provided automatically by GitHub Actions in CI.

## Optional

- `UPLOAD_IPA`
  - Consumed by `.github/workflows/build_ipa.yml`.
  - Defaults to `true`.
  - Set to `false` to skip IPA artifact upload and release publishing in CI runs where only build validation is needed.

- `DEVELOPER_DIR`
  - Optional local macOS override when a developer needs to pin a specific Xcode installation before running `xcodebuild`.
  - Not required by repository automation because CI uses `maxim-lobanov/setup-xcode`.

## Currently Unused

- No mandatory runtime environment variables are defined for the iOS app target.
- Future hosted components, if introduced, should define their Azure deployment variables here instead of scattering them across workflow files.
