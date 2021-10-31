<div align="center">
  <h1><img src="ui/public/logo.svg" alt="FACT" width="320" /></h1>
  <h3>Forensic Artefact Collection Tool</h3>
</div>

# Overview

FACT is a tool to collect, process and visualise forensic data from clusters of
machines running in the cloud or on-premise.

# Deployment

For a basic single-node deployment, we recommend using [Docker](https://docs.docker.com/get-docker/)
and [Docker Compose](https://docs.docker.com/compose/install/). Start the stack 
using:

```sh
docker-compose up -d
```

Read [`docker-compose.yaml`](docker-compose.yaml) for configuration and
requirements.

## Multi-Node Deployment

We have not yet documented and tested multi-node deployments, thus you are on
your own for now.

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- vim: set conceallevel=2 et ts=2 sw=2: -->
