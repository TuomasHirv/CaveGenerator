import heapq
import numpy as np


points = []

def distance(a, b):
    #real distance does matter now as it has to comapared to g_score
    dist = np.sqrt(((a[0] - b[0])**2) + ((a[1] - b[1])**2))
    return dist



def A_star(start, end, length, width, grid):
    weight = 10
    points = []
    route = [[None for _ in range(length)] for _ in range(width)]

    #Storing the route in an array for faster lookup
    route[start[0]][start[1]]=(-1,-1)
    f_scores = [[None for _ in range(length)] for _ in range(width)]

    #(f_score, g_score, coordinates)
    heapq.heappush(points, (distance(start, end), 0, (start[0],start[1])))
    f_scores[start[0]][start[1]] = distance(start, end)

    def add_to_heap(point, end, g_score):
        x, y = point
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),]:
            next_x, next_y = (x + dx, y + dy)
            if 0 <= next_x < width and 0 <= next_y < length:

                if route[next_x][next_y] == None or f_scores[next_x][next_y] > distance((next_x,next_y), end) + g_score:
                    n_weight = grid.check_for_weigth(next_y, next_x) * weight
                    heapq.heappush(points, (distance((next_x,next_y), end) + g_score + n_weight, g_score + n_weight, (next_x, next_y)))
                    f_scores[next_x][next_y] = distance((next_x,next_y), end) + g_score
                    route[next_x][next_y]=(x, y)

    while points:
        next = heapq.heappop(points)
        if next[2] == end:
            break
        add_to_heap(next[2], end, next[1] + 1)
    
    return route

def trace_route(route, end, start):
    path = []
    if route[end[0]][end[1]] is not None:
        
        current = end
        while current != (-1, -1):
            path.append(current)
            current = route[current[0]][current[1]]
    
        path.append(start)
    else:
        print("COULDNT FIND PATH FOR ROUTE: ", start, "to", end)
        return None
    return path



def starter(edges, length, width, grid):
    routes = []
    for edge in edges:
        map = (A_star(edge[0], edge[1], length, width, grid))
        route = trace_route(map, edge[1], edge[0])
        routes.append(route)
        grid.carve_route(route)
    print("AMOUNT OF ROUTES: ", len(routes))
    return routes
