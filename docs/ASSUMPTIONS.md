# Assumptions

- Behave BDD suites are acceptable stand-ins for higher-fidelity UI automation and can run in Ubuntu CI.
- VHS terminal recording is sufficient to illustrate behavior; a placeholder GIF committed will be regenerated in CI.
- Device connection/JIT flows are represented via lightweight Python models for contract-level tests, not real device I/O.
- macOS build pipeline remains as existing `build_ipa.yml`; no change required.
