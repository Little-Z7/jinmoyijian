# 多平台安装指南

本指南帮助没有开发经验的用户，把 `npc-motorcycle-opinion-assistant` 安装到支持 Agent Skills 的 AI 工具中。兼容性按官方资料分级；“覆盖某工具”不代表该工具一定支持持久安装或具备操作网页的能力。

> [!IMPORTANT]
> 安装或自动触发本 Skill，不等于授权提交意见。验证码、登录和个人信息必须由用户本人处理；每次最终提交前仍需展示完整内容并取得本次确认。严禁批量、重复、冒名、定时投稿或绕过网站限制。安装前请阅读 [免责声明](DISCLAIMER.md) 和 [禁止滥用与可接受使用政策](ACCEPTABLE_USE.md)。

## 下载地址

- 国内优先（Gitee）：<https://gitee.com/tangenzhe/jinmoyijian>
- GitHub：<https://github.com/Little-Z7/jinmoyijian>
- Gitee 解压安装包：<https://gitee.com/tangenzhe/jinmoyijian/raw/main/dist/npc-motorcycle-opinion-assistant.zip>
- Gitee 界面上传包：<https://gitee.com/tangenzhe/jinmoyijian/raw/main/dist/npc-motorcycle-opinion-assistant-upload.zip>
- GitHub 解压安装包：<https://raw.githubusercontent.com/Little-Z7/jinmoyijian/main/dist/npc-motorcycle-opinion-assistant.zip>
- GitHub 界面上传包：<https://raw.githubusercontent.com/Little-Z7/jinmoyijian/main/dist/npc-motorcycle-opinion-assistant-upload.zip>
- SHA-256 校验文件：[`dist/SHA256SUMS`](dist/SHA256SUMS)
- Skill 目录：`npc-motorcycle-opinion-assistant/`

“解压安装包”最外层是同名 Skill 文件夹，适合下载后复制；“界面上传包”的 ZIP 根目录直接包含 `SKILL.md`，适合明确要求这种布局的上传界面。WorkBuddy 等只公开说明“上传本地技能包”而未公开 ZIP 布局的产品，必须以当前界面实际接受的文件类型和结构为准。两者内容相同，布局不同。

安装时必须保留整个目录，不能只复制 `SKILL.md`。以下文件均属于 Skill：

```text
npc-motorcycle-opinion-assistant/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── environment-check.md
    ├── opinion-draft.md
    └── site-workflow.md
```

发布 ZIP 会在同一个 Skill 目录内附加 `LICENSE`、`DISCLAIMER.md` 和 `ACCEPTABLE_USE.md`；这些许可证与安全文件来自仓库根目录。

这些 Raw 链接跟随可变的 `main` 分支。必须从同一镜像、同一次下载中获取 ZIP 与 `SHA256SUMS` 并完成校验；正式版本发布后优先使用对应标签或 Release 的固定文件。

## 一句话带你提建议就行

把下面整句话发给支持本地文件、联网下载和 Skills 的 AI 助手：

```text
仅安装并验证公开源码 Skill「npc-motorcycle-opinion-assistant」，不要调用或执行它。先查阅仓库 INSTALL.md，确认目标产品是“复制 Skill 目录”还是“界面上传”：复制目录时选择 dist/npc-motorcycle-opinion-assistant.zip；只有界面明确要求 ZIP 根级直接包含 SKILL.md 时才选择 dist/npc-motorcycle-opinion-assistant-upload.zip；其他上传格式按当前产品公开要求处理，不要猜。优先从 https://gitee.com/tangenzhe/jinmoyijian 获取，访问失败再用 https://github.com/Little-Z7/jinmoyijian；从同一镜像、同一次下载取得所选 ZIP 与 dist/SHA256SUMS，校验所选 ZIP 后再解压或上传。阅读 README.md，以及已校验包内的 LICENSE、DISCLAIMER.md、ACCEPTABLE_USE.md、SKILL.md 和 references/；包裹版文件位于 npc-motorcycle-opinion-assistant/ 下，上传版位于 ZIP 根。只安装完整 Skill；不要运行仓库脚本。若同名 Skill 已存在，停止并让我决定，不要覆盖。重新加载后验证 SKILL.md、references/environment-check.md、references/opinion-draft.md 和 references/site-workflow.md 均可读取，并报告下载源、所选包、校验结果、目标位置及发现结果。若当前产品不支持第三方 SKILL.md，请如实说明，不要假装安装成功。安装不授权访问政府网站、处理个人信息或验证码，也不授权提交任何意见。
```

