<div align="center">
  <h1><img src="ui/public/logo.svg" alt="FACT" width="320" /></h1>
  <h3>Forensic Artefact Collection Tool</h3>
</div>

# Overview

FACT is a tool to collect, process and visualise forensic data from clusters of
machines running in the cloud or on-premise.

# Deployment

For a basic single-node deployment, we recommend using [Docker](https://docs.docker.com/get-docker/)
and [Docker Compose](https://docs.docker.com/compose/install/). First, read
[`docker-compose.yaml`](docker-compose.yaml) for configuration and requirements.
Then, start the stack using:

```sh
docker-compose up -d
```

See [INSTALL.md](docs/INSTALL.md) for more details and other deployment methods.

See [USAGE.md](docs/USAGE.md) for details on using FACT.

# Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md).

# Screenshots

![targets-1](https://user-images.githubusercontent.com/1705906/140052919-23f7e567-ab52-441e-982e-1a0ec819d17c.png)
![tasks-1](https://user-images.githubusercontent.com/1705906/140052963-f39cce21-5634-4235-afa2-193e1621ba50.png)
![dashboard-1](https://user-images.githubusercontent.com/1705906/140052998-09c39a3f-b690-4c62-a2ba-9734244ace63.png)

<!-- vim: set conceallevel=2 et ts=2 sw=2: -->
