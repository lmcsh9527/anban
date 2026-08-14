<h1 align="center">
  <img src="build/icon.png" width="64" alt="Anban logo" valign="middle" />
  案板 Anban
</h1>

<p align="center">
  <strong>什么都能下锅的创作台。</strong><br />
  <em>The creation bench where everything goes into the pot.</em>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh.md">简体中文</a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-171513.svg" /></a>
  <img alt="macOS" src="https://img.shields.io/badge/macOS-Apple%20Silicon%20%7C%20Intel-171513.svg" />
  <img alt="Windows" src="https://img.shields.io/badge/Windows-x64-171513.svg" />
</p>

案板 (Anban) is a **local-first content creation workbench** for food / history / natural-history creators, built on top of the DeepSeek Harness desktop shell. Put your raw material on the board — cutting, mincing, stir-frying, plating are Anban's job.

It combines three things:

- **DSH Desktop shell** — a fork of [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) (MIT), a cross-platform desktop wrapper around [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).
- **Free search stack** — [dsh-search-free](https://github.com/lmcsh9527/dsh-search-free): multi-layer web search (Exa → Tavily → Bing auto-fallback) + `web_fetch`, no paid official search package needed.
- **Creator skill pack** — a five-step creation pipeline distilled from real creator workflows.

> [!IMPORTANT]
> Anban is an early preview pinned to `@deepseek-ai/dsh@0.1.0-rc.6`. Current builds are not code-signed or notarized by Apple and are not recommended for production use.

## The creation pipeline

Say **“帮我写个口播稿”** (help me write a voice-over script) and Anban walks the full pipeline:

| Step | Skill | What it does |
|---|---|---|
| 1 | `topic-mining` | Mine topics from your material pool & trends into topic cards (hook / audience / angle / series / verifiability) |
| 2 | `fact-check` | Multi-source verification of every concrete fact (numbers, dates, names) via `web_search`, with confidence levels |
| 3 | `oral-script` | Write the script in a 老饕 (foodie) + storyteller tone: hook → story arc → spoken-language rewrite → golden line |
| 4 | `storyboard` | Turn the script into a shot list (visuals / captions / SFX / pacing) with a footage checklist |
| 5 | `publish-checklist` | Pre-publish & post-publish checklist for Bilibili + YouTube (titles, covers, descriptions, series, 48h review) |

Skills live in [`skills/`](skills/) and are auto-loaded by the [`anban-creator`](presets/anban-creator/) agent preset (老饕 + 说书人 persona, grounded, never fabricates history).

## Download

| Platform | Package | Download |
| --- | --- | --- |
| macOS Apple Silicon | DMG installer | [Download for Apple Silicon](https://github.com/lmcsh9527/anban/releases/latest/download/anban-mac-arm64.dmg) |
| macOS Intel | DMG installer | [Download for Intel Mac](https://github.com/lmcsh9527/anban/releases/latest/download/anban-mac-x64.dmg) |
| Windows x64 | Setup installer | [Download Windows installer](https://github.com/lmcsh9527/anban/releases/latest/download/anban-windows-x64-setup.exe) |
| Windows x64 | Portable executable | [Download portable version](https://github.com/lmcsh9527/anban/releases/latest/download/anban-windows-x64-portable.exe) |

All current and historical packages are on the [GitHub Releases page](https://github.com/lmcsh9527/anban/releases).

## Quick start (new install)

1. Install the DMG, right-click → Open (unsigned build).
2. Choose a workspace.
3. The default model is **jy** (tokenrhythm relay) — configure per [profile-overrides/settings.model.yml](profile-overrides/settings.model.yml) (keys via `JY_API_KEY` env, never committed).
4. `web_search` works out of the box with the free search stack — configure per [profile-overrides/cordis.patch.yml](profile-overrides/cordis.patch.yml) and symlink the plugin into the parent tree (never `npm install` inside a live profile).
5. Start a session on the **案板创作助手** preset and say “帮我写个口播稿”.

See [profile-overrides/README.md](profile-overrides/README.md) for both environments (web profile `~/.dsh/profiles/web/`, desktop profile under `~/Library/Application Support/dsh-desktop/harness/profiles/`).

## Development

```bash
git clone https://github.com/lmcsh9527/anban.git
cd anban
npm install        # runs patch-package + brand-asset install + Electron runtime
npm run dev        # electron-vite dev
```

Quality checks:

```bash
npm test
npm run typecheck
npm run build
node scripts/check-runtime-deps.mjs   # 19 runtime @deepseek-ai deps present
```

Packaging (run on the matching platform/arch):

```bash
npm run package:mac:arm64
npm run package:mac:x64
npm run package:win
scripts/smoke-packaged.sh <path-to-Anban.app>   # verify the 19 runtime deps shipped
```

CI (`.github/workflows/release.yml`) builds macOS arm64 + Intel + Windows x64, checks the 19 runtime deps, and publishes a GitHub Release on tags.

## Runtime architecture

The upstream shell architecture is unchanged: Anban is a fork of dataelement/dsh-desktop, which launches a local Harness instance on a random `127.0.0.1` port, persists profiles/plugins/sessions outside the app install directory, and hardens the BrowserWindow. See the [upstream README](https://github.com/dataelement/dsh-desktop) for the full architecture.

## Upstream collaboration

- This repository is a **fork of [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) (MIT)**. The upstream MIT attribution is kept (see [LICENSE](LICENSE)).
- Upstream bug fixes are contributed back as PRs — e.g. [PR #10](https://github.com/dataelement/dsh-desktop/pull/10) (declare the 19 runtime `@deepseek-ai` deps so electron-builder bundles them).
- The `main` branch stays clean for upstream PRs; Anban development lives on `anban-brand`.

## Related projects

| Project | Description |
|---|---|
| [dsh-search-free](https://github.com/lmcsh9527/dsh-search-free) | Free multi-layer search + fetch plugin (Exa → Tavily → Bing + `web_fetch`), published on npm |
| [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | Upstream desktop shell (MIT) |

## License

[MIT](LICENSE) © lmcsh9527, on top of the dataelement/dsh-desktop MIT base (upstream attribution retained).

DeepSeek Harness and its dependencies remain subject to their respective upstream licenses and trademark policies. Anban is an independent community project and is not affiliated with DeepSeek.
