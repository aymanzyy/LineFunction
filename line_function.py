def line_function_creation(p1,p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    slope = (y2 - y1)/(x2 -x1)
    print(slope)
    offset = y2 - (slope * y1)
    print(offset)
    if y3 == (x3 * slope) + offset:
        return True
    else: 
        return False

#if __name__ == "__main__":
#    answer = line_function_creation((2,4), (4,8), 6)
#    print(answer)