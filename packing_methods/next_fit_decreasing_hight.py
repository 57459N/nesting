import copy

from packing_methods.base_method import BaseMethod
from rectangle import Rectangle


class NFDH(BaseMethod):
    @staticmethod
    def pack(_rects: list[Rectangle], width: float) -> list[Rectangle]:
        rects = copy.deepcopy(_rects)

        w = 0
        h = 0
        i = 1

        rects.sort(key=lambda r: -r.height)

        rects[0].x = 0
        rects[0].y = 0

        h = 0
        next_h = rects[0].height
        w = rects[0].width

        for idx, r in enumerate(rects[1:]):
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

        return rects
