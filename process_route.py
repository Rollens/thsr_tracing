import math
from find_closest import find_closest_point

def read_route_file(filepath):
    with open(filepath, 'r') as file:
        line = file.readline().strip()
    route_list = [(float(coords.split()[0]), float(coords.split()[1])) for coords in line.split(',')]
    return route_list

def read_station_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    stations = {}
    for line in lines:
        parts = line.strip().split(',')
        station_name = parts[1]
        coordinates = (float(parts[2]), float(parts[3]))
        stations[station_name] = coordinates
    return stations

def save_station_points(filepath, station_points):
    with open(filepath, 'w') as file:
        for station_name, point in station_points.items():
            file.write(f"{station_name},{point[0]},{point[1]}\n")

if __name__ == "__main__":
    route_filepath = '/Users/rollens/code/pilotdemo/route.txt'
    station_filepath = '/Users/rollens/code/pilotdemo/station.txt'
    output_filepath = '/Users/rollens/code/pilotdemo/station_points.txt'
    
    route_list = read_route_file(route_filepath)
    stations = read_station_file(station_filepath)
    
    station_points = {}
    for station_name, coordinates in stations.items():
        closest_point = find_closest_point(route_list, coordinates)
        station_points[station_name] = closest_point
    
    save_station_points(output_filepath, station_points)
    print(f"Station points saved to {output_filepath}")
