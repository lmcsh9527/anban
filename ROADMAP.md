# 案板 Anban — Phase 1 路线图（品牌化 MVP）

目标：把 dsh-desktop fork 改造成「案板工作台」，出一版 v0.2.0，自用 + 分享。

## 任务清单（按顺序）

### P1.0 仓库与品牌底座 ✅
- [x] 把 fork 仓库重命名为 **`anban`**（`gh repo rename anban` 已完成，旧链接自动重定向，PR #10 不受影响）
- [x] 应用名改为 **案板 / Anban**（`package.json` 的 `productName: Anban` + `appId: io.anban.desktop`）
- [x] 图标：`build/icon.icns` / `build/icon.ico` / `build/icon.png` 换成案板主题图标（案板+菜刀+蒸汽，`scripts/gen-icon.py` 可复现）
- [x] 侧边栏品牌：`patches/@deepseek-ai+dsh-client-ui-sidebar+0.1.0-rc.6.patch` 的 `DshDesktopLogo` 机制已替换为案板 Logo + 「案板 Anban」标语

### P1.1 自媒体技能包（核心资产，纯 markdown）✅
从创始人现有创作流程提炼，建 `skills/` 目录，每个技能一个 markdown（参照 dsh-search-free 的规范）：
- [x] `topic-mining` 选题挖掘（从 416工程/选题卡/母链建矿 的流程提炼）
- [x] `oral-script` 口播稿写作（从 biaoge/口播稿生产流水线_v1.md 提炼）
- [x] `fact-check` 事实核查（从 sugar_fact_check.md 提炼，配合 web_search）
- [x] `storyboard` 视频分镜（从视频制作流程提炼）
- [x] `publish-checklist` 发布清单（B站/YouTube 双平台）

### P1.2 创作者预设 ✅
- [x] 新建 agent preset `anban-creator`：人设（老饕+说书人，接地气）+ 自动加载上述技能（`presets/anban-creator/`，已安装到本机 `~/.dsh/.agent-presets/`）
- [x] preset 里预置：工作流说明（选题→查证→口播稿→分镜→发布，写入 persona）

### P1.3 预置配置（新装即用）✅
- [x] 提供 `profile-overrides/`：cordis.patch.yml（freesearch + web-search-free）+ 模型配置模板（jy/qingzou + 模型列表）
- [x] 安装说明：README 写明手动复制步骤（不写脚本，避免在运行中 profile 里 install）

### P1.4 工程质量 ✅
- [x] CI：`.github/workflows/release.yml` 补 mac-x64 构建验证（PR 也触发）+ 19 个运行时依赖存在性检查 job（防止 #9 回归）
- [x] `verify-target.mjs` 已存在，确认 x64 目标可用
- [x] 打包冒烟脚本：`scripts/smoke-packaged.sh`（检查 app bundle 里 19 个 @deepseek-ai 包都在）

### P1.5 文档与发布
- [x] README 改成案板介绍（中英，保留 dsh-desktop 原说明的链接）
- [x] 打 tag `v0.2.0`，发布 release（mac-arm64 + mac-x64 + win）——[v0.2.0](https://github.com/lmcsh9527/anban/releases/tag/v0.2.0)，CI 三平台构建+19 包检查+冒烟全绿
- [x] 在 README 写明：这是 dsh-desktop 的定制分支，上游修复以 PR 形式回馈（PR #10）

## 完成定义（DoD）
1. 新装一台 Mac，装案板 DMG → 右键打开 → 选工作区 → 直接能用（模型 jy 已配好、搜索能搜、web_fetch 能用）
2. 新建会话说"帮我写个口播稿"，自动走 选题→查证→成稿 流程
3. CI 全绿，19 包检查通过

## 遗留清理（并行处理）
- [x] 桌面端已装应用的插件副本升级到 dsh-search-free 0.1.1（`~/Library/Application Support/dsh-desktop/harness/profiles/web/plugins/dsh-search-free/`，web 端同步升级，重启生效）
- [x] 跟进 PR https://github.com/dataelement/dsh-desktop/pull/10（已拆出品牌 docs commit，PR 只剩 fix，待上游 review/合并）
- [x] npm token 轮换提醒（对话中暴露过，已多次提醒用户删除重建）
