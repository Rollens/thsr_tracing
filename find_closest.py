import math

def find_closest_point(route_list, target):
    def distance(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    
    closest_point = min(route_list, key=lambda point: distance(point, target))
    return closest_point
