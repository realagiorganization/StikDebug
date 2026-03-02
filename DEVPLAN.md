# Development Plan for StikDebug

## Objectives
- Maintain reliable device connection and trust handling for iOS 17.4+.
- Provide auditable JIT enablement flows with live logging.
- Support mini tool execution with history and error surfacing.
- Keep CI coverage for BDD scenarios plus visual proof via VHS.

## Workstreams & Steps
1) **Environment & Tooling**
   - Xcode 15/16/26 on macOS for app builds; Python 3.11 + `behave` for BDD.
   - Install `vhs` (Charmbracelet) to record CLI flows into GIF for README.
2) **BDD Coverage**
   - Model device lifecycle (trust, reconnect) and JIT gating.
   - Cover mini tools (success + failure) and live log filtering/reconnect tail.
   - Keep features in `bdd/features`, steps in `bdd/features/steps`.
3) **CI Automation**
   - GitHub Action `bdd.yml` runs Behave on pushes/PRs; uploads artifacts.
   - `vhs-gif` job records demo GIF from `assets/demo.tape` for documentation.
4) **Release & Assets**
   - README badges for BDD status and demo GIF for quick visual verification.
   - Ensure AltSource/IPA download links stay current.

## External Dependencies
- Python 3.11 runtime for BDD (`behave==1.2.6`).
- Charmbracelet `vhs` v0.10.0 for terminal capture.
- macOS + Xcode (26.0.1 in CI) for building the IPA (existing workflow).

## Verification
- Run `behave bdd/features` locally (or via CI) to validate behavior contracts.
- Inspect generated `assets/demo.gif` from VHS to confirm user-facing flow.
- Build pipeline (`build_ipa.yml`) ensures app compiles against current SDK.
