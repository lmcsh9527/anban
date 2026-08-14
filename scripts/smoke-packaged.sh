#!/usr/bin/env bash
# Smoke-test a packaged Anban app bundle: verify all 19 runtime @deepseek-ai
# packages actually shipped inside the bundle (guards against the PR #9 / #10
# packaging regression where the app crashed with ERR_MODULE_NOT_FOUND).
#
# Usage: scripts/smoke-packaged.sh <path-to-Anban.app>
set -euo pipefail

BUNDLE="${1:?usage: scripts/smoke-packaged.sh <path-to-Anban.app>}"
NM="$BUNDLE/Contents/Resources/app/node_modules"

if [ ! -d "$NM" ]; then
  echo "❌ node_modules not found at $NM (is this a packaged .app?)"
  exit 1
fi

DEPS=$(node -e '
  const p = require("./package.json");
  console.log(
    Object.keys(p.dependencies)
      .filter((n) => n.startsWith("@deepseek-ai/") && n !== "@deepseek-ai/dsh")
      .join("\n")
  );
')

MISSING=0
COUNT=0
while IFS= read -r dep; do
  [ -z "$dep" ] && continue
  COUNT=$((COUNT + 1))
  if [ ! -d "$NM/$dep" ]; then
    echo "❌ MISSING: $dep"
    MISSING=1
  fi
done <<< "$DEPS"

if [ "$MISSING" = "1" ]; then
  echo "❌ $COUNT runtime deps checked, some missing in bundle"
  exit 1
fi

echo "✅ $COUNT runtime @deepseek-ai deps present in bundle: $BUNDLE"
