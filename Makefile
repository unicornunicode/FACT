PYTHON:=python

PROTO_SRC=proto
PROTO_OUT=fact
PROTO_OUT_UI=ui/proto
PROTOS= \
	controller \
	management \
	tasks
PROTOS_UI= \
	management \
	tasks

.PHONY: all
all:

.PHONY: proto
proto: $(addprefix $(PROTO_OUT)/,$(addsuffix _pb2.py,$(PROTOS)))
.PHONY: proto-ts
proto-ts: $(addprefix $(PROTO_OUT_UI)/$(PROTO_OUT)/,$(addsuffix .ts,$(PROTOS_UI)))

$(PROTO_OUT)/%_pb2.py: $(PROTO_SRC)/$(PROTO_OUT)/%.proto
	$(PYTHON) -m grpc_tools.protoc -I$(PROTO_SRC) --python_out=. --grpc_python_out=. --mypy_out=. --proto_path=$(PROTO_SRC) $<

$(PROTO_OUT_UI)/$(PROTO_OUT)/%.ts: $(PROTO_SRC)/$(PROTO_OUT)/%.proto
	$(PYTHON) -m grpc_tools.protoc -I$(PROTO_SRC) --plugin=ui/node_modules/.bin/protoc-gen-ts_proto --ts_proto_out=$(PROTO_OUT_UI) --ts_proto_opt=esModuleInterop=true --ts_proto_opt=outputClientImpl=grpc-web --proto_path=$(PROTO_SRC) $<
