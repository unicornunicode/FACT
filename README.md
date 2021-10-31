<div align="center">
  <h1><img src="ui/public/logo.svg" alt="FACT" width="320" /></h1>
  <h3>Forensic Artefact Collection Tool</h3>
</div>

# Overview

FACT is a tool to collect, process and visualise forensic data from clusters of
machines running in the cloud or on-premise.

# Manual Deployment

You'll need Python 3.9+ on your controller node and worker nodes, and Node.js
for the UI. Additionally,
you'll need to install [grpcwebproxy](https://github.com/improbable-eng/grpc-web/tree/master/go/grpcwebproxy), [Elasticsearch and Kibana](https://www.elastic.co/start).

Install FACT on the controller node and worker nodes with:

```sh
sudo pip install https://github.com/unicornunicode/FACT.git
```

Start the controller node using:

```sh
python -m fact.controller --listen-addr [::]:5123 --elasticsearch http://$ELASTICSEARCH_ADDRESS:9200
```

Start the worker nodes using:

```sh
python -m fact.worker --controller-addr $CONTROLLER_ADDRESS:5123
```

Start the UI using:

```sh
git clone --depth 1 https://github.com/unicornunicode/FACT.git
cd ui
npm ci
npm run build
npm start
```

# Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- vim: set conceallevel=2 et ts=2 sw=2: -->
