from dataclasses import dataclass


@dataclass
class Rectangle:
    width: int = 0
    height: int = 0
    x: int = 0
    y: int = 0
    fill: str = None
    outline: str = 'black'
