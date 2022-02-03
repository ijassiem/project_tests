# MathFunctions.py
import math

def areaCircle(radius):
    area = math.pi*radius**2
    return area

def areaSquare(length):
    area = length*length
    return area

def areaTriangle(length, height):
    area = 0.5*length*height
    return area

def volumeCube(length, width, height):
    volume = length*width*height
    return volume
