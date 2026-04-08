<div align="center">
   <img width="217" height="217" src="/assets/StikJIT.png" alt="Logo">
</div>

<div align="center">
  <h1><b>StikDebug</b></h1>
  <p><i>An on-device debugger and JIT enabler for iOS 17.4+ powered by <a href="https://github.com/jkcoxson/idevice">idevice</a>.</i></p>
</div>

<h6 align="center">
  <a href="https://discord.gg/ZnNcrRT3M8">
    <img src="https://img.shields.io/badge/Discord-join%20us-7289DA?logo=discord&logoColor=white&style=for-the-badge&labelColor=23272A" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/realagiorganization/StikDebug?label=License&color=5865F2&style=for-the-badge&labelColor=23272A" />
  </a>
  <a href="https://github.com/realagiorganization/StikDebug/stargazers">
    <img src="https://img.shields.io/github/stars/realagiorganization/StikDebug?label=Stars&color=FEE75C&style=for-the-badge&labelColor=23272A" />
  </a>
  <a href="https://github.com/realagiorganization/StikDebug/actions/workflows/bdd.yml">
    <img src="https://github.com/realagiorganization/StikDebug/actions/workflows/bdd.yml/badge.svg" alt="BDD Suite" />
  </a>
  <a href="https://github.com/realagiorganization/StikDebug/actions/workflows/build_ipa.yml">
    <img src="https://github.com/realagiorganization/StikDebug/actions/workflows/build_ipa.yml/badge.svg" alt="Build Unsigned Debug IPA" />
  </a>
  <a href="https://github.com/realagiorganization/StikDebug/actions/workflows/updatesource.yml">
    <img src="https://github.com/realagiorganization/StikDebug/actions/workflows/updatesource.yml/badge.svg" alt="Update StikJIT Source" />
  </a>
  <br />
</h6>

## What It Does

- Imports a pairing file and prepares the device-side debugging flow.
- Connects to trusted iOS devices and tolerates reconnect events.
- Enables JIT for supported apps with auditable console state.
- Streams and filters console logs for active bundles.
- Runs Mini Tools and surfaces success or failure history.

## Download

- Follow the latest workflow artifacts from [`Build Unsigned Debug IPA`](https://github.com/realagiorganization/StikDebug/actions/workflows/build_ipa.yml) for unsigned debug builds.
- Check [`Releases`](https://github.com/realagiorganization/StikDebug/releases) if this fork publishes packaged binaries.

## Code Help
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/stephendev0/stikdebug)

## Developer Docs

- [`docs/USAGE.md`](docs/USAGE.md) for local setup, BDD execution, and build commands.
- [`docs/ENVS.md`](docs/ENVS.md) for CI and local environment variables.
- [`docs/DEVPLAN.md`](docs/DEVPLAN.md) for the tracked development roadmap.
- [`docs/ASSUMPTIONS.md`](docs/ASSUMPTIONS.md) for the assumptions used in the current automation setup.
- [`docs/AGENTS.md`](docs/AGENTS.md) for the working prompts used during this task.

## Quality Gates

- Principal user flows are described in `bdd/features`.
- GitHub Actions runs the Behave contract suite and uploads a JUnit report artifact.
- GitHub Actions also records the terminal demo from `assets/demo.tape` and publishes the GIF artifact.

## License

StikDebug is licensed under **AGPL-3.0**. See [`LICENSE`](LICENSE) for details.

## Demo

<div align="center">
  <img src="assets/demo.gif" alt="BDD contract suite demo" width="640" />
</div>