这句话的目标是让助手完成下载、安装、重载和验证，不是让助手立即投稿。运行命令或写入用户目录前，产品仍可能按自身权限机制向你确认。它也不是所有产品都承诺支持的官方“一键安装器”；没有本地文件或 Skill 导入能力的产品只能提供人工步骤。

## 是否真的安装成功

至少满足以下四项才算成功：

1. 产品显示或列出了 `npc-motorcycle-opinion-assistant`；
2. `SKILL.md`、`references/environment-check.md`、`references/opinion-draft.md` 和 `references/site-workflow.md` 均可读取；
3. 新会话中说“帮我填写禁摩意见”时，助手说明正在使用该 Skill，或允许手动选中它；
4. 助手没有因为“自动触发”而跳过验证码、身份信息接管或最终提交确认。

只收到一句“安装好了”但没有目录、技能列表或界面状态佐证，不算验证成功。

## 运行前环境检查

安装成功后，每次真正调用本 Skill 都会先检查当前会话是否具备网页操作能力。这个检查适用于本指南覆盖的全部产品：OpenAI Codex、Claude Code、Cursor、Gemini CLI、OpenCode、Pi Coding Agent、Kimi、Kimi Work、Kimi Code、MiniMax Agent、MiniMax Code、Google Antigravity、WorkBuddy、千问办公、豆包、豆包工作、TraeCode、TraeWork、Qoder、Qoder CLI 和 QoderWork。

1. 优先确认能否连接用户明确指定的现有登录浏览器；只能新开隔离浏览器时必须说明不会自动继承登录态。
2. 依次判断当前会话是否实际提供 Browser Use、浏览器控制、Playwright 或 Computer Use，而不是只看产品是否安装了 Skill。
3. 工具已安装但关闭、未连接或未授权时，只按当前产品实际可见的设置入口引导用户开启，随后用读取 URL、标题或页面可见文字的无副作用动作验证。
4. 没有任何网页控制能力时切换为人工协作：助手给出导航、正文和核对清单，用户操作网页；不能声称已预填或已提交。
5. 登录状态失效时，仅在尚未进入提交阶段、页面没有待保存内容且不会重发 POST 时普通刷新一次；否则不刷新并交由用户本人处理。不读取或搬运 Cookie、令牌和密码。

不同产品对这些能力的命名和开放范围不同。出现 Browser Use、Browser、Chrome、Playwright、Computer Use 等名称时仍要检查其工具说明与实时可调用状态；不要猜测隐藏开关，也不要为了启用能力关闭安全确认。完整规则见 [`references/environment-check.md`](npc-motorcycle-opinion-assistant/references/environment-check.md)。

## 支持矩阵

状态含义：**官方目录**表示官方资料明确公开 `SKILL.md` 目录；**官方上传**表示官方只保证从界面上传；**适配后支持**表示需要产品插件格式；**仅临时兼容**表示只能把文件作为当前对话资料，不是持久安装。

