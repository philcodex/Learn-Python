# Git Commands — Quick Reference

A summary of the most useful Git commands for daily use.

---

## Setup
```bash
git config --global user.name "philcodex"
git config --global user.email "your@github-email.com"

git config user.name        # check current name
git config user.email       # check current email
```

---

## Starting a repo
```bash
git init                    # initialise a new local repo
git clone <url>             # clone a remote repo locally
```

---

## Staging & committing
```bash
git status                  # show changed files
git add .                   # stage all changes
git add <file>              # stage a specific file
git add <folder>/           # stage a specific folder

git commit -m "message"     # commit with a message
git commit --amend          # edit the last commit message
```

---

## Pushing & pulling
```bash
git push                            # push to remote
git push -u origin main             # push and set upstream
git push origin main --force        # force push (use with caution)

git pull                            # fetch and merge remote changes
git pull origin main                # pull from specific branch
git pull origin main --allow-unrelated-histories
```

---

## Branches
```bash
git branch                  # list local branches
git branch <name>           # create a new branch
git checkout <name>         # switch to a branch
git checkout -b <name>      # create and switch to a new branch
git branch -m <old> <new>   # rename a branch
git branch -d <name>        # delete a branch
```

---

## Remote
```bash
git remote -v                           # show remote URLs
git remote add origin <url>            # add a remote
git remote set-url origin <url>        # update remote URL
git remote remove origin               # remove remote
```

---

## Undoing changes
```bash
git restore <file>              # discard changes in working directory
git restore --staged <file>     # unstage a file

git revert <commit>             # undo a commit by creating a new one
git reset --soft HEAD~1         # undo last commit, keep changes staged
git reset --hard HEAD~1         # undo last commit, discard all changes

git rebase --abort              # cancel an in-progress rebase
git rebase --continue           # continue after resolving rebase conflict
```

---

## Viewing history
```bash
git log                         # full commit history
git log --oneline               # compact commit history
git log --oneline --graph       # visual branch history
git diff                        # show unstaged changes
git diff --staged               # show staged changes
```

---

## Removing files
```bash
git rm <file>                   # remove file from repo and local
git rm --cached <file>          # remove from repo only, keep locally
git rm -r --cached <folder>/    # remove folder from repo only
```

---

## Stashing
```bash
git stash                       # save uncommitted changes temporarily
git stash pop                   # restore stashed changes
git stash list                  # list all stashes
git stash drop                  # delete the latest stash
```

---

## Common workflows

**Start a new project:**
```bash
git init
git add .
git commit -m "initial commit"
git remote add origin <url>
git push -u origin main
```

**Daily update:**
```bash
git add .
git commit -m "update notes"
git push
```

**Fix wrong remote URL:**
```bash
git remote set-url origin https://github.com/philcodex/<repo>.git
```

**Remove a file from repo but keep locally:**
```bash
git rm --cached <file>
git commit -m "remove file from tracking"
git push
```

---

## Glossary

| Term | Meaning |
|------|---------|
| `origin` | Default name for the remote repo |
| `main` | Default primary branch name |
| `HEAD` | Pointer to the current commit |
| `staged` | Changes added but not yet committed |
| `upstream` | The remote branch your local branch tracks |
| `detached HEAD` | Not on a branch — checked out a specific commit |