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
