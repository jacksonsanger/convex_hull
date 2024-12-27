# Convex Hull Algorithms: Brute Force and QuickHull

This project implements and compares two convex hull algorithms, **Brute Force** and **QuickHull**, using Python. The algorithms are applied to sets of randomly generated 2D points, and their performance is evaluated both visually and empirically.

## Overview

The project provides implementations of:
- **Brute Force Convex Hull Algorithm**: Computes the convex hull by evaluating all possible edges to determine if they form part of the hull.
- **QuickHull Algorithm**: A recursive, divide-and-conquer approach that efficiently computes the convex hull by finding points furthest from partitioning lines.

Key implementation details include:
- Custom point representation with a `Point` class.
- Distance computations using cross-product methods for QuickHull.
- Graphical output using a drawing library for visual validation.
- Empirical runtime analysis of both algorithms over increasing input sizes.

## File Structure

- **`ConvexHullBruteForce.py`**: Implementation of the brute force convex hull algorithm.
- **`QuickHull.py`**: Implementation of the QuickHull algorithm and associated helper methods.
- **`Point.py`**: Class defining 2D points with basic utilities like distance computation.
- **`main1DrawingDemo.py`**: Demonstrates the convex hull algorithms graphically by drawing points and their hulls.
- **`main2EmpiricalTesting.py`**: Compares runtime performance of the Brute Force and QuickHull algorithms.

## Features

1. **Brute Force Algorithm**:
   - Iteratively checks all point pairs to determine if they form part of the convex hull.
   - Simple but computationally expensive with \(O(n^3)\) complexity.

2. **QuickHull Algorithm**:
   - Recursively divides points into upper and lower hulls based on their distances from partitioning lines.
   - Efficient \(O(n \log n)\) average complexity.

3. **Graphical Demonstration**:
   - Users can specify the number of points to generate.
   - Points and their computed convex hull are drawn on a canvas for visual validation.

4. **Empirical Analysis**:
   - Measures and compares the runtime of Brute Force and QuickHull for increasing dataset sizes.
   - Outputs results as runtime statistics.

## Usage

### 1. Graphical Demonstration
Run `main1DrawingDemo.py` to visualize the QuickHull algorithm:
- Specify the number of random points to generate.
- Observe the computed convex hull drawn on the canvas.

### 2. Runtime Comparison
Run `main2EmpiricalTesting.py` to compare the runtimes of Brute Force and QuickHull algorithms:
- Outputs runtime data for different input sizes.
- Demonstrates the efficiency of QuickHull over Brute Force as input size grows.

## Results

- **Accuracy**: Both algorithms correctly compute the convex hull for all tested datasets.
- **Efficiency**: QuickHull significantly outperforms Brute Force for larger datasets, as expected.
- **Visualization**: Graphical output provides intuitive validation of algorithm correctness.
