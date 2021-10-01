import logging

from grpc.aio import insecure_channel
from ..controller_pb2 import HelloRequest, HelloReply
from ..controller_pb2_grpc import GreeterStub


class Worker:
    controller_addr: str

    def __init__(self, controller_addr: str):
        self.controller_addr = controller_addr

    async def start(self):
        async with insecure_channel(self.controller_addr) as channel:
            stub = GreeterStub(channel)
            response: HelloReply = await stub.SayHello(HelloRequest(name="worker"))
            logging.info(f"Recieved {response.message}")

    async def stop(self):
        pass


# vim: set et ts=4 sw=4:
