# Learn CDK for Terraform

```console
$ cdktf init --template=python --local

# add pagerduty provider
$ cdktf provider add "PagerDuty/pagerduty"

# or, pipenv run main.py
# generates the same cdktf.out directory
$ cdktf synth

# TODO: explore/try this
$ cdktf deploy
```

## Local dev

```console

# install deps
$ pipenv install

# lint
$ pipenv run isort .
$ pipenv run black .
```
