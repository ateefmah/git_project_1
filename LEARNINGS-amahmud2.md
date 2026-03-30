# Learnings — amahmud2

## Checkpoint 1: Staging Is Not Committing

**Commands used:**
```
git add tests/test_calculator.py
git commit -m "fix"
git add src/calculator.py
git commit -m "update"
git push origin feature/amahmud2
```

**Reflection:** The staging area lets you craft commits with surgical precision — even when multiple files are modified, you can choose exactly which changes belong together. This keeps each commit focused on a single logical change, making history easier to read and bugs easier to trace.

---

## Checkpoint 2: Undo Without Erasing History

**Commands used:**
```
git log --oneline
git revert 66f6716 --no-edit
```

**Reflection:** `git revert` creates a new commit that inverts a previous change without touching the existing history, which is crucial on shared branches. This preserves the audit trail while safely removing harmful code from the working state.

---

## Checkpoint 3: Moving a Commit to the Right Branch

**Commands used:**
```
git checkout main
# (edited src/validator.py to add is_positive)
git add src/validator.py
git commit -m "Add is_positive helper function"
git reset --hard HEAD~1
git checkout feature/amahmud2
git cherry-pick 705ce1d5fe9168434c73d0128bd7521e89e0d744
# (resolved merge conflict — kept both validate_range and is_positive)
git add src/validator.py
git cherry-pick --continue --no-edit
```

**Reflection:** `git cherry-pick` lets you transplant any commit onto a different branch by its hash, making it easy to rescue work committed to the wrong place. Merge conflicts during cherry-pick require manually keeping both versions when the branches have diverged.

---

## Checkpoint 4: Recovering Lost Work with Reflog

**Commands used:**
```
git checkout -b experiment/amahmud2
# (added a comment to src/calculator.py)
git add src/calculator.py
git commit -m "Experimental: note future trigonometric extension"
git checkout feature/amahmud2
git branch -D experiment/amahmud2
git reflog
git branch recovered/amahmud2 f3019f4
git merge recovered/amahmud2 --no-edit
```

**Reflection:** `git reflog` records every HEAD movement, so commits are never truly lost until garbage collection runs. This is a safety net for accidental branch deletions or hard resets — as long as you know the hash, you can resurrect any commit.

---

## Checkpoint 5: Syncing with Upstream

**Commands used:**
```
git remote -v
git fetch upstream
git checkout main
git merge --ff-only upstream/main
git checkout feature/amahmud2
git rebase main
git push --force-with-lease origin feature/amahmud2
```

**Reflection:** Keeping a fork in sync with upstream requires maintaining two remotes (`origin` for your fork, `upstream` for the original) and rebasing your feature work on top of the latest changes. `--force-with-lease` is safer than `--force` because it refuses to push if someone else has updated the remote branch since your last fetch.

---

## Checkpoint 6: Interactive Rebase to Clean Up History

**Commands used:**
```
git log main..HEAD --oneline
git rebase -i HEAD~8
# (rewrote "fix" → "Fix missing modulo import in test_calculator.py")
# (rewrote "update" → "Add descriptive module-level docstring to calculator")
git push --force-with-lease origin feature/amahmud2
```

**Reflection:** Interactive rebase (`reword`, `squash`, reordering) lets you reshape your commit history before sharing it, turning a messy trail of save-points into a clean narrative that reviewers can follow. A good commit message explains *why* a change was made, not just what changed.
