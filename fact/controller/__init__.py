import asyncio
import logging

from grpc.aio import server as grpc_server, Server, ServicerContext
from google.protobuf.empty_pb2 import Empty
from ..controller_pb2 import WorkerRegistration, WorkerAcceptance, WorkerTask
from ..controller_pb2_grpc import WorkerTasksServicer, add_WorkerTasksServicer_to_server


class WorkerTasks(WorkerTasksServicer):
    async def Register(
        self, request: WorkerRegistration, context: ServicerContext
    ) -> WorkerAcceptance:
        await asyncio.sleep(5)
        uuid = b"TODO"
        return WorkerAcceptance(uuid=uuid)

    async def GetTask(
            self, request: Empty, context: ServicerContext
            ) -> WorkerTask:
        await asyncio.sleep(1)
        return WorkerTask(task_none=None)


class Controller:
    listen_addr: str
    server: Server

    def __init__(self, listen_addr: str):
        self.listen_addr = listen_addr
        self.server = grpc_server()
        # Services
        worker_tasks = WorkerTasks()
        add_WorkerTasksServicer_to_server(worker_tasks, self.server)

    async def start(self):
        logging.info(f"Starting server on {self.listen_addr}")
        self.server.add_insecure_port(self.listen_addr)
        await self.server.start()
        await self.server.wait_for_termination()

    async def stop(self, grace: float):
        await self.server.stop(grace)


# vim: set et ts=4 sw=4:
