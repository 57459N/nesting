import random
from random import randint
from tkinter import *
from rectangle import Rectangle
from packing_methods.next_fit_decreasing_high import NFDH
from packing_methods.first_fit_decreasing_high import FFDH
from packing_methods.burke import Burke


class MainFrame(Tk):
    def __init__(self, width, height, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.height = height
        self.width = width

        self.geometry(f'{width}x{height}')

        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.pack()

    def create_rectangle(self, *args, **kwargs):
        self.canvas.create_rectangle(*args, **kwargs)

    def draw_rectangle(self, rect: Rectangle):
        self.canvas.create_rectangle(
            self._transform_coords(rect.x, rect.y),
            self._transform_coords(rect.x + rect.width, rect.y + rect.height),
            fill=rect.fill,
            outline=rect.outline
        )

    def _transform_coords(self, x, y):
        # transforming coords from first to fourth square
        return x, self.height - y

    def draw_rectangles(self, rects: list[Rectangle]):
        for r in rects:
            self.draw_rectangle(r)


def main():
    random.seed(1)

    RECT_AMOUNT = 50

    width = 1500
    height = 1080

    rs = [Rectangle(randint(10, 250),
                    randint(10, 250),
                    0,
                    0,
                    fill=random.choice(['#673147', '#ADD8E6']),
                    outline='black') for _ in range(1, RECT_AMOUNT)]

    methods = [Burke, FFDH, NFDH]

    windows = []

    for m in methods:
        packed, h = m.pack(rs, width)

        w = MainFrame(width, height)
        w.title(f'{m.__name__} - {h}')
        w.draw_rectangles(packed)
        windows.append(w)
        print(m.__name__, ' packed')

    while True:
        for w in windows:
            w.update()


if __name__ == '__main__':
    main()
