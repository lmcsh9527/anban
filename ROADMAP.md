# 案板 Anban — Phase 1 路线图（品牌化 MVP）

目标：把 dsh-desktop fork 改造成「案板工作台」，出一版 v0.2.0，自用 + 分享。

## 任务清单（按顺序）

### P1.0 仓库与品牌底座
- [ ] 把 fork 仓库 `lmcsh9527/dsh-desktop` 重命名为 **`anban`**（`gh repo rename anban`，GitHub 会自动重定向旧链接，PR #10 不受影响）
- [ ] 应用名改为 **案板 / Anban**（`package.json` 的 `productName` + `appId`）
- [ ] 图标：`build/icon.icns` / `build/icon.ico` 换成案板主题图标（案板+菜刀 或 灶火元素）
- [ ] 侧边栏品牌：`patches/@deepseek-ai+dsh-client-ui-sidebar+0.1.0-rc.6.patch` 里已有 `DshDesktopLogo` 机制，替换为案板 Logo + 标语

### P1.1 自媒体技能包（核心资产，纯 markdown）
从创始人现有创作流程提炼，建 `skills/` 目录，每个技能一个 markdown（参照 dsh-search-free 的规范）：
- [ ] `topic-mining` 选题挖掘（从 416工程/选题卡/母链建矿 的流程提炼）
- [ ] `oral-script` 口播稿写作（从 biaoge/口播稿生产流水线_v1.md 提炼）
- [ ] `fact-check` 事实核查（从 sugar_fact_check.md 提炼，配合 web_search）
- [ ] `storyboard` 视频分镜（从视频制作流程提炼）
- [ ] `publish-checklist` 发布清单（B站/YouTube 双平台）

### P1.2 创作者预设
- [ ] 新建 agent preset `anban-creator`：人设（老饕+说书人，接地气）+ 自动加载上述技能 + 默认用 jy 模型
- [ ] preset 里预置：工作流说明（选题→查证→口播稿→分镜→发布）

### P1.3 预置配置（新装即用）
- [ ] 提供 `profile-overrides/`：cordis.patch.yml（freesearch + web-search-free）+ 模型配置模板（jy/qingzou + 模型列表）
- [ ] 安装后脚本把配置写入用户 profile（或 README 说明手动复制）

### P1.4 工程质量
- [ ] CI：`.github/workflows` 补 mac-x64 构建验证（当前只有 arm64 验证过）+ 19 个运行时依赖存在性检查（防止 #9 回归）
- [ ] `verify-target.mjs` 已存在，确认 x64 目标可用
- [ ] 打包冒烟脚本：`scripts/smoke-packaged.sh`（检查 app bundle 里 19 个 @deepseek-ai 包都在）

### P1.5 文档与发布
- [ ] README 改成案板介绍（中英，保留 dsh-desktop 原说明的链接）
- [ ] 打 tag `v0.2.0`，发布 release（mac-arm64 + mac-x64 + win）
- [ ] 在 GitHub Discussions/README 写明：这是 dsh-desktop 的定制分支，上游修复以 PR 形式回馈

## 完成定义（DoD）
1. 新装一台 Mac，装案板 DMG → 右键打开 → 选工作区 → 直接能用（模型 jy 已配好、搜索能搜、web_fetch 能用）
2. 新建会话说"帮我写个口播稿"，自动走 选题→查证→成稿 流程
3. CI 全绿，19 包检查通过

## 遗留清理（并行处理）
- [ ] 桌面端已装应用的插件副本升级到 dsh-search-free 0.1.1（`~/Library/Application Support/dsh-desktop/harness/profiles/web/plugins/dsh-search-free/`）
- [ ] 跟进 PR https://github.com/dataelement/dsh-desktop/pull/10
- [ ] npm token 轮换提醒（对话中暴露过，建议 npm 设置里删除重建）