| 产品 | 状态 | 推荐安装方式 | 调用或验证 |
| --- | --- | --- | --- |
| OpenAI Codex | 官方目录 | `~/.agents/skills/` 或项目 `.agents/skills/`；也可让 `$skill-installer` 处理仓库 | `/skills`、`$npc-motorcycle-opinion-assistant` |
| Claude Code | 官方目录 | `~/.claude/skills/` 或项目 `.claude/skills/` | `/npc-motorcycle-opinion-assistant` |
| Cursor | 官方目录 | `~/.agents/skills/`、`~/.cursor/skills/` 或对应项目目录 | `/npc-motorcycle-opinion-assistant` 或自动触发 |
| Gemini CLI | 官方目录/命令 | `gemini skills link <本地目录>`、`~/.gemini/skills/` 或 `.agents/skills/` | `/skills reload`、`/skills list` |
| OpenCode | 官方目录 | `~/.config/opencode/skills/`、`~/.agents/skills/` 或项目目录 | 新会话观察 Skill 加载 |
| Pi Coding Agent | 官方目录/包 | `pi install <Gitee Git URL>`（本仓库含 Pi 清单），或 `~/.pi/agent/skills/` | `pi list`、`/skill:npc-motorcycle-opinion-assistant` |
| Kimi Code CLI | 官方目录 | `~/.kimi-code/skills/`、`~/.agents/skills/` 或项目目录 | `/skill:npc-motorcycle-opinion-assistant` |
| Kimi Work | 官方上传 | Skills 面板上传本地技能 | 输入 `/` 或从技能列表选择 |
| Kimi 普通聊天 | 第三方持久导入未核验 | 仅使用当前产品实际可见的 Skills 入口；否则只作当前对话资料 | 不得把临时读取说成安装 |
| MiniMax Code / MiniMax Agent | 适配后支持 | 官方以 Agent Plugin/插件市场为主；本仓库当前不是 MiniMax 插件 | 不得把临时读取说成安装 |
| Google Antigravity 桌面/IDE | 官方目录 | 项目 `.agents/skills/`；不同形态的全局目录见后文 | 新会话自然语言触发 |
| WorkBuddy | 官方上传 | “添加技能 → 上传技能”，按当前界面要求选择本地包 | 在已安装技能列表核验 |
| 千问办公（QwenWork） | 官方目录/对话安装 | 仓库链接对话安装、上传，或 `~/.qwenworkcn/skills/` | 输入 `/`、从“我的安装”选择 |
| 豆包工作 | 外部 Skill 导入未核验 | 最新桌面端“工作任务”中仅使用实际可见且明确支持第三方 Skill 的入口 | 没有入口即停止 |
| 豆包普通聊天 | 仅临时兼容 | 上传文件或读取仓库，仅用于当前对话 | 明确提示“未持久安装” |
| TraeCode | 官方目录/上传 | `.trae/skills/`、全局 `~/.trae-cn/skills/` 或技能界面 | 在技能与命令页面核验 |
| TraeWork | 官方上传 | 插件市场 → 技能 → 上传“界面上传包” | 在已安装技能中核验 |
| Qoder IDE | 官方上传 | Extensions → Skills → Add Skills → Upload Skill | 输入 `/` 选择 |
| Qoder CLI | 官方目录 | `~/.qoder/skills/` 或项目 `.qoder/skills/` | `/skills reload`、`/skills` |
| QoderWork | 官方目录/对话安装 | 仓库链接对话安装、上传，或 `~/.qoderwork/skills/` | 输入 `/` 或技能列表 |

产品迭代很快；本表于 **2026-09-02** 按公开资料核对。界面与本表冲突时，以产品当前官方说明和实际可见入口为准，不要让助手猜测或写入未经确认的隐藏目录。`agents/openai.yaml` 是 Codex 专属元数据，其他工具可忽略；能读取 `SKILL.md` 也不等于具备操作浏览器、保留登录态或安全交接验证码的能力。

## 各工具安装提示词

以下提示词都只授权安装与验证，不授权打开政府网站或提交意见。

### WorkBuddy

```text
请只协助安装，不执行 Skill：先阅读 https://gitee.com/tangenzhe/jinmoyijian 的免责声明与禁止滥用政策（失败再用 GitHub 镜像）；如果当前 WorkBuddy 能调用“添加技能 → 上传技能”，请先告诉我界面实际接受的文件类型，再选择符合该要求的本地技能包并在已安装列表核验。不要假定 ZIP 根布局一定兼容；若格式不匹配或没有入口就停止，不要假装安装成功，也不要访问或提交任何意见。
```

官方确认的手动路径是“添加技能 → 上传技能”。公开资料没有给出 WorkBuddy 自身的固定磁盘目录，也没有保证粘贴任意 Git URL 就能自动安装；不要把 CodeBuddy Code 的目录硬套到 WorkBuddy。

### TraeCode 与 TraeWork

```text
请只安装并验证，不执行 Skill：从 https://gitee.com/tangenzhe/jinmoyijian 获取 npc-motorcycle-opinion-assistant，先阅读安全文件；TraeCode 请把完整目录复制到当前项目 .trae/skills/npc-motorcycle-opinion-assistant/，TraeWork 请准备并上传 dist/npc-motorcycle-opinion-assistant-upload.zip。若目标已存在或当前版本没有官方技能入口，停止并告诉我，不要覆盖，也不要访问政府网站。
```

