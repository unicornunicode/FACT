PYTHON:=python

PROTO_SRC=proto
PROTO_OUT=fact
PROTOS= \
	controller

.PHONY: all
all:

.PHONY: proto
proto: $(addprefix $(PROTO_OUT)/,$(addsuffix _pb2.py,$(PROTOS)))

$(PROTO_OUT)/%_pb2.py: $(PROTO_SRC)/$(PROTO_OUT)/%.proto
	$(PYTHON) -m grpc_tools.protoc -I$(PROTO_SRC) --python_out=. --grpc_python_out=. --mypy_out=. --proto_path=$(PROTO_SRC) $<
