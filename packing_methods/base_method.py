from abc import ABC
from rectangle import Rectangle


class BaseMethod(ABC):
    @staticmethod
    def pack(_rects: list[Rectangle], width: float) -> (list[Rectangle], float):
        pass
