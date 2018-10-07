# grumpy

## Setup

### Create a hooks directory

`mkdir -p ~/.git-template/hooks`

### Create a pre-commit file in that directory and feed it the commit-hook

`touch ~/.git-template/hooks/pre-commit`

### Put that in the pre-commit file

Point to take-picture.py in this repository

```bash
#!/bin/bash
python ~/grumpy/take-picture.py
```

### Make the file executable

```bash
chmod o+x ~/.git-templates/hooks/pre-commit
```

### “activate” your init dir

git config --global init.templatedir ‘~/.git_template’
