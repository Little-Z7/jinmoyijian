# 禁摩意见提交 Skill

这是一个正在设计中的 Codex skill 仓库，目标是协助用户在全国人大法律草案征求意见系统中填写并提交与摩托车通行政策相关的意见。

> [!WARNING]
> 本项目涉及政府网站意见征集，但不是官方工具，也未获得全国人民代表大会、全国人大常委会或网站运营方的授权、认可或背书。严禁使用本项目批量灌入、重复提交、冒名提交、操纵参与数据，或绕过验证码、访问控制、频率限制和反自动化措施。每次提交都必须由实际意见人知情、逐次授权并在最终提交前确认。

使用或贡献本项目之前，必须阅读：

- [免责声明](DISCLAIMER.md)
- [禁止滥用与可接受使用政策](ACCEPTABLE_USE.md)

当前状态：Skill 已实现，正在等待真实人工流程的只读/预填验证；仓库不会自动进行任何意见提交。

## 功能

- 在中国人大网当前征求意见列表中按完整标题定位《道路交通安全法（修订草案）》；
- 在用户本人完成个人信息、登录或验证码后，按其选择预填四条摩托车政策意见；
- 支持合并为一条总体意见，或按第十九、四十八、七十一、八十二条逐条处理；
- 在每次最终提交前展示完整正文并取得本次确认；
- 提交结果不明确时停止，不自动重试。

Skill 位于 [`npc-motorcycle-opinion-assistant/`](npc-motorcycle-opinion-assistant/)。

## 安装

使用 Codex 的 Skill 安装器从本仓库安装：

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo Little-Z7/jinmoyijian \
  --path npc-motorcycle-opinion-assistant
```

安装后开启一个新会话，并通过以下方式调用：

```text
$npc-motorcycle-opinion-assistant 请帮我在全国人大意见征集页面预填并核对禁摩相关意见，提交前先让我确认。
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
- 若官方表单仍使用明文 HTTP，助手不得代点发送个人信息或最终提交，只能预填非敏感正文并交由用户本人决定；
- 四条意见若分别提交，需要四次独立确认，不能用一次授权覆盖。

## 仓库结构

```text
npc-motorcycle-opinion-assistant/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── opinion-draft.md
    └── site-workflow.md
```

## 验证

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" \
  npc-motorcycle-opinion-assistant
git diff --check
```

## 许可证

尚未选择开源许可证。在公开发布前需要确定许可证并添加 `LICENSE` 文件。

禁止滥用政策是项目的安全边界与维护者支持政策，不应被误写进或冒充标准开源许可证条款。如需让用途限制具有许可证层面的法律约束力，应先取得专业法律意见，并重新评估项目能否继续称为开源软件。
