
# Requirements

- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org)

# Setup

If you haven't already, clone the repository.

Install development dependencies using:
```sh
poetry install --no-root
# Enter virtual environment
poetry shell
```

# Checks

Before submitting commits or pull requests, consider running the following
checks:
```sh
# Enter virtual environment if you haven't already
poetry shell
# Linting
flake8 .
# Type-check
mypy .
# Run unit tests
python -m pytest
```

# Writing Messages

We follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/#summary)
for commit messages and pull requests:
```
<type>[optional scope]: <description>
```

We use the following types:

* **ci**: Changes to CI configuration
* **docs**: Documentation only changes
* **feat**: A new feature
* **fix**: A bug fix
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* **test**: Adding missing tests or correcting existing tests


<!-- vim: set conceallevel=2 et ts=2 sw=2: -->
