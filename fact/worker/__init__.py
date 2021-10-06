import asyncio
import logging
from typing import AsyncIterable

from grpc.aio import insecure_channel
from ..controller_pb2 import (
    SessionResults,
    SessionEvents,
    WorkerRegistration,
    WorkerTaskResult,
    TaskNoneResult,
)
from ..controller_pb2_grpc import WorkerTasksStub
from ..utils.itertools import chain
from .stream import Stream


log = logging.getLogger("worker")


class Worker:
    controller_addr: str

    def __init__(self, controller_addr: str):
        self.controller_addr = controller_addr

    async def start(self):
        async with insecure_channel(self.controller_addr) as channel:
            stub = WorkerTasksStub(channel)

            first_result = SessionResults(
                worker_registration=WorkerRegistration(
                    previous_uuid=b"TODO", hostname="todo"
                )
            )

            response_stream: Stream[SessionResults] = Stream()
            responses: AsyncIterable[SessionResults] = chain(
                [
                    first_result,
                ],
                response_stream,
            )
            session_events: AsyncIterable[SessionEvents] = stub.Session(responses)

            first_event = await session_events.__aiter__().__anext__()
            if first_event.WhichOneof("event") != "worker_acceptance":
                return

            async for session_event in session_events:
                worker_task = session_event.worker_task
                log.debug(worker_task)

                await asyncio.sleep(1)

                await response_stream.add(
                    SessionResults(
                        worker_task_result=WorkerTaskResult(task_none=TaskNoneResult())
                    )
                )

    async def stop(self):
        pass


# vim: set et ts=4 sw=4:
