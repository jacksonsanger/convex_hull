from __future__ import annotations
import dudraw
from random import random
from Point import Point
from ConvexHullBruteForce import ConvexHullBruteForce
from QuickHull import QuickHull
from time import time
def main():
    # #Run time is O(n^3)
    # print("Empirical Testing of Brute Force:")
    # #print out labels for each column in a readable way
    # print(f"n:\telapsed time:\t\ttime per call:")
    # #initialize a variable for the number of times we will repeat the algorithm
    # num_trials = 10000
    # #make a brute force object
    # bf = ConvexHullBruteForce()
    # #loop over varying input sizes
    # for n in [10, 20, 40, 80]:
    #     #generate our test points of varying sizes
    #     test_points = []
    #     for i in range(n):
    #         x = int(random() * 100)
    #         y = int(random() * 100)
    #         test_points.append(Point(x, y))
    #     #start the timer
    #     start = time()
    #     #repeat the algorithm num trials times
    #     for i in range(num_trials):
    #         #run the algorithm
    #         bf.convexHullBruteForce(test_points)
    #     #stop the timer
    #     stop = time()
    #     #calculate elapsed time
    #     elapsed_time = stop - start
    #     #print out the results in a way that is easy to read
    #     print(f"{n}\t{elapsed_time}\t{elapsed_time/num_trials}")

    #Run time is O(nlogn)
    print("Empirical Testing of QuickHull:")
    #print out labels for each column in a readable way
    print(f"n:\telapsed time:\t\ttime per call:")
    #initialize a variable for the number of times we will repeat the algorithm
    num_trials = 10000
    #make a brute force object
    qh = QuickHull()
    #loop over varying input sizes
    for n in [100, 200, 400, 800, 1600, 3200, 6400]:
        #generate our test points of varying sizes
        test_points = []
        for i in range(n):
            x = int(random() * 100)
            y = int(random() * 100)
            test_points.append(Point(x, y))
        #start the timer
        start = time()
        #repeat the algorithm num trials times
        for i in range(num_trials):
            #run the algorithm
            qh.quickHullStart(test_points)
        #stop the timer
        stop = time()
        #calculate elapsed time
        elapsed_time = stop - start
        #print out the results in a way that is easy to read
        print(f"{n}\t{elapsed_time}\t{elapsed_time/num_trials}")

if __name__ == "__main__":
    main()
