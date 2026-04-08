# Developer Usage

## Prerequisites

- macOS with Xcode 26.x for app builds.
- Python 3.11 for the BDD suite.
- Optional: `vhs` if you want to regenerate the demo GIF locally instead of through CI.

## Repository Setup

```bash
git clone https://github.com/realagiorganization/StikDebug.git
cd StikDebug
python3 -m pip install -r bdd/requirements.txt
```

## Run the BDD Suite

```bash
python3 -m behave bdd/features
```

To produce the same style of report the CI job uploads:

```bash
mkdir -p reports/behave
python3 -m behave --format progress2 --junit --junit-directory reports/behave bdd/features
```

## Regenerate the Demo GIF

If `vhs` is installed locally:

```bash
vhs assets/demo.tape
```

The committed tape runs the BDD suite and writes `assets/demo.gif`.

## Build the App Locally

```bash
xcodebuild clean archive \
  -project StikDebug.xcodeproj \
  -scheme "StikDebug" \
  -configuration Debug \
  -archivePath build/StikDebug.xcarchive \
  -sdk iphoneos \
  -destination 'generic/platform=iOS' \
  ONLY_ACTIVE_ARCH=NO \
  CODE_SIGN_IDENTITY="" \
  CODE_SIGNING_REQUIRED=NO \
  CODE_SIGNING_ALLOWED=NO \
  SWIFT_OPTIMIZATION_LEVEL="-Onone" \
  IPHONEOS_DEPLOYMENT_TARGET=17.4
```

## CI Workflows

- `BDD Suite`: runs Behave and records the VHS demo.
- `Build Unsigned Debug IPA`: archives the app and uploads a debug IPA artifact.
- `Update StikJIT Source`: refreshes source metadata when release automation requires it.

## Deployment Note

The iOS app is primarily distributed as an artifact/release today. If the project adds hosted services or a docs site with server-side processing, plan those workloads on Azure.
