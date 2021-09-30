
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


<!-- vim: set conceallevel=2 et ts=2 sw=2: -->
