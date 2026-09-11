# AGENTS.md

Personal learning repository (not a software project). Goal: understand deep learning from the math up — linear algebra → neural nets → Transformer → LLM — for an electrical engineering × AI research direction. There is no build system, test suite, linter, or CI. Value here is notes and experiment code, not production quality.

## Repository layout

- `notes/` — dated learning notes in Chinese (`day1.md`, …), one file per study day
- `weekNN/` — weekly experiment code, one directory per week (`week01/`), primarily Jupyter notebooks
- `scratch/` — drafts and throwaway experiments (may be empty; git does not track empty dirs, so it may not exist after a fresh clone)
- `README.md` — progress checklist and structure map; update the 进度 (progress) section when completing a milestone
- `output.png` / other small generated images — acceptable to commit at repo root or near the code that produced them

## Environment

- Python virtualenv at `.venv/` (Python 3.10.12) containing only numpy, matplotlib, and the Jupyter/ipykernel stack. Run code with `.venv/bin/python` or `.venv/bin/jupyter`, or activate it first.
- No PyTorch (yet). If a future week needs it, install into `.venv`.
- Repo lives on a Windows drive mounted in WSL (`/mnt/d/study-space/Ai`). File I/O through `/mnt/d` is noticeably slower than native Linux paths.
- Notebooks are executed from VS Code using the `.venv (3.10.12)` kernel. Saved notebook outputs (plots, printed results) are intentional — they document experiments, so don't strip them when editing notebooks.

## Git conventions (owner's explicit workflow, from notes/day1.md)

- **Language**: all notes, README, and commit message descriptions are written in Chinese. Commit subjects use the prefix pattern `dayN: <做了什么>` or `weekN: <做了什么>` (e.g. `day1: environment setup`, `week1: 手写两层MLP反向传播`). Never use vague messages like `update`.
- **Single branch**: always work on `main`. The owner has deliberately decided not to use branches in this solo learning repo.
- **Commit ≠ push**: commits are local snapshots; only `git push` syncs to GitHub. The owner expects regular commits and pushes (backup is the point of the remote).
- **Remote/credentials gotcha**: remote `origin` is `https://github.com/wayxi111/Ai.git` and credentials are stored in the `gh` CLI under the `wayxi111` account. A past failure was caused by `origin` pointing at a nonexistent repo under a different account (`wayci-bot`). If push fails, first check `git remote -v` and `gh auth status` before touching anything else.

## What belongs in the repo (owner's stated rules)

- Commit: source code (`.py`, `.ipynb`), notes (`.md`), README, small result images.
- Never commit: datasets (`data/` is gitignored — MNIST etc. must be downloaded by each machine), `.venv/`, `__pycache__/`, `.ipynb_checkpoints/`, and bulk generated artifacts.
- GitHub repo is not a file dump: everything committed should be readable as evidence of learning progress.

## Working style for agents

- When adding study notes, match the existing style in `notes/day1.md`: Chinese prose, markdown headings, occasional ASCII diagrams and tables.
- When adding weekly code, create/extend the matching `weekNN/` directory rather than putting notebooks at the repo root.
- Prefer numpy/matplotlib implementations from scratch over deep-learning frameworks unless the week's topic explicitly calls for a framework — the stated goal is mathematical understanding.
- When adding a bridge to `notes/bridges.md`, label both its relationship type and evidence state. Keep teaching analogies, mathematical identities, experimental observations, literature-backed claims, and unverified research hypotheses distinct.
- At the end of each completed module, add at most one electrical-engineering-related research question to the research-seed table in `notes/bridges.md`. A seed is not a conclusion; record the next evidence needed.

## Teaching contract (owner-confirmed, applies to every session)

- **任务单模式**：出任务时只给 任务 + 验收标准 + 坑预警，代码由 owner 自己写。代劳写学习代码是被拒绝的（"改好检查"是理解过程）。owner 卡壳求助时先给提示链，不直接给答案。
- **先猜后跑**：每个实验先让 owner 猜结果/量级再运行。对 owner 的"口头回答"类问题，等 2 分钟冷静期，不急着代劳。
- **验收惯例**：用"残差 vs 允差"（1/√N 家族传播公式），不用"数值接近"；全绿才算通过。
- **黄金验收区**：探索 cell 和踩坑输出可以保留，但每个阶段性 notebook 的末尾要有一段可独立重跑的验收区：固定 seed/参数 → 从头构造数据 → 打印理论、实测、残差、允差、PASS/FAIL。里程碑提交前执行 Restart Kernel + Run All，保存输出；未全量重跑不得宣称 notebook 可复现。
- **1–7–30 回看**：只从卡点金矿生成复习负载。次日闭卷复述机制，7 天后做变式/反例，30 天后说明它与新知识的连接；每个主题最多 3 个口头问题 + 1 个小实验，不给所有笔记机械制卡。
- **较真文化**：输出与预期不符必须停下来查根因；提示词与数据冲突时信数据不信人（包括导师）——owner 已两次用数据推翻导师提示并记档。
- **卡点记档**：踩坑记进当日 notes/dayN.md 的"卡点金矿"段（症状/根因/防御三件套），这是仓库最有价值的资产。
- **语言**：与 owner 的一切交流用中文；笔记、README、commit 同理。

## Session continuity (how a fresh session picks up the thread)

1. **开工**：读 README「进度」区（状态锚点，现在时）→ `git log --oneline -5` → 若涉及早前决策，跑 project-memory 的 `context` 命令（store: `D:\codex-knowledge`, project-id `ai-kaoyan`）。检索只按需 `search`，不整库加载；不再使用 WSL 内的 Crush 记忆库。
2. **收工分层**：每个学习日完成时立即收工（**不等到 session 终止**——本仓库 session 曾因上下文过长被截断，届时已无力存档），但不机械重复所有归档动作：
   1. **每日必做**：完成 dayN/mathNN 的卡点与三句话总结；把 README 状态锚点的“当前/下一步/欠账/决策”更新到真实状态；提交并 push 当日学习证据。
   2. **有新桥才做**：扫当日知识主线/卡点金矿，只把新的、有复用价值的桥写入 `notes/bridges.md`，同时标注关系类型和证据状态；没有新桥就不凑数。
   3. **有持久变化才做**：仅当战略、接口、约束、方法论或里程碑发生稳定变化时写 project-memory checkpoint；普通学习日不重复 dayN 内容。
   4. **里程碑额外做**：notebook 通过黄金验收区并 Restart Kernel + Run All；未闭环实验留在 README“欠账”，不提前打勾。
3. **信源优先级**：仓库文件（notes/README/AGENTS.md）> 记忆库 > 会话记忆。会话摘要可能串线（曾把"hello.ipynb 已跑 MNIST 95%"记成事实，实际仓库里根本没有），以文件为准。
4. **记忆库是单机资产**：Windows 侧 `D:\codex-knowledge` 不随 git 同步，是本项目唯一在用的 project-memory store；WSL 内旧库仅作为迁移来源，不再继续写入。换机器时优先复制该目录；若不可用，则凭仓库文件重建（注册 + 按 README/bridges/dayN 重写 overview 与主题 checkpoint 即可，本 memory 的知识 90% 源自 repo 内文件）。store 内全部是纯 markdown，没有 project-memory skill 时也可直接读取。
