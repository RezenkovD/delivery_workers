from abc import ABC, abstractmethod
from typing import Any, List


class IRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Any]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    def create(self, item: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, item: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> bool:
        raise NotImplementedError
