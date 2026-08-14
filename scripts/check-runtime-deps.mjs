#!/usr/bin/env node
// Check that every runtime @deepseek-ai dependency declared in package.json is
// actually installed. Guards against the PR #9 / #10 regression where
// electron-builder pruned 19 runtime packages and the packaged app crashed
// with ERR_MODULE_NOT_FOUND on startup.
//
// Run after `npm ci` in CI (and locally before packaging).
import { readFileSync, existsSync } from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const pkg = JSON.parse(readFileSync(path.join(root, 'package.json'), 'utf8'))

// The 19 runtime packages (everything under @deepseek-ai except the main
// `dsh` package itself, which npm always installs as the direct dependency).
const deps = Object.keys(pkg.dependencies)
  .filter((n) => n.startsWith('@deepseek-ai/') && n !== '@deepseek-ai/dsh')
  .sort()

const missing = []
for (const dep of deps) {
  if (!existsSync(path.join(root, 'node_modules', dep, 'package.json'))) {
    missing.push(dep)
  }
}

if (missing.length > 0) {
  console.error(`MISSING runtime deps (${missing.length}/${deps.length}):`)
  for (const m of missing) console.error(`  - ${m}`)
  process.exit(1)
}

console.log(`OK: all ${deps.length} runtime @deepseek-ai deps present`)
