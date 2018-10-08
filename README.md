# grumpy

## Setup

### install python requirements

`sudo pip install -r requirements.txt`

### Create a pre-commit hook and configure git

`mkdir -p ~/.git-template/hooks`

`touch ~/.git-template/hooks/pre-commit`

- put the code below in the pre-commit file

```bash
#!/bin/bash
python ~/grumpy/take-picture.py
```

adapt the path to `take-picture.py` if necessary

- make the file executable

`chmod o+x ~/.git-template/hooks/pre-commit`

- "activate" your init dir

`git config --global init.templatedir "~/.git_template"`

- adapt your PICTURES_DIRECTORY: in `take-picture.py`, set PICTURES_DIRECTORY to the local folder of your choice
- the git hook will kick in automatically in your new repos. For the existing ones, running `git init` will update the configuration.

## uploads to s3

By default, `take-picture.py` will store shots on your local filesystem. You can use `s3.py` to upload your shots in an s3 bucket and remove the local version.
