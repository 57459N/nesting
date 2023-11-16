from random import randint
from tkinter import *
from packing_methods.next_fit_decreasing_hight import NFDH
from rectangle import Rectangle

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
    RECT_AMOUNT = 10

    width = 500
    height = 500
    window = MainFrame(width, height)

    window.create_rectangle(10, 10, width - 10, height - 10, outline='red')
    rs = [Rectangle(randint(50, 100),
                    randint(50, 100),
                    randint(10, 400),
                    randint(10, 400)) for i in range(1, RECT_AMOUNT)]

    rs_packed = NFDH.pack(rs, width)
    window.draw_rectangles(rs_packed)

    window.mainloop()


if __name__ == '__main__':
    main()