- TraeCode 项目级：`.trae/skills/npc-motorcycle-opinion-assistant/`。
- TraeCode 全局：macOS/Linux 为 `~/.trae-cn/skills/npc-motorcycle-opinion-assistant/`；Windows 为 `%USERPROFILE%/.trae-cn/skills/npc-motorcycle-opinion-assistant/`。
- TraeCode 还可在“设置 → 技能与命令”中上传，并可启用 `.agents/skills/` 兼容目录。
- TraeWork：插件市场 → 技能 → 上传技能。上传包根目录必须直接包含 `SKILL.md`，因此使用本仓库的 `-upload.zip`，不要上传整个仓库 ZIP。

### Qoder、Qoder CLI 与 QoderWork

```text
请从 https://gitee.com/tangenzhe/jinmoyijian （失败时改用 https://github.com/Little-Z7/jinmoyijian）下载 npc-motorcycle-opinion-assistant 完整目录，先审查免责声明与全部文件，再按当前产品的官方用户级 Skills 机制安装，重新加载技能并确认能自动匹配“禁摩意见”等触发词；现在只安装验证，不访问或提交任何意见。
```

- Qoder IDE：Extensions → Skills → Add Skills → Upload Skill，优先使用界面上传包。
- Qoder CLI：复制到 `~/.qoder/skills/npc-motorcycle-opinion-assistant/`，执行 `/skills reload`，再用 `/skills` 查看。
- QoderWork：可在对话中提供仓库链接让其下载指定子目录，也可从技能界面上传；用户级目录为 `~/.qoderwork/skills/npc-motorcycle-opinion-assistant/`。

### 豆包与豆包工作

豆包桌面端的相关入口可能显示为“工作任务”。目前引用的官方公开资料没有确认豆包工作可导入任意外部 `SKILL.md`、固定用户目录或 Gitee 仓库；普通豆包聊天同样没有已核验的外部 Agent Skills 持久安装能力。这里只提供条件式操作，不能据此宣称兼容。

```text
请先确认我使用的是最新版豆包桌面端“工作任务”。只下载并审查 https://gitee.com/tangenzhe/jinmoyijian 的界面上传包；如果当前界面实际显示第三方 Skill 上传入口，再导入并在技能列表核验。若没有入口，请明确说明当前版本不能持久安装并停止，不要把临时读取说成安装，也不要开始提交意见。
```

普通豆包聊天只能使用下面的临时兼容提示词：

```text
请读取 https://gitee.com/tangenzhe/jinmoyijian 中 npc-motorcycle-opinion-assistant/SKILL.md 和 references；如果无法读取，请让我上传这些文件。仅在本次对话按其安全规则协助，不能持久安装时必须明确说明，也不要执行最终提交。
```

不要把以下行为写成“安装成功”：只打开仓库网页、把 `SKILL.md` 临时粘贴进一次对话、创建一个同名普通智能体，或仅口头承诺以后遵循。

### Kimi、Kimi Work 与 Kimi Code

```text
我使用 Kimi Work。请优先从 https://gitee.com/tangenzhe/jinmoyijian 获取已校验的本地技能包（失败再用 GitHub 镜像），阅读免责声明后通过当前 Skills 面板的本地上传入口安装，确认 references 文件齐全并在新会话测试“禁摩意见”能触发；本次只安装，不执行网页提交。
```

- Kimi Work：官方资料确认可上传本地技能；仅使用当前 Skills 面板公开的上传入口，安装后输入 `/` 检查。
- Kimi 普通聊天：官方资料仅确认 Skills 市场、对话创建及生态概念，没有确认任意第三方 `SKILL.md` 或 ZIP 的持久导入。只能在实际出现明确导入入口时尝试；否则将文件作为当前对话资料并明确“未安装”。
- Kimi Code：复制到 `~/.kimi-code/skills/npc-motorcycle-opinion-assistant/`，或通用目录 `~/.agents/skills/npc-motorcycle-opinion-assistant/`；重开会话后用 `/skill:npc-motorcycle-opinion-assistant` 调用。可使用这句：`请只安装并验证，不执行 Skill：从 Gitee 镜像下载并审查仓库，把完整 Skill 目录复制到 ~/.kimi-code/skills/，确认 environment-check.md、opinion-draft.md 和 site-workflow.md 均可读；目标已存在时停止，不要覆盖。`
- Kimi Code 的 Git 仓库插件直装只明确支持 GitHub；Gitee 应先克隆到本地再复制 Skill 目录，或使用 HTTP(S) ZIP。不要把本仓库当成带 `kimi.plugin.json` 的 Kimi 插件。

