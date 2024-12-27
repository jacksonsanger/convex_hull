from __future__ import annotations
import dudraw
from random import random
from Point import Point


class ConvexHullBruteForce:    
    #return true if the point i is a left turn from the line defined by ab
    def leftTurn(self, a: Point, b: Point, i: Point):
        #determine x and y components of vectors ab and bi
        abXComp = b.x - a.x
        abYComp = b.y - a.y
        biXComp = i.x - b.x
        biYComp = i.y - b.y
        #compute cross product (vab X vbi)
        crossProdct = (abXComp * biYComp) - (abYComp * biXComp)
        return crossProdct > 0


    #S is the list of points in 2D space, returns a list of the points of the hull
    def convexHullBruteForce(self, S: list)-> list:
        #create empty list which the points in the hull will be added to
        CH = []
        #iterate over every point
        for i in range(len(S)):
            #iterate over every possible other point j to form a line ij
            for j in range(i+1, len(S)):
                #keep track of the number of left turns
                #we only need to use left turns because we are just checking if every point k is either above line ij or none are
                leftTurnCount = 0
                for k in range(len(S)):
                    #compare every other point besides point i and j themselves
                    if k != i and k != j:
                        #check if point k is a left turn from the line ij
                        if self.leftTurn(S[i], S[j], S[k]):
                            leftTurnCount += 1
                #After looking at every possible point k for every possible line ij, add to the hull if
                #there were either no left turns or all left turns
                if leftTurnCount == 0 or leftTurnCount == len(S) - 2:
                        CH.append(S[i])
                        CH.append(S[j])
        return CH

    #takes in an array that represents a ConvexHull and draws it on the canvas
    def drawConvexHullWithLines(self, CH: list):
        #we will set the pen color to green for clarity
        dudraw.set_pen_color(dudraw.GREEN)
        #for each pair of points (why we have a step of 2)
        for i in range(0, len(CH), 2):
            #draw a line between two consecutive points
            dudraw.line(CH[i].x, CH[i].y, CH[i+1].x, CH[i+1].y)
