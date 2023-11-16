import copy

from .base_method import BaseMethod
from rectangle import Rectangle


class NFDH(BaseMethod):
    @staticmethod
    def pack(_rects: list[Rectangle], width: float) -> (list[Rectangle], float):
        rects = copy.deepcopy(_rects)

        rects.sort(key=lambda r: -r.height)

        rects[0].x = 0
        rects[0].y = 0

        h = 0
        next_h = rects[0].height
        w = rects[0].width

        for r in rects[1:]:
            if width - w >= r.width:
                r.x = w
                r.y = h
                w += r.width
            else:
                h = next_h
                next_h += r.height
                r.x = 0
                r.y = h
                w = r.width

        return rects, next_h