### MiniMax Agent 与 MiniMax Code

MiniMax 的公开资料确认其 Agent/Code 产品支持插件内 Skills，但官方主要分发形态是 Agent Plugin、插件市场或插件 ZIP。本仓库当前是通用 Skill，而不是带 `.minimax-plugin/plugin.json` 的 MiniMax 插件，因此不能声称可直接安装。

```text
请只核验当前 MiniMax Agent 或 MiniMax Code 是否允许导入一个通用 SKILL.md 目录；先审查 https://gitee.com/tangenzhe/jinmoyijian 的安全政策。若产品要求 MiniMax Agent Plugin，请明确说明本仓库尚无该适配层并停止，不要猜测隐藏目录、不要把临时阅读说成安装，也不要执行意见提交。
```

### Gemini CLI

```text
请优先从 https://gitee.com/tangenzhe/jinmoyijian 下载仓库（失败再用 GitHub 同名仓库），把 npc-motorcycle-opinion-assistant 完整目录安装为 Gemini CLI 用户级 Agent Skill，完成后提醒我在交互会话执行 /skills reload 和 /skills list 验证；现在不要运行该 Skill。
```

仓库下载到本地后，推荐链接本地目录：

```bash
gemini skills link ./npc-motorcycle-opinion-assistant
```

`gemini skills install` 用于远程 Git 仓库或本地 `.skill` 包，不用于这个本地目录。也可复制到 `~/.gemini/skills/npc-motorcycle-opinion-assistant/` 或 `~/.agents/skills/npc-motorcycle-opinion-assistant/`，再执行 `/skills reload`。需要工作区级链接时给 `link` 加 `--scope workspace`；项目 Skill 需要信任工作区。

### Google Antigravity

```text
请从 https://gitee.com/tangenzhe/jinmoyijian （失败再用 GitHub 同名仓库）下载 npc-motorcycle-opinion-assistant 完整目录，阅读免责声明后，将它安装到 Antigravity 官方支持的用户级 Skills 目录并验证名称可被发现；以后在禁摩意见相关任务中自动启用，但本次只安装，不访问政府网站或提交。
```

- 项目级：`<项目>/.agents/skills/npc-motorcycle-opinion-assistant/`。
- Antigravity 桌面产品全局：`~/.gemini/config/skills/npc-motorcycle-opinion-assistant/`。
- Antigravity for IDEs 全局：`~/.gemini/antigravity/skills/npc-motorcycle-opinion-assistant/`。
- Antigravity CLI 全局：`~/.gemini/antigravity-cli/skills/`，但 CLI 文档还展示扁平 Markdown 形态，不能假定与目录式 Skill 完全等价；优先使用项目 `.agents/skills/`。
- 官方没有承诺 Gitee URL 直装，采用 clone/copy。

### Cursor

```text
请优先从 https://gitee.com/tangenzhe/jinmoyijian 下载仓库（失败再用 GitHub 同名仓库），先审查安全政策，再把 npc-motorcycle-opinion-assistant 完整目录安装到 ~/.cursor/skills/，重新加载 Cursor 并验证它能在“禁摩意见”请求中自动启用；现在不要执行网页操作或提交。
```

也可复制到 `~/.agents/skills/npc-motorcycle-opinion-assistant/`。安装后输入 `/npc-motorcycle-opinion-assistant`，或打开 Customize → Skills 查看。

### 千问办公（QwenWork）

```text
请从 https://gitee.com/tangenzhe/jinmoyijian 下载 npc-motorcycle-opinion-assistant 子目录，先阅读免责声明与禁止滥用政策，再完整安装到 ~/.qwenworkcn/skills/npc-motorcycle-opinion-assistant/；若同名目录存在先停止询问，不要覆盖。安装后确认 SKILL.md 和三份 references 可读，并在“我的安装”或 `/` 列表中核验。本次只安装，不访问或提交任何意见。
```

