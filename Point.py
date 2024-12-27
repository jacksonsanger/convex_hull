from __future__ import annotations
import dudraw
from random import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other: Point):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self) -> str:
        return str(self)