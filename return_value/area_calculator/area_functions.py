"""
This module contains the AreaCalculator class 
which provides methods to calculate the area of various geometric shapes.
"""

class AreaCalculator:
    @staticmethod
    def area_square(side: float) -> float:
        return side * side

    @staticmethod
    def area_rectangle(length: float, width: float) -> float:
        return length * width

    @staticmethod
    def area_triangle(base: float, height: float) -> float:
        return 0.5 * base * height

    @staticmethod
    def area_circle(radius: float) -> float:
        return 3.141592653589793 * radius * radius