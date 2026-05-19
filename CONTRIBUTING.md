# Contributing

## Setup

Get the project with:

```bash
git clone git@github.com:epfl-si/django-epfl-web2018.git
cd django-epfl-web2018
```

Assuming you have `pyenv` and `pyenv-virtualenv` installed:

```bash
make setup
```

## Lint

```bash
make lint
```

## Test

```bash
tox
# or
make test
```

## Build

If you want to inspect the built artifacts locally:

```bash
pdm build
```

## Release

1. Bump the correct version
1. Update the file [CHANGELOG.md](CHANGELOG.md)
1. Create and push the tag  
    `git tag -a v<version> -m "django-epfl-web2018 v<version> release"`  
    `git push origin main --tags`

After the push, the project will be automatically published to PyPI.
