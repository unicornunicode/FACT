# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fact import controller_pb2 as fact_dot_controller__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class WorkerTasksStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/WorkerTasks/Register',
                request_serializer=fact_dot_controller__pb2.WorkerRegistration.SerializeToString,
                response_deserializer=fact_dot_controller__pb2.WorkerAcceptance.FromString,
                )
        self.GetTask = channel.unary_unary(
                '/WorkerTasks/GetTask',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=fact_dot_controller__pb2.WorkerTask.FromString,
                )


class WorkerTasksServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerTasksServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=fact_dot_controller__pb2.WorkerRegistration.FromString,
                    response_serializer=fact_dot_controller__pb2.WorkerAcceptance.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=fact_dot_controller__pb2.WorkerTask.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'WorkerTasks', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkerTasks(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/WorkerTasks/Register',
            fact_dot_controller__pb2.WorkerRegistration.SerializeToString,
            fact_dot_controller__pb2.WorkerAcceptance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/WorkerTasks/GetTask',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            fact_dot_controller__pb2.WorkerTask.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
