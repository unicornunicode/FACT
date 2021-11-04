# Installation

To install FACT for deployment

1. [Docker Compose Single-node Deployment](#docker-compose-single-node-deployment)
1. [Kubernetes Multi-node Deployment](#kubernetes-multi-node-deployment)

For a development environment, see [CONTRIBUTING.md](CONTRIBUTING.md)

## Docker Compose Single-node Deployment

You can run FACT on platforms supported by Docker Desktop using our Docker
Compose setup. *This setup is not meant for production use yet.*

### Prerequisites

1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/install/)
3. A large amount of disk space for disk images
4. At least 3GB of RAM available, 8GB recommended

### Configuring `docker-compose.yml`

[Download `docker-compose.yml`](https://github.com/unicornunicode/FACT/raw/main/docker-compose.yaml)
from this repository. Open it in a text editor.

Replace `${HOST_IP}` with the IP address of your machine running Docker. You can
find your IP address using your operating system tools or when using Docker
Desktop, try `host.docker.internal`.

The IP address can be either the one used to connect to the internet, or when
using Docker Desktop, the internal IP address of the underlying Docker Desktop
VM. It should be reachable from both your host and within Docker.

### Starting all services

Open a shell, enter the directory containing `docker-compose.yml` and start all
the services using:

```sh
docker-compose up -d
```

View the [documentation](https://docs.docker.com/compose/reference/) for
`docker-compose` for other operations.

Once all the services have started, you can open [http://localhost:3000](http://localhost:3000)
for the UI, and [http://localhost:5601](http://localhost:5601/app/discover) for
the search UI (Kibana). Data will be populated after your first Ingest.

### Tips

- When using Docker Desktop, remember to allocate enough disk space to your
  Docker Desktop machine.
- Do keep tabs on the amount of disk space left.

## Kubernetes Multi-node Deployment

We have not yet documented and tested multi-node deployments, thus you are on
your own for now. We have plans to write Kubernetes manifests for multi-node
deployments.

<!-- vim: set conceallevel=2 et ts=2 sw=2: -->
