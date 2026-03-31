# Learnings - kbryan27

## Checkpoint 1
### Commands
git add tests/test_calculator.py
git commit -m "fix"
git add src/validator.py
git commit -m "update"
git push origin feature/kbryan27

### Learned
The staging area lets you control which changes go into a commit.
It is good to commit bite sized chunks at a time to keep code functional for everyone

## Checkpoint 2
### Commands
git log --oneline
git revert b19f233

### Learned
'git revert' undoes a commit by creating a new one.
safer than deleting commits because it leaves a log.

## Checkpoint 3
### Commands
git checkout main
git add src/validator.py
git commit -m "Add is_positive helper function"
git log --oneline
git reset --hard HEAD~1
git checkout feature/kbryan27
git cherry-pick 612ff43

### Learned
cherry-pick moves a commit from one branch to another.
helps if you accidentaly commit in the wrong branch

## Checkpoint 4
### Commands
git checkout -b experiment/kbryan27
git add .
git commit -m "Experiment commit"
git checkout feature/kbryan27
git branch -D experiment/kbryan27
git reflog
git checkout -b recovered/kbryan27 099bb74
git merge recovered/kbryan27

### Learned
'git reflog' tracks all Git takes, even deleted stuff.
keeps accidental deletions minor in damage

## Checkpoint 5
### Commands
git remote add upstream git@github.com:mdurrani808/git_project_1    
git fetch upstream
git checkout main
git merge upstream/main
git checkout feature/kbryan27
git rebase main
git push --force-with-lease origin feature/kbryan27

### Learned
able to sync a forked repo with the original upstream repository (real main)
Rebase keeps the history normal? (doesnt mess up commit history)

## Checkpoint 6
### Commands
git log main..HEAD --oneline
git rebase -i main
git push --force-with-lease origin feature/kbryan27

### Learned
editing rebase lets you rewrite, rename, and merge commits.
moving around and editing in vim, including insert and escape mode.