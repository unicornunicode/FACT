import asyncio
import logging

from grpc.aio import server as grpc_server, Server, ServicerContext
from ..controller_pb2 import HelloRequest, HelloReply
from ..controller_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server


class Greeter(GreeterServicer):
    async def SayHello(
        self, request: HelloRequest, context: ServicerContext
    ) -> HelloReply:
        await asyncio.sleep(5)
        return HelloReply(message=f"hello {request.name}")


class Controller:
    server: Server

    def __init__(self):
        self.server = grpc_server()
        add_GreeterServicer_to_server(Greeter(), self.server)

    async def start(self, listen_addr: str):
        logging.info(f"Starting server on {listen_addr}")
        self.server.add_insecure_port(listen_addr)
        await self.server.start()
        await self.server.wait_for_termination()

    async def stop(self, grace: float):
        await self.server.stop(grace)


# vim: set et ts=4 sw=4:
