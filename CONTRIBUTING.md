# Requirements

- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org)
- [Node.js](https://nodejs.org)
- [Elasticsearch and Kibana](https://www.elastic.co/start)
- A decent amount of disk space for disk images
- At least 6GB of RAM available

# Setup

If you haven't already, clone the repository.

Install development dependencies using:

```sh
# Set up virtual environment and install dependencies
poetry install --no-root
# Enter virtual environment
poetry shell
# Install grpcwebproxy
python tools/download-grpcwebproxy.py
# Optional: Install Git hooks to check your code and commit messages
python tools/hooks.py install
# Optional: When working on the UI
cd ui
npm install
```

# Checks

Before submitting commits or pull requests, consider running the code formatter,
linter, type checks and tests:

```sh
# With Git hooks installed
git commit
# Without Git hooks installed
python tools/pre-commit.py
```

If you wish to skip the linter, type checks and tests:

```sh
# With Git hooks installed
SKIP_CHECKS=y git commit
# Without Git hooks installed
SKIP_CHECKS=y python tools/pre-commit.py
```

# Tools

All the tools in `tools/` must be run from the project root.

# Writing Messages

We follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/#summary)
for commit messages and pull requests:

```
<type>[optional scope]: <description>
```

We use the following types:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **test**: Adding missing tests or correcting existing tests
- **ci**: Changes to our CI configuration files and scripts
- **chore**: Other changes that don't modify src or test files
- **wip**: Work-in-progress

To help you write commit messages, you can use:

```sh
# Asks you a series of questions about your commit
mkcommit --autoselect
```

With Git hooks installed, your commit messages will automatically be checked
upon commit.

# Updating gRPC Protocol

After any change to the gRPC protocol as defined in the `.proto` files, the
services, stubs and types must be regenerated using the protocol buffer compiler.
This can be done by running:

```sh
# Enter virtual environment if you haven't already
poetry shell
# Compile the files specified in Makefile if they changed
make proto
# Do the same for the UI
make proto-ts
```

When `make` is unavailable, directly invoke the compiler:

```sh
python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. --mypy_out=. --proto_path=proto proto/fact/controller.proto
```

# Running

For development, a script combining the controller and worker components
communicating on the loopback interface can be used:

```sh
# Enter virtual environment if you haven't already
poetry shell
# Start the development instance
python -m fact.dev
```

And the UI can be run with

```sh
cd ui
npm run dev
```

# Running (Docker Compose)

If installing the above requirements is something you don't want to do, you can
use Docker Compose to run a full development environment. Before you start,
you'll need:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

If you haven't already, clone the repository.

Build and start every component in development mode using:

```sh
docker-compose -f docker-compose.dev.yaml up
# Or to run in the background
docker-compose -f docker-compose.dev.yaml up --detach
# Or when dependencies have changed
docker-compose -f docker-compose.dev.yaml up --build
```

The controller and worker are started independently. After a code change,
restart either process using:

```sh
docker-compose -f docker-compose.dev.yaml restart controller
docker-compose -f docker-compose.dev.yaml restart worker
```

The UI is started with `npm run dev`, which automatically loads new changes. If
a hard restart is needed, that can be done using:

```sh
docker-compose -f docker-compose.dev.yaml restart ui
```

If you want to clean up the Docker volumes, you can use:

```sh
docker-compose -f docker-compose.dev.yaml down --volumes
```

<!-- vim: set conceallevel=2 et ts=2 sw=2: -->
