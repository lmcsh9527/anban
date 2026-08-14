# profile-overrides — 案板 Anban 预置配置（新装即用）

让一台新装的 Mac 开箱即用（选工作区 → jy 模型对话 → web_search 能搜 → 说"帮我写个口播稿"走完整创作流程）。

## 目录

| 文件 | 作用 | 装到哪 |
|---|---|---|
| `cordis.patch.yml` | 搜索配置：freesearch provider（Exa→Tavily→Bing 降级）+ web_fetch | profile 的 `cordis.patch.yml` |
| `settings.model.yml` | 模型 provider：tokenrhythm（jy）主 / 轻舟（qingzou）备 + 模型列表 + 默认模型 | 合并进 `~/.dsh/settings.yaml` |

## 安装步骤

### 1. 搜索配置（双环境同法）

1. 把 `cordis.patch.yml` 的内容复制到目标 profile 的 `cordis.patch.yml`：
   - 网页版：`~/.dsh/profiles/web/cordis.patch.yml`
   - 桌面端：`~/Library/Application Support/dsh-desktop/harness/profiles/web/cordis.patch.yml`
2. 填入你自己的 `exaApiKey` / `tavilyApiKey`（**密钥只放本机，绝不入库**）
3. 插件用符号链接挂进父级依赖树（**绝不在 profile 里跑 npm/pnpm install**）：

   ```sh
   ln -s <dsh-search-free 路径>/dsh-search-free ~/.dsh/profiles/node_modules/dsh-search-free
   ```

4. 重启对应 Harness 生效。

### 2. 模型配置

1. 把 `settings.model.yml` 的 `llm-pi-ai` / `agent-default-model` 合并进 `~/.dsh/settings.yaml`
2. 把 `<你的中转地址>` 替换为真实端点
3. 用环境变量提供密钥：`export JY_API_KEY=...`（tokenrhythm）`export QINGZOU_API_KEY=...`（轻舟）

### 3. 创作者预设（可选）

安装 `anban-creator` 预设（见仓库 `presets/anban-creator/`）：复制到 `~/.dsh/.agent-presets/anban-creator/`，新会话选择「案板创作助手」即自动加载选题/口播稿/核查/分镜/发布五个技能。

## 铁律提醒

- ⚠️ 绝不在运行中的 profile 里执行 `npm install` / `pnpm install`（影子 node_modules → 工具管线崩溃 `prepare undefined`）
- ⚠️ 密钥永不入库：Exa / Tavily / JY / QINGZOU key 只放本机 profile 与凭据
- ⚠️ `dsh-search-free` 只依赖 `@deepseek-ai/dsh-tools`（精确 `0.1.0-rc.6`），不要引入 schemastery
