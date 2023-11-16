import copy

from .base_method import BaseMethod
from rectangle import Rectangle


class FFDH(BaseMethod):
    @staticmethod
    def pack(_rects: list[Rectangle], width: float) -> (list[Rectangle], float):
        rects = copy.deepcopy(_rects)

        rects.sort(key=lambda r: -r.height)

        rects[0].x = 0
        rects[0].y = 0

        ws = [rects[0].width]
        hs = [0]

        h_next = rects[0].height

        for r in rects[1:]:
            placed = False
            for idx, (w, h) in enumerate(zip(ws, hs)):
                if width - w >= r.width:
                    r.x = w
                    r.y = h
                    ws[idx] += r.width
                    placed = True
                    break
            if not placed:
                r.x = 0
                r.y = h_next

                ws.append(r.width)
                hs.append(h_next)
                h_next += r.height

        return rects, h_next
