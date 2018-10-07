# grumpy

## Setup

### install python requirements

`sudo pip install -r requirements.txt`

### Create a pre-commit hook and configure git

- create a hooks directory

`mkdir -p ~/.git-template/hooks`

- create a pre-commit file in that directory

`touch ~/.git-template/hooks/pre-commit`

- put the code below in the pre-commit file

Point to take-picture.py in this repository

```bash
#!/bin/bash
python ~/grumpy/take-picture.py
```

- make the file executable

`chmod o+x ~/.git-templates/hooks/pre-commit`

- “activate” your init dir

`git config --global init.templatedir ‘~/.git_template’`

## TODO

- Configuration variables in separate file (PICTURES_DIRECTORY, BUCKET_NAME etc...)
