# AGENTS.md — 案板（Anban）fork 维护指南

本文件指导任何 AI Agent（或人类）维护**案板**（Anban）——基于 dsh-desktop 的内容创作工作台。**动手前先读本文件 + BRAND.md + ROADMAP.md。**

## 这是什么

案板 = [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop)（MIT）的定制分支，定位"什么都能下锅的创作台"，为自媒体创作者（美食/历史/博物向）提供开箱即用的本地创作工作台。

## 铁律（血的教训）

1. **绝不要在运行中的 DSH profile 目录里执行 `npm install` / `pnpm add` / `pnpm install`**。
   会产生"影子 node_modules"，布局与真实依赖树不一致，运行中的实例懒加载后整个工具管线崩溃：
   `Cannot read properties of undefined (reading 'prepare')`。
   装插件用符号链接挂进父级树：
   ```sh
   ln -s <插件路径>/dsh-search-free "$DSH_HOME/profiles/node_modules/dsh-search-free"
   ```
2. **保留 dataelement 的 MIT 版权声明**（本 fork 的上游署名，法律要求，不可删）
3. **不冒充 DeepSeek 官方**（品牌红线，见 BRAND.md）
4. **密钥永不入库**（模型 key / Exa / Tavily 只放 profile 配置或凭据文件）
5. **官方 Exa 包是坏的**（缺 `@deepseek-ai/dsh-environment`），用自研 `dsh-search-free`（npm 0.1.1+）

## 上游协作

- 本仓库是 dataelement/dsh-desktop 的 fork。**上游 bug 修复以 PR 形式回馈**到 dataelement/dsh-desktop（参见已提交的 PR #10：声明运行时缺失的 19 个 @deepseek-ai 依赖）
- 上游 `main` 有新提交时，及时 `git fetch upstream && git merge upstream/main` 同步

## 常用命令

```sh
# 构建打包（mac x64/arm64）
npm run package:mac:x64    # 或 package:mac:arm64 / package:win
# 测试与类型检查
npm test
npm run typecheck
# git 凭据（本机用 gh 认证）
git config credential.helper '!gh auth git-credential'
```

## 相关项目

| 项目 | 说明 |
|---|---|
| [dsh-search-free](https://github.com/lmcsh9527/dsh-search-free) | 免费多层搜索+抓取插件（Exa→Tavily→Bing + web_fetch），npm 已发布；维护规范见其 AGENTS.md |
| dataelement/dsh-desktop | 上游桌面壳（MIT） |

## 当前本机部署（双环境）

- 网页版 profile：`~/.dsh/profiles/web/`（补丁 + 插件符号链接）
- 桌面端 profile：`~/Library/Application Support/dsh-desktop/harness/profiles/`
- 改完插件/配置后：重启对应 Harness 生效；改完仓库后如需同步到本机，把文件复制过去并重启
