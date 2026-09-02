# 禁摩意见提交 Skill

这是一个面向多种 Agent Skills 兼容工具的公开源码仓库，目标是协助用户在全国人大法律草案征求意见系统中填写并提交与摩托车通行政策相关的意见。

> [!WARNING]
> 本项目涉及政府网站意见征集，但不是官方工具，也未获得全国人民代表大会、全国人大常委会或网站运营方的授权、认可或背书。严禁使用本项目批量灌入、重复提交、冒名提交、操纵参与数据，或绕过验证码、访问控制、频率限制和反自动化措施。每次提交都必须由实际意见人知情、逐次授权并在最终提交前确认。

使用或贡献本项目之前，必须阅读：

- [免责声明](DISCLAIMER.md)
- [禁止滥用与可接受使用政策](ACCEPTABLE_USE.md)

当前状态：Skill 已实现。仓库不会自动进行任何意见提交；提交结果不明确时立即停止且不自动重试。

## 功能

- 在中国人大网当前征求意见列表中按完整标题定位《道路交通安全法（修订草案）》；
- 运行前检查当前会话是否具备已登录浏览器控制、Browser Use、Playwright 或 Computer Use 能力，缺失时引导开启或切换为人工协作；
- 在用户本人完成个人信息、登录或验证码后，按其选择预填四条摩托车政策意见；
- 支持合并为一条总体意见，或按第十九、四十八、七十一、八十二条逐条处理；
- 在每次最终提交前展示完整正文并取得本次确认；
- 提交结果不明确时停止，不自动重试。

Skill 位于 [`npc-motorcycle-opinion-assistant/`](npc-motorcycle-opinion-assistant/)。

## 安装

指南覆盖 OpenAI Codex、Claude Code、Cursor、Gemini CLI、OpenCode、Pi Coding Agent、Kimi、Kimi Work、Kimi Code、MiniMax Agent、MiniMax Code、Google Antigravity、WorkBuddy、千问办公、豆包、豆包工作、TraeCode、TraeWork、Qoder、Qoder CLI、QoderWork 等工具。不同产品的原生支持程度、安装入口和浏览器能力并不相同，详见 [多平台安装指南](INSTALL.md)。

国内用户可优先使用 Gitee 镜像：<https://gitee.com/tangenzhe/jinmoyijian>；GitHub 地址为：<https://github.com/Little-Z7/jinmoyijian>。

### 一句话带你提建议就行

把下面整句话发给具备联网、本地文件和 Skills 能力的 AI 工具，它会协助完成安装与验证；不具备这些能力的产品会如实说明：

```text
仅安装并验证公开源码 Skill「npc-motorcycle-opinion-assistant」，不要调用或执行它。先查阅仓库 INSTALL.md，确认目标产品是“复制 Skill 目录”还是“界面上传”：复制目录时选择 dist/npc-motorcycle-opinion-assistant.zip；只有界面明确要求 ZIP 根级直接包含 SKILL.md 时才选择 dist/npc-motorcycle-opinion-assistant-upload.zip；其他上传格式按当前产品公开要求处理，不要猜。优先从 https://gitee.com/tangenzhe/jinmoyijian 获取，访问失败再用 https://github.com/Little-Z7/jinmoyijian；从同一镜像、同一次下载取得所选 ZIP 与 dist/SHA256SUMS，校验所选 ZIP 后再解压或上传。阅读 README.md，以及已校验包内的 LICENSE、DISCLAIMER.md、ACCEPTABLE_USE.md、SKILL.md 和 references/；包裹版文件位于 npc-motorcycle-opinion-assistant/ 下，上传版位于 ZIP 根。只安装完整 Skill；不要运行仓库脚本。若同名 Skill 已存在，停止并让我决定，不要覆盖。重新加载后验证 SKILL.md、references/environment-check.md、references/opinion-draft.md 和 references/site-workflow.md 均可读取，并报告下载源、所选包、校验结果、目标位置及发现结果。若当前产品不支持第三方 SKILL.md，请如实说明，不要假装安装成功。安装不授权访问政府网站、处理个人信息或验证码，也不授权提交任何意见。
```

安装授权不等于意见提交授权。详细指南还提供了每个产品可单独复制的一句话、手动目录、验证方式和兼容性说明。

### Codex 快速安装

在 Codex 中发送：

```text
$skill-installer 请安装 https://github.com/Little-Z7/jinmoyijian/tree/main/npc-motorcycle-opinion-assistant，安装后验证完整目录并告诉我如何调用；现在不要执行这个 Skill。
```

安装后开启一个新会话，并通过以下方式调用：

```text
$npc-motorcycle-opinion-assistant 请先检查当前会话的浏览器或 Computer Use 能力，再帮我在全国人大意见征集页面预填并核对禁摩相关意见；缺少能力时引导我开启或切换为人工协作，提交前先让我确认。
```

## 设计边界

- 仅代表当前用户处理其明确授权的意见，不用于批量、重复或冒名提交。
- 提交前展示最终内容并取得用户确认。
- 不绕过验证码、访问控制或网站的反自动化机制；遇到此类步骤时交由用户完成。
- 不编造姓名、联系方式等身份信息，也不把本地凭据、浏览器会话或个人资料提交到仓库。
- 提交后核验页面反馈，尽量避免因重试造成重复提交。

## 人工接管点

- 姓名、联系方式等个人信息只能由用户直接在官方页面填写；
- 登录、短信验证和图片验证码只能由用户本人完成；
- 发送个人信息前，以及每一次最终提交前，都必须取得紧邻动作的确认；
- 若官方表单仍使用明文 HTTP，助手只能只读导航并离线展示正文，不得在网页字段中输入内容，也不得代点发送个人信息或最终提交；
- 四条意见若分别提交，需要四次独立确认，不能用一次授权覆盖。

## 仓库结构

```text
npc-motorcycle-opinion-assistant/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── environment-check.md
    ├── opinion-draft.md
    └── site-workflow.md

dist/
├── npc-motorcycle-opinion-assistant.zip
├── npc-motorcycle-opinion-assistant-upload.zip
└── SHA256SUMS

package.json  # Pi Coding Agent 包清单
```

两个发布 ZIP 还会把仓库根目录的 `LICENSE`、`DISCLAIMER.md` 和 `ACCEPTABLE_USE.md` 放进 Skill 目录；它们是发布包附加的许可证与安全文件，源码 Skill 目录本身仍保持上图结构。

仓库根目录的 [`INSTALL.md`](INSTALL.md) 提供跨平台安装矩阵、一句话提示词和故障排查。

## 验证

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" \
  npc-motorcycle-opinion-assistant
git diff --check
```

## 许可证

本项目采用 [Apache License 2.0](LICENSE) 开源许可证，允许使用、修改和再分发，并包含明确的专利许可条款。

禁止滥用政策是项目的安全边界与维护者支持政策，不修改 Apache-2.0 的授权范围，也不冒充许可证条款。任何使用者仍须遵守适用法律、网站规则并自行承担提交行为责任。