官方还支持把开源仓库链接发给 QwenWork 并要求安装指定子目录。手动路径：扩展 → 技能 → 安装技能；按界面选择 `SKILL.md` 与 `references/` 等辅助文件，只有当前界面明确接受根级 `SKILL.md` ZIP 时才使用 `-upload.zip`，不要上传整个仓库 ZIP。若当前入口只能接收单个 `SKILL.md` 且无法同时提供三份 `references/`，不能宣称完整安装。

文件系统安装：复制完整目录到 `~/.qwenworkcn/skills/npc-motorcycle-opinion-assistant/`，然后重启或刷新千问办公。

### OpenCode

```text
请优先从 https://gitee.com/tangenzhe/jinmoyijian 下载仓库（失败再用 GitHub 同名仓库），审查后把 npc-motorcycle-opinion-assistant 完整目录安装到 ~/.config/opencode/skills/，重启 OpenCode 并验证 Agent 能发现和加载该 Skill；现在不要执行该 Skill 或提交意见。
```

项目级也可使用 `.opencode/skills/` 或 `.agents/skills/`。如果同名目录已存在，先比较内容，不要无提示覆盖用户修改。

### Pi Coding Agent

本仓库包含只声明 Skill 路径、没有依赖和生命周期脚本的 `package.json`，因此 Pi 可以把 Gitee 仓库作为包安装：

```text
请先审查 https://gitee.com/tangenzhe/jinmoyijian 的 README、免责声明、禁止滥用政策、package.json 和 Skill 全部文件，确认 package.json 没有安装脚本或依赖后，再执行 pi install https://gitee.com/tangenzhe/jinmoyijian.git；安装后用 pi list 和 /skill:npc-motorcycle-opinion-assistant 验证。本次只安装，不运行 Skill，不访问或提交任何意见。
```

```bash
pi install https://gitee.com/tangenzhe/jinmoyijian.git
```

项目级安装加 `-l`。也可手动复制到 `~/.pi/agent/skills/npc-motorcycle-opinion-assistant/`、`~/.agents/skills/npc-motorcycle-opinion-assistant/`，或项目 `.pi/skills/`、`.agents/skills/`。Pi 包具有较高系统权限，第三方包必须先审阅；不要关闭其安全确认。

### OpenAI Codex

在 Codex 对话中发送：

```text
$skill-installer 请安装 https://github.com/Little-Z7/jinmoyijian/tree/main/npc-motorcycle-opinion-assistant，安装后验证完整目录并告诉我如何调用；现在不要执行这个 Skill。
```

OpenAI 官方说明 `$skill-installer` 可处理其他仓库，但没有点名 Gitee。若 GitHub 访问困难，请发送本指南顶部的通用提示词，让 Codex 从 Gitee 克隆后复制到官方用户目录 `~/.agents/skills/npc-motorcycle-opinion-assistant/`。安装后新建会话，通过 `/skills` 核验，再用 `$npc-motorcycle-opinion-assistant` 显式调用或让描述自动匹配。

### Claude Code

```text
请优先从 https://gitee.com/tangenzhe/jinmoyijian 下载仓库（失败再用 GitHub 同名仓库），先阅读免责声明和禁止滥用政策；若 ~/.claude/skills/npc-motorcycle-opinion-assistant 已存在就停止询问，否则复制完整目录并确认三份 references 可读，再验证可通过 /npc-motorcycle-opinion-assistant 调用。现在只安装，不执行或提交。
```

本仓库目前没有 `.claude-plugin/marketplace.json`，因此采用原生 Skill 目录安装，不宣称可直接作为 Claude 插件市场源。

## 人工下载与安装

当辅助安装未成功时，按下面做：

1. 复制到磁盘目录时下载“解压安装包”；只有界面明确要求 ZIP 根级直接包含 `SKILL.md` 时才下载“界面上传包”，其他界面按其实际文件类型和布局要求准备。如果改为下载整个仓库 ZIP，再找到其中的 `npc-motorcycle-opinion-assistant` 文件夹；
2. 确认 `SKILL.md` 直接位于 `npc-motorcycle-opinion-assistant` 文件夹内；
3. 将**这个文件夹本身**复制到产品的用户级 Skills 目录；界面明确要求根级 `SKILL.md` ZIP 时选择本仓库生成的 `-upload.zip`，否则遵循该产品当前公开要求；
4. 重启产品或刷新 Skills；
5. 按“是否真的安装成功”的四项标准验收。

