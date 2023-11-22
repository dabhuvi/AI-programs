import math

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def nearest_neighbor(graph, start_city):
    unvisited_cities = set(graph.keys())
    current_city = start_city
    tour = [current_city]

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: graph[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    tour.append(start_city)
    return tour

def total_distance(tour, graph):
    distance = 0
    for i in range(len(tour) - 1):
        distance += graph[tour[i]][tour[i + 1]]
    return distance

def tsp_nearest_neighbor(cities):
    graph = {}
    for i, city1 in enumerate(cities):
        graph[city1] = {}
        for j, city2 in enumerate(cities):
            if i != j:
                graph[city1][city2] = euclidean_distance(city1, city2)

    start_city = cities[0]
    tour = nearest_neighbor(graph, start_city)
    distance = total_distance(tour, graph)

    return tour, distance

if __name__ == "__main__":
    cities = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

    tour, distance = tsp_nearest_neighbor(cities)

    print("Tour:", tour)
    print("Total Distance:", distance)
