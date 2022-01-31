import numpy

def line_function_creation(p1,p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    slope = y2 - y1/ (x2 -x1)
    offset = y2 - (slope * y1)
    return (x3 * slope) + offset