常见错误：

- 多套了一层目录，例如 `npc-motorcycle-opinion-assistant/npc-motorcycle-opinion-assistant/SKILL.md`；
- 只复制了 `SKILL.md`，遗漏 `references/`；
- 文件名变成 `skill.md`、`SKILL.md.txt`；
- 把整个仓库 ZIP 上传给只接受单个 Skill 的界面；
- 安装到了项目目录，却在另一个项目或云端 Agent 中测试；
- 没有重载或重启产品；
- 产品只读取本机用户目录，但任务实际运行在远程/云端机器。

## 自动触发与手动触发

本 Skill 的 `description` 已包含以下触发语义：

- 禁摩意见；
- 道路交通安全法征求意见；
- 全国人大意见填写。

原生支持自动匹配的平台通常会在相关请求中按需加载。自动触发失败时，可以直接说：

```text
请使用 npc-motorcycle-opinion-assistant Skill，先检查当前会话是否具备浏览器或 Computer Use 能力，再核对官方页面和我的意见正文；缺少能力时引导我开启或切换为人工协作，任何提交动作前都必须再次让我确认。
```

手动调用名称因产品而异：Codex 常用 `$名称`，Claude/Cursor/Qoder 常用 `/名称`，Kimi Code 常用 `/skill:名称`，Kimi Work/千问办公通常可在输入框键入 `/` 后选择。无论哪种方式，都不得把调用 Skill 理解为一次最终提交授权。

## 官方资料

以下链接用于核对各产品公开的 Skills 能力和目录；产品更新后请优先查看其最新版本：

- [OpenAI Codex：Build skills](https://learn.chatgpt.com/docs/build-skills)
- [WorkBuddy：Skill Marketplace](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)
- [TraeCode：Skills](https://docs.trae.cn/ide_skills)
- [TraeWork：Skills](https://docs.trae.cn/work_skills)
- [Qoder IDE：Skills](https://docs.qoder.com/qoder/skills)
- [Qoder CLI：Skills](https://docs.qoder.com/cli/Skills)
- [QoderWork：Skills](https://docs.qoder.com/qoderwork/skills)
- [豆包普通聊天：功能介绍](https://www.doubao.com/legal/feature_intro)
- [Kimi：什么是 Skills](https://www.kimi.ai/zh-hans/help/features/what-are-skills)
- [Kimi Work 产品介绍](https://www.kimi.ai/zh-hans/help/kimi-work/overview)
- [Kimi Code：Agent Skills](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html)
- [Kimi Code：Plugins](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/plugins)
- [MiniMax：Agent Plugins](https://agent.minimaxi.com/docs/code/agents/plugins)
- [Gemini CLI：Using Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/)
- [Google Antigravity：Agent Skills](https://antigravity.google/docs/skills)
- [Cursor：Agent Skills](https://cursor.com/docs/skills)
- [千问办公：技能](https://help.aliyun.com/zh/qwenwork/skills)
- [OpenCode：Agent Skills](https://opencode.ai/docs/skills)
- [Pi Coding Agent：Skills](https://pi.dev/docs/latest/skills)
- [Pi Coding Agent：Packages](https://pi.dev/docs/latest/packages)
- [Claude Code：Extend Claude with skills](https://code.claude.com/docs/en/slash-commands)

## 维护者：生成安装包

修改 Skill 或政策文件后，在仓库根目录运行：

```bash
python3 scripts/package_skill.py
```

提交前同时检查两种布局：普通包应以同名目录为根，上传包应直接以 `SKILL.md` 为根级文件。再核验摘要：

```bash
unzip -l dist/npc-motorcycle-opinion-assistant.zip
unzip -l dist/npc-motorcycle-opinion-assistant-upload.zip
cd dist && shasum -a 256 -c SHA256SUMS
```

脚本使用固定时间戳生成两个可重复构建的 ZIP，并同时更新 `dist/SHA256SUMS`。`package.json` 仅为 Pi 声明 Skill 路径，不包含依赖或生命周期脚本。
