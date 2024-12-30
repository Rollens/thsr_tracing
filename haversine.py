import math

def haversine_distance(point1, point2):
    # 哈弗辛公式計算兩點之間的距離
    R = 6371  # 地球半徑，單位為公里
    lat1, lon1 = point1
    lat2, lon2 = point2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)  # 修正經度差計算
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def euclidean_distance(point1,point2):
    x1, y1= point1
    x2, y2= point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_closest_point(route_list, target):
    closest_point = min(route_list, key=lambda point: haversine_distance(point, target))
    return closest_point
