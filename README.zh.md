<h1 align="center">
  <img src="build/icon.png" width="64" alt="案板 logo" valign="middle" />
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

**案板（Anban）** 是为美食 / 历史 / 博物向内容创作者打造的**本地优先创作工作台**——基于 DeepSeek Harness 桌面端。你只管把素材往案板上一放，切、剁、炒、装盘，都是它的事。

它由三块拼成：

- **DSH 桌面壳**：fork 自 [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop)（MIT）的跨平台桌面壳，包装 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)
- **免费搜索栈**：[dsh-search-free](https://github.com/lmcsh9527/dsh-search-free)——多层网络搜索（Exa → Tavily → Bing 自动降级）+ `web_fetch`，不用官方付费搜索包
- **自媒体技能包**：从真实创作流程提炼的五步创作流水线

> [!IMPORTANT]
> 案板目前是早期预览版，锁定 `@deepseek-ai/dsh@0.1.0-rc.6`。当前构建未经 Apple 签名与公证，不建议生产使用。

## 创作流水线

说一句**“帮我写个口播稿”**，案板自动走完整流程：

| 步骤 | 技能 | 作用 |
|---|---|---|
| 1 | `topic-mining` 选题挖掘 | 从素材池/趋势挖选题，出选题卡（钩子/受众/角度/母链/可查证性） |
| 2 | `fact-check` 事实核查 | 用 `web_search` 对每个具体事实（数字/年代/人名/地名）多源验证，标注置信度 |
| 3 | `oral-script` 口播稿 | 老饕 + 说书人调性：钩子 → 故事线 → 口语化改写 → 金句 |
| 4 | `storyboard` 视频分镜 | 口播稿转分镜脚本（画面/字幕/音效/节奏）+ 素材清单 |
| 5 | `publish-checklist` 发布清单 | B站/YouTube 双平台发布前检查 + 48h 复盘 |

技能文件在 [`skills/`](skills/)，由 [`anban-creator`](presets/anban-creator/) 创作者预设自动加载（老饕+说书人人设，接地气，绝不编造史实）。

## 下载

| 平台 | 安装包 | 下载 |
| --- | --- | --- |
| macOS Apple Silicon | DMG | [Apple Silicon 版](https://github.com/lmcsh9527/anban/releases/latest/download/anban-mac-arm64.dmg) |
| macOS Intel | DMG | [Intel Mac 版](https://github.com/lmcsh9527/anban/releases/latest/download/anban-mac-x64.dmg) |
| Windows x64 | 安装程序 | [Windows 安装版](https://github.com/lmcsh9527/anban/releases/latest/download/anban-windows-x64-setup.exe) |
| Windows x64 | 便携版 | [Windows 便携版](https://github.com/lmcsh9527/anban/releases/latest/download/anban-windows-x64-portable.exe) |

全部历史版本见 [GitHub Releases](https://github.com/lmcsh9527/anban/releases)。

## 快速开始（新装）

1. 安装 DMG，右键 → 打开（未签名构建）
2. 选工作区
3. 默认模型 **jy**（tokenrhythm 中转）——按 [profile-overrides/settings.model.yml](profile-overrides/settings.model.yml) 配置（密钥走 `JY_API_KEY` 环境变量，绝不入库）
4. `web_search` 开箱即用（免费搜索栈）——按 [profile-overrides/cordis.patch.yml](profile-overrides/cordis.patch.yml) 配置，插件用符号链接挂进父级依赖树（**绝不在运行中的 profile 里 npm install**）
5. 新会话选「**案板创作助手**」预设，说“帮我写个口播稿”

双环境安装细节见 [profile-overrides/README.md](profile-overrides/README.md)（网页版 `~/.dsh/profiles/web/`、桌面端 `~/Library/Application Support/dsh-desktop/harness/profiles/`）。

## 开发

```bash
git clone https://github.com/lmcsh9527/anban.git
cd anban
npm install        # 自动跑 patch-package + 品牌资源安装 + Electron 运行时
npm run dev        # electron-vite dev
```

质量检查：

```bash
npm test
npm run typecheck
npm run build
node scripts/check-runtime-deps.mjs   # 19 个运行时 @deepseek-ai 依赖存在性
```

打包（在对应平台/架构上执行）：

```bash
npm run package:mac:arm64
npm run package:mac:x64
npm run package:win
scripts/smoke-packaged.sh <Anban.app 路径>   # 冒烟：bundle 内 19 个运行时依赖齐全
```

CI（`.github/workflows/release.yml`）构建 macOS arm64 + Intel + Windows x64、检查 19 个运行时依赖、打 tag 自动发布 Release。

## 运行时架构

上游壳架构保持不变：案板 fork 自 dataelement/dsh-desktop——启动本地 Harness 实例（随机 `127.0.0.1` 端口）、把 profile/插件/会话放在应用安装目录之外（升级不丢数据）、加固 BrowserWindow。完整架构见[上游 README](https://github.com/dataelement/dsh-desktop)。

## 上游协作

- 本仓库是 [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop)（MIT）的 **fork**，上游 MIT 署名保留（见 [LICENSE](LICENSE)）
- 上游 bug 修复以 PR 回馈——例如 [PR #10](https://github.com/dataelement/dsh-desktop/pull/10)（声明 19 个运行时 `@deepseek-ai` 依赖，让 electron-builder 打包进 bundle）
- `main` 分支保持干净供上游 PR 使用；案板开发在 `anban-brand` 分支

## 相关项目

| 项目 | 说明 |
|---|---|
| [dsh-search-free](https://github.com/lmcsh9527/dsh-search-free) | 免费多层搜索+抓取插件（Exa → Tavily → Bing + web_fetch），npm 已发布 |
| [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | 上游桌面壳（MIT） |

## 许可证

[MIT](LICENSE) © lmcsh9527，叠加在 dataelement/dsh-desktop MIT 基础之上（保留上游署名）。

DeepSeek Harness 及其依赖遵循各自上游许可证与商标政策。案板是独立社区项目，与 DeepSeek 官方无关。
