# Publishing this repository

This archive is a ready-to-publish initial version of **Awesome Inference Specialization**.

## With the GitHub CLI

Sign in using `gh auth login` if needed, then run from the extracted project directory:

```bash
git init
git add .
git commit -m "Initial curated inference specialization catalog"
git branch -M main
gh repo create awesome-inference-specialization --public --source=. --remote=origin --push
```

The command creates a new public repository in the GitHub account selected by `gh`; verify the owner beforehand with `gh auth status`. If the target repository already exists, do not run `gh repo create` again; add the correct remote and push instead.

## Without the GitHub CLI

Create an **empty public repository** named `awesome-inference-specialization` using https://github.com/new. Do not initialize the repository with a README, license, or .gitignore (this archive already includes those files).

Then, from the extracted project directory:

```bash
git init
git add .
git commit -m "Initial curated inference specialization catalog"
git branch -M main
git remote add origin https://github.com/OWNER/awesome-inference-specialization.git
git push -u origin main
```

Replace `OWNER` with the intended GitHub username or organization, and authenticate with an approved GitHub credential method. This archive contains **no access tokens or private keys**.

## Verify

```bash
python scripts/validate_catalog.py
python scripts/update_readme.py --check
```

After publication, consider enabling GitHub Discussions and adding repository topics: `awesome-list`, `inference`, `llm-inference`, `model-specialization`, `ai-systems`, `video-generation`, `diffusion`.
