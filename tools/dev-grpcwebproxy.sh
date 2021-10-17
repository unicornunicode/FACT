#!/bin/sh

set -euo pipefail

grpcwebproxy --backend_addr=localhost:5123 --backend_tls=false --server_http_debug_port=5124 --run_tls_server=false --allow_all_origins
