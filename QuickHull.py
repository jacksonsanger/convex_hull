from __future__ import annotations
import dudraw
from random import random
from Point import Point

class QuickHull:    
    #return true if the point i is a left turn from the line defined by ab
    def leftTurn(self, a: Point, b: Point, i: Point):
        #determine x and y components of vectors ab and bi
        abXComp = b.x - a.x
        abYComp = b.y - a.y
        biXComp = i.x - b.x
        biYComp = i.y - b.y
        #compute cross product (vab X vbi)
        crossProdct = (abXComp * biYComp) - (abYComp * biXComp)
        #greater than 0 makes it strictly left
        return crossProdct > 0

    def valueBasedOnLineDistance(self, a: Point, b: Point, p: Point):
        abXComp = b.x - a.x
        abYComp = b.y - a.y
        bpXComp = p.x - a.x
        bpYComp = p.y - a.y
        return abs(abXComp * bpYComp - abYComp * bpXComp)

    #takes in a set of points and starts the quick hull algorithm
    def quickHullStart(self, S: list):
    #get min and max X values, points a and b
        min = S[0].x
        max = S[0].x
        a = S[0]
        b = S[0]
        for i in range(len(S)):
            if S[i].x < min:
                min = S[i].x
                a = S[i]
            if S[i].x > max:
                max = S[i].x
                b = S[i]
        #make a list of all points above AB
        SUpper = []
        #make a list of all points below AB
        SLower = []
        for i in range(len(S)):
            if self.leftTurn(a, b, S[i]):
                SUpper.append(S[i])
            if self.leftTurn(b, a, S[i]):
                SLower.append(S[i])
        #after computing a and b, we will add them to the result, a and b are guaranteed to be a part of each hull
        UpperHull = self.quickHull(a, b, SUpper, [a, b])
        LowerHull = self.quickHull(b, a, SLower, [a, b])
        return UpperHull, LowerHull

    def quickHull(self, a: Point, b: Point, S: list, Result: list):
        #base case, list is empty. Return the result
        if len(S) == 0:
            return Result
        #find c, the furthest point, we will set it to a initially
        maxDistance = -1
        c = None
        for i in range(len(S)):
            distance = self.valueBasedOnLineDistance(a, b, S[i])
            if distance > maxDistance:
                maxDistance = distance
                c = S[i]
        if c is None:
            return Result
        #after finding C, add it to result
        Result.append(c)
        #get Set left, the list of points strictly left of AC
        left = []
        #get set right, the list of points strictly left of CB
        right = []
        for i in range(len(S)):
            if self.leftTurn(a, c, S[i]):
                left.append(S[i])
            if self.leftTurn(c, b, S[i]):
                right.append(S[i])     

        #make recursive calls
        Result = self.quickHull(a, c, left, Result)
        Result = self.quickHull(c, b, right, Result)
        return Result


    #takes in a tuple that respresents the hull, the first value is the upper hull, second is the lower
    def drawHullWithLines(self, upperAndLower: tuple[list, list]):
        dudraw.set_pen_color(dudraw.GREEN)
        #get the upper and lower from the tuple
        upper = upperAndLower[0]
        lower = upperAndLower[1]
        #sort each with respect to x
        upper.sort(key = lambda point : point.x)
        lower.sort(key = lambda point : point.x)
        #draw a line between each consecutive pairs of points in each hull
        for i in range(len(upper)-1):
            dudraw.line(upper[i].x, upper[i].y, upper[i+1].x, upper[i+1].y)
        for i in range(len(lower)-1):
            dudraw.line(lower[i].x, lower[i].y, lower[i+1].x, lower[i+1].y)