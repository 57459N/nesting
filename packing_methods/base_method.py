from abc import ABC
from rectangle import Rectangle


class BaseMethod(ABC):
    @staticmethod
    def pack(rects: list[Rectangle], width: float) -> list[Rectangle]:
        pass
