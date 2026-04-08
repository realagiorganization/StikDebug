# Assumptions

- The repository should keep its authoritative operational documentation in `docs/`, with `README.md` remaining the only required root-level narrative document.
- Behave-based contract tests are an acceptable first automation layer for principal user flows even though they model behavior rather than exercising a physical iOS device.
- VHS terminal capture is sufficient for the requested README demo because the behavior being recorded for this task is the BDD/test flow, not a simulator-driven UI recording.
- The current GitHub Actions footprint remains valid: Ubuntu for Behave/VHS work and macOS for Xcode/IPA builds.
- The existing IPA build and source-update workflows remain part of the repository and therefore should be represented in README badges.
- No new hosted backend was required for this run; if one is added later, Azure is the approved compute host for it.
