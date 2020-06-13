import math

def solve(x1, y1, z1, x2, y2, z2):
    if x1 == x2 and (x1 == 10 or x1 == 0):
        return findArcLength(y1, z1, y2, z2)
    elif y1 == y2 and (y1 == 10 or y1 == 0):
        return findArcLength(x1, z1, x2, z2)
    elif z1 == z2 and (z1 == 10 or z1 == 0):
        return findArcLength(x1, y1, x2, y2)

    return getShortestDistance(x1, y1, z1, x2, y2, z2)    


def getIntermediatePoint(x1, y1, z1, x2, y2, z2):
    x3, y3 , z3 = x1, y1, z1
    if x2 == 0 or x2 == 10:
        x3 = x2
    elif y2 ==0 or y2 == 10:
        y3 = y2 
    else:
        z3 = z2
    return x3, y3, z3


        

def getShortestDistance(x1, y1, z1, x2, y2, z2):
    distance = 0     

    x3, y3 ,z3 = getIntermediatePoint(x1, y1, z1, x2, y2, z2)

    # Calculate distance from first coordinate to intermediate point.
    distance = getDistance3(x1, y1, z1, x3, y3, z3)

    # Calculate distance from intermedaite point to second coordinate.
    distance += getDistance3(x3, y3, z3, x2, y2, z2) 

    return float(format(distance, '0.2f'))

def findArcLength(x1, y1, x2, y2):
    # s=r*Theta
    r = findRadius(x1, y1, x2, y2)
    theta = math.pi / 3
    return float(format(r * theta, '0.2f'))

def findRadius(x1, y1, x2, y2):
    # For CASE-1, we can ignore one of the coordinate
    line_distance = getDistance(x1, y1, x2, y2) / 2
    rad60 = math.pi / 3
    c60 = math.cos(rad60)
    return line_distance / c60


def getDistance(x1, y1, x2, y2):
    p1 = math.pow(x2 - x1, 2)
    p2 = math.pow(y2 - y1, 2)
    return math.sqrt(p1 + p2)

def getDistance3(x1, y1, z1, x2, y2, z2):
    p1 = math.pow(x2 - x1, 2)
    p2 = math.pow(y2 - y1, 2)
    p3 = math.pow(z2 - z1, 2)
    return math.sqrt(p1 + p2 + p3)



def main():
    num_points = int(input()) 
    c_pool = [ int(x) for x in input().split(",")] 
    distance = 0
    x1, y1, z1 = c_pool[0], c_pool[1], c_pool[2]
    d_temp = 0
    for i in range(3, 3 * num_points, 3):
        x2, y2, z2 = c_pool[i], c_pool[i+1], c_pool[i+2]
        print(f"Currently examining ({x1},{y1},{z1}) and ({x2},{y2},{z2})")
        distance += solve(x1, y1, z1, x2, y2, z2)
        print(f"\t distance = {distance - d_temp}")
        d_temp = distance
        x1, y1, z1 = x2, y2, z2
    print(distance)

if __name__ == "__main__":
    main()