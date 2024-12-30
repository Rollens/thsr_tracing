import math
from haversine import haversine_distance, euclidean_distance

def read_route_file(filepath):
    # 讀取路徑檔案，並將其轉換為經緯度的列表
    with open(filepath, 'r') as file:
        line = file.readline().strip()
    route_list = [(float(coords.split()[0]), float(coords.split()[1])) for coords in line.split(',')]
    return route_list

def read_station_file(filepath):
    # 讀取車站檔案，並將其轉換為車站名稱和經緯度的字典
    with open(filepath, 'r') as file:
        lines = file.readlines()
    stations = {}
    for line in lines:
        parts = line.strip().split(',')
        station_name = parts[0]
        coordinates = (float(parts[1]), float(parts[2]))
        stations[station_name] = coordinates
    return stations

def find_closest_route_point(route_list, target):
    # 找到距離目標座標最近的路徑點
    closest_point = min(route_list, key=lambda point: euclidean_distance(point, target))
    return closest_point

def find_closest_station(route_list, stations, target):
    # 找到距離目標座標最近的車站
    start = route_list.index(target)
    distance_north = 0
    distance_south = 0
    for i in range(start, len(route_list)-1):
        if route_list[i] in stations.values():
            closest_station_south = route_list[i]
            break
        distance_south += haversine_distance(route_list[i], route_list[i+1])
    for i in range(start, 0, -1):
        if route_list[i] in stations.values():
            closest_station_north = route_list[i]
            break
        distance_north += haversine_distance(route_list[i], route_list[i-1])
    print("Distace to north {:.2f}, to south {:.2f}".format(distance_north, distance_south))
    if distance_north < distance_south:
        closest_station = (list(stations.keys())[list(stations.values()).index(closest_station_north)], closest_station_north)
    else:
        closest_station = (list(stations.keys())[list(stations.values()).index(closest_station_south)], closest_station_south)
    return closest_station

if __name__ == "__main__":
    route_filepath = 'route.txt'
    station_filepath = 'station_points.txt'
    
    # 讀取路徑和車站資料
    route_list = read_route_file(route_filepath)
    stations = read_station_file(station_filepath)
    
    # 接收使用者輸入的座標
    user_input = input("請輸入座標 (格式: 經度,緯度): ")
    target_coordinates = find_closest_route_point(route_list, tuple(map(float, user_input.split(','))))
    print(f"Closest point to {user_input} is {target_coordinates}")

    # 找到最近的車站
    closest_station = find_closest_station(route_list, stations, target_coordinates)
    
    print(f"Closest station to {target_coordinates} is {closest_station[0]} with coordinates {closest_station[1]}")

