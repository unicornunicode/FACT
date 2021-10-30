from abc import abstractmethod
from typing import Protocol, Tuple, List

from ..storage import Session


class TargetAccess(Protocol):
    @abstractmethod
    def collect_image(
        self, remote_path_of_image: str, storage_session: Session, bufsize: int = 65535
    ) -> None:
        pass

    @abstractmethod
    def get_all_available_disk(self) -> List[Tuple[str, int, str, str]]:
        pass


# vim: set et ts=4 sw=4:
