import logging

from fact.exceptions import SSHInfoError, TargetRuntimeError
from fact.utils import uncompress_gzip

from pssh.clients import ParallelSSHClient
from pssh.exceptions import PKeyFileError

# from pssh.utils import enable_logger
# Increase default logging level to prevent unnecessary logging of remote command results to stdout/file due to pssh.utils implementation
# enable_logger(logging.getLogger("pssh.host_logger"), level=logging.NOTSET)
# ^^ TODO: Check when running, only a set of host-logger run. Understand what the purpose of this is. Able to direct to stderr???

log = logging.getLogger(__name__)


class SSHAccessInfo:
    """Core information needed for SSH connection to the target. Refer to pssh documentation"""

    def __init__(
        self,
        user: str,
        hosts: list[str],
        port: int,
        privateKey_path: str = None,
        password: str = None,
    ):
        self.user = user
        self.hosts = hosts
        self.port = port
        self.privateKey_path = privateKey_path
        self.password = password

        # self.hosts: We support only a list of 1 host for now.
        if type(self.hosts) is not list:
            raise SSHInfoError("Input is not a list of 1 host", self.hosts)
        if len(self.hosts) != 1:
            raise SSHInfoError("More than 1 target host is provided", self.hosts)


class SSHProxyInfo:
    """Optional fields for connecting to targets via a proxy server. Supported by pssh."""

    def __init__(
        self,
        proxy_user: str = None,
        proxy_host: str = None,
        proxy_port: int = None,
        proxy_password: str = None,
        proxy_pkey: str = None,
    ):
        self.proxy_user = proxy_user
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_password = proxy_password
        self.proxy_pkey = proxy_pkey


class SSHAccessInfoOptional:
    """Optional fields that may be needed, has to be supported by pssh."""

    def __init__(
        self,
        num_retries: int = 3,
        retry_delay: int = 5,
        timeout: float = None,
        pool_size: int = 100,
        host_config: list = None,
        allow_agent: bool = True,
        identity_auth: bool = True,
        forward_ssh_agent: bool = False,
        keepalive_seconds: int = 60,
    ):
        self.num_retries = num_retries
        self.retry_delay = retry_delay
        self.timeout = timeout
        self.pool_size = pool_size
        self.host_config = host_config
        self.allow_agent = allow_agent
        self.identity_auth = identity_auth
        self.forward_ssh_agent = forward_ssh_agent
        self.keepalive_seconds = keepalive_seconds


class TargetEndpoint:
    def __init__(
        self,
        SSHAccessInfo: SSHAccessInfo,
        SSHProxyInfo: SSHProxyInfo,
        SSHAccessInfoOptional: SSHAccessInfoOptional,
    ):
        self.SSHAccessInfo = SSHAccessInfo
        self.SSHProxyInfo = SSHProxyInfo
        self.SSHAccessInfoOptional = SSHAccessInfoOptional
        try:
            self.client_session = ParallelSSHClient(
                self.SSHAccessInfo.hosts,
                user=self.SSHAccessInfo.user,
                port=self.SSHAccessInfo.port,
                pkey=self.SSHAccessInfo.privateKey_path,
                password=self.SSHAccessInfo.password,
                num_retries=self.SSHAccessInfoOptional.num_retries,
                timeout=self.SSHAccessInfoOptional.timeout,
                pool_size=self.SSHAccessInfoOptional.pool_size,
                allow_agent=self.SSHAccessInfoOptional.allow_agent,
                host_config=self.SSHAccessInfoOptional.host_config,
                retry_delay=self.SSHAccessInfoOptional.retry_delay,
                proxy_host=self.SSHProxyInfo.proxy_host,
                proxy_port=self.SSHProxyInfo.proxy_port,
                proxy_user=self.SSHProxyInfo.proxy_user,
                proxy_password=self.SSHProxyInfo.proxy_password,
                proxy_pkey=self.SSHProxyInfo.proxy_pkey,
                forward_ssh_agent=self.SSHAccessInfoOptional.forward_ssh_agent,
                keepalive_seconds=self.SSHAccessInfoOptional.keepalive_seconds,
                identity_auth=self.SSHAccessInfoOptional.identity_auth,
            )
        except PKeyFileError as e:
            raise SSHInfoError("Error finding private key") from e

    def collect_image(
        self, remote_path_of_image: str, path_to_save: str, decompress: bool = True
    ):
        """
        Collects the image of a file. Can be a disk, or process, or file in general.
            The remote user must have root priv.
        :param remote_path_to_image: Path of the remote image
        :param path_to_save: Full path + filename of the file_output
        :param decompress: Whether to decompress the resulting GZ file. Defaults to True
        :raises TargetRuntimeError: If there is problem during the remote file acquisition
        """

        remote_command = (
            "dd if=" + remote_path_of_image + " bs=4096 conv=noerror | gzip -1 -f"
        )
        log.info(f"Executing remote command: {remote_command}")

        remote_output = self.client_session.run_command(
            remote_command, sudo=True, encoding="iso-8859-1"
        )

        gz_path = path_to_save + ".gz"
        try:
            with open(gz_path, "wb") as f:
                for host_output in remote_output:
                    for line in host_output.buffers.stdout.rw_buffer:
                        f.write(line)
        except OSError as e:
            raise TargetRuntimeError("Unable to open file for writing", e) from e

        if decompress:
            uncompress_gzip(gz_path)
