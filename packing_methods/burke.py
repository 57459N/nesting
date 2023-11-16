import copy
from math import ceil, inf

from .base_method import BaseMethod
from rectangle import Rectangle


class Burke(BaseMethod):
    @staticmethod
    def pack(_rects: list[Rectangle], width: float) -> (list[Rectangle], float):
        rects = copy.deepcopy(_rects)
        result = []

        levels = [0 for _ in range(ceil(width))]

        while rects:
            lowest_level = min(levels)
            start, space = Burke._find_lowest_plato(levels)

            placed = False
            idx = 0
            for r in rects:
                if r.width <= space:
                    r.x = start
                    r.y = lowest_level
                    for i in range(start, start + r.width):
                        levels[i] += r.height
                    placed = True
                    break
                idx += 1

            if placed:
                result.append(rects[idx])
                rects.pop(idx)
            else:
                Burke._raise_lowest_level(levels)

        highest = max(result, key= lambda x: x.y + x.height)
        return result, highest.y + highest.height

    @staticmethod
    def _find_lowest_plato(levels: list[int]) -> (int, float):
        # returns index of beginning of plato and its width

        lowest_level = min(levels)
        cur_len = 0
        max_len = 0
        cur_start_pos = None
        max_len_start_pos = None

        for i, level in enumerate(levels):
            if level == lowest_level:
                if cur_len == 0:
                    cur_start_pos = i
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                    max_len_start_pos = cur_start_pos
                cur_len = 0

            if cur_len > max_len:
                max_len = cur_len
                max_len_start_pos = cur_start_pos

        return max_len_start_pos, max_len

    @staticmethod
    def _raise_lowest_level(levels: list[int]) -> None:
        lowest = min(levels)

        while lowest in levels:
            start, length = Burke._find_lowest_plato(levels)

            left_neighbor = levels[start - 1]
            right_neighbor = levels[start + length] if start + length < len(levels) else inf

            lowest_neighbor = min(left_neighbor, right_neighbor)

            for i in range(start, start + length):
                levels[i] = lowest_neighbor
