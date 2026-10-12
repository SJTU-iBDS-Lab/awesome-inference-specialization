# Publishing this repository

This archive is a ready-to-publish initial version of **Awesome Inference Specialization**.

## With the GitHub CLI

Sign in using `gh auth login` if needed, then run from the extracted project directory:

```bash
git init
git add .
git commit -m "Initial curated inference specialization catalog"
git branch -M main
gh repo create SJTU-iBDS-Lab/awesome-inference-specialization --private --source=. --remote=origin --push
```

The command creates a new private repository in the `SJTU-iBDS-Lab` organization. Check the signed-in account with `gh auth status` and ensure it has permission to create repositories in that organization. If the target repository already exists, do not run `gh repo create` again; use the correct remote and push instead.

## Without the GitHub CLI

Create an **empty private repository** named `awesome-inference-specialization` under `SJTU-iBDS-Lab` using https://github.com/organizations/SJTU-iBDS-Lab/repositories/new. Confirm that the owner is `SJTU-iBDS-Lab` and visibility is **Private**. Do not initialize the repository with a README, license, or .gitignore (this archive already includes those files).

Then, from the extracted project directory:

```bash
git init
git add .
git commit -m "Initial curated inference specialization catalog"
git branch -M main
git remote add origin https://github.com/SJTU-iBDS-Lab/awesome-inference-specialization.git
git push -u origin main
```

Authenticate with an approved GitHub credential method. This archive contains **no access tokens or private keys**.

## Verify

```bash
python scripts/validate_catalog.py
python scripts/update_readme.py --check
```

After publication, consider enabling GitHub Discussions and adding repository topics: `awesome-list`, `inference`, `llm-inference`, `model-specialization`, `ai-systems`, `video-generation`, `diffusion`.
