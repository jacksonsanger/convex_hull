from __future__ import annotations
import dudraw
from random import random
from Point import Point
from ConvexHullBruteForce import ConvexHullBruteForce
from QuickHull import QuickHull


def main():
    # # Demo of brute force
    # dudraw.set_canvas_size(600, 600)
    # dudraw.set_x_scale(0, 100)
    # dudraw.set_y_scale(0, 100)
    # dudraw.clear(dudraw.GRAY)

    # test_points = [
    #     Point(1, 2),
    #     Point(2, 5),
    #     Point(3, 1),
    #     Point(5, 3),
    #     Point(3, 3),
    #     Point(4, 4)
    # ]

    # #draw the points on the Canvas
    # test_points = []
    # for i in range(50):
    #     x = int(random() * 100)
    #     y = int(random() * 100)
    #     test_points.append(Point(x, y))

    # #draw the points on the Canvas
    # dudraw.set_pen_color(dudraw.BLACK)
    # for point in test_points:
    #     dudraw.filled_circle(point.x, point.y, 1)
    # #find hull and draw it
    # bruteForce = ConvexHullBruteForce()
    # theHull = bruteForce.convexHullBruteForce(test_points)
    # bruteForce.drawConvexHullWithLines(theHull)
    # dudraw.show(float('inf'))

    #Demo of QuickHull
    dudraw.set_canvas_size(600, 600)
    dudraw.set_x_scale(0, 100)
    dudraw.set_y_scale(0, 100)
    dudraw.clear(dudraw.GRAY)

    test_points = []
    numPoints = 25
    for i in range(numPoints):
        x = int(random() * 100)
        y = int(random() * 100)
        test_points.append(Point(x, y))

    #draw the points on the Canvas
    dudraw.set_pen_color(dudraw.BLACK)
    for point in test_points:
        dudraw.filled_circle(point.x, point.y, 1)

    quickHull = QuickHull()

    theHull = quickHull.quickHullStart(test_points)
    quickHull.drawHullWithLines(theHull)
    dudraw.show(float('inf'))


if __name__ == "__main__":
    main()
