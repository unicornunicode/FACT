import asyncio
import logging
from pathlib import Path
from subprocess import DEVNULL
from typing import Optional

from ..utils.net import split_addr


log = logging.getLogger(__name__)


default_binary = Path(__file__).parent / "grpcwebproxy"


class GRPCWebProxy:
    """
    GRPCWebProxy starts the grpcwebproxy binary
    """

    controller_addr: str
    listen_addr: str
    binary: Path
    process: Optional[asyncio.subprocess.Process] = None

    def __init__(
        self, listen_addr: str, controller_addr: str, binary: Path = default_binary
    ):
        self.listen_addr = listen_addr
        self.controller_addr = controller_addr
        self.binary = binary

    async def start(self) -> None:
        log.info(f"Starting grpcwebproxy on {self.listen_addr}")
        bind_address, http_debug_port = split_addr(self.listen_addr)
        args = []
        # Backend
        args.append("--backend_tls=false")
        args.append(f"--backend_addr={self.controller_addr}")
        # Server
        args.append("--run_tls_server=false")
        args.append(f"--server_bind_address={bind_address}")
        args.append(f"--server_http_debug_port={http_debug_port}")
        args.append("--allow_all_origins")
        # Create process
        self.process = await asyncio.create_subprocess_exec(
            self.binary, *args, stdin=DEVNULL
        )
        log.info(f"started grpcwebproxy with pid {self.process.pid}")
        await self.process.wait()
        log.info(f"grpcwebproxy exited with code {self.process.returncode}")

    async def stop(self) -> None:
        if self.process is None:
            return
        try:
            self.process.terminate()
            await self.process.wait()
        except Exception:
            pass


# vim: set et ts=4 sw=4:
