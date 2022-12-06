from _point import Point

import math
import matplotlib.pyplot as plt
import random

class Sierpinski:
    def __init__(self, edges):
        self.edges = edges
    
    def __init__(self, sideSize):
        height = (sideSize*math.sqrt(3))/2
        self.edges = [Point(0, 0), Point(sideSize/2, height), Point(sideSize, 0)]

    def generatePoints(self, iterations=1000):
        self.__plotPoints = self.edges.copy()
        for _ in range(iterations):
            randomPoint = random.choice(self.__plotPoints)
            randomEdge = random.choice(self.edges)
            self.__plotPoints.append(randomPoint.midPoint(randomEdge))

    def plot(self, markerSize=0.5):
        x, y = list(zip(*[(point.x, point.y) for point in self.__plotPoints]))
        plt.plot(x, y, "ro", markersize=markerSize)
        plt.show()
