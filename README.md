
<div align="center">
  <h1><img src=".github/logo.svg" alt="FACT" width="320" /></h1>
  <h3>Forensic Artefact Collection Tool</h3>
</div>

# Overview

FACT is a tool to collect, process and visualise forensic data from clusters of
machines running in the cloud or on-premise.

# Manual Deployment

You'll need Python 3.9+ on your controller node and worker nodes, and a 
PostgreSQL database.

Install FACT on the controller node and worker nodes with:
```sh
sudo pip install https://github.com/unicornunicode/FACT.git
```

## Controller

Start the controller node using:
```sh
python -m fact.controller --listen-addr [::]:5123
```

## Worker

Start the worker nodes using:
```sh
python -m fact.worker --controller-addr $CONTROLLER_ADDRESS:5123
```

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).


<!-- vim: set conceallevel=2 et ts=2 sw=2: -->
