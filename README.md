# grumpy

A git hook that takes a webcam snapshot at each commit.

## setup

- install python requirements

`sudo pip install -r requirements.txt`

- create a `config.ini` file and adapt the following content

```ini
[folders]
pictures_directory=/home/you/.gitshots
```

- create a pre-commit hook and configure git

`mkdir -p ~/.git-template/hooks`
`touch ~/.git-template/hooks/pre-commit`

- put the code below in the pre-commit file (adapt the path to `take-picture.py` if necessary)

```bash
#!/bin/bash
python ~/grumpy/take-picture.py
```

- make the file executable

`chmod o+x ~/.git-template/hooks/pre-commit`

- "activate" your init dir

`git config --global init.templatedir "~/.git-template"`

- adapt your PICTURES_DIRECTORY: in `take-picture.py`, set PICTURES_DIRECTORY to the local folder of your choice
- **Run `git init` in your existing git repos**. The hook will kick in automatically in your new repos while they are being configured. For the existing ones, running `git init` will update the configuration.

## uploads to AWS S3

By default, `take-picture.py` will store shots on your local filesystem. You can use `s3.py` to upload your shots in an s3 bucket and remove the local version.

## make it a timelapse

`ffmpeg -r 24 -pattern_type glob -i '*.jpg' -s hd1080 -vcodec libx264 timelapse.mp4`
