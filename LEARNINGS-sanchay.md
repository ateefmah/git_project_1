Checkpoint 1:

git add src/calculator.py
git commit -m "fix"
git add src/validator.py
git commit -m "update"
git push origin feature/sanchay

At this checkpoint I learned about adding files to the staging area and performing a commit and push to push changes.

-

Checkpoint 2:

git log --oneline
git revert 4dc20fb
git status
git add src/calculator.py
git commit -m "Removed excessive debug logging clogging output from calculator module"
git push origin feature/sanchay

At this checkpoint I learned about resolving a merge conflict that resulted from trying to revert. I also learned about using revert and specifying the hash of the commit I wanted to use revert with.

-

Checkpoint 3:

git switch main
git add src/validator.py
git commit -m "Add is_positive helper function"
git reset --hard HEAD~1
git switch feature/sanchay
git cherry-pick 80b0010
git add src/validator.py
git cherry-pick --continue
git push origin feature/sanchay

At this checkpoint I learned how to edit commit using Vim, since this editor opened to let me edit commit message for my cherry-picked commit.

-

Checkpoint 4:

git switch -c experiment/sanchay
git add src/calculator.py
git commit -m "Added comment to calculator.py"
git switch feature/sanchay
git branch -D experiment/sanchay
git reflog
git switch -c recovered/sanchay 4a0083e
git switch feature/sanchay
git merge recovered/sanchay
git push origin feature/sanchay

At this checkpoint I learned how to use git reflog to find the hash of a commit, before then using this hash to create a branch.

-

Checkpoint 5:

git remote add upstream git@github.com:mdurrani808/git_project_1.git
git fetch upstream
git checkout main
git reset --hard upstream/main
git checkout feature/sanchay
git rebase main
git push --force-with-lease origin feature/sanchay

At this checkpoint I learned to use rebase to incorporate main changes into my branch. There were no merge conflicts I had to handle.

-

Checkpoint 6:

git log main..HEAD --oneline
git rebase -i main
git push --force-with-lease
git push origin feature/sanchay

At this checkpoint I learned to perform an interactive rebase using Vim to specify what I wanted to happen to each commit - I reworded 2 of the initial commit messages I created at the start of the project, and I squashed 2 others together.