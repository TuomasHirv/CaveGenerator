"""Module for A* algorithm"""
import heapq
import math

def A_star(edge, measure, tile_map):
    """Implementation of A* algorithm"""
    length, width = measure
    weight = 10
    start = edge[0]
    end = edge[1]
    points = []
    route = [[None for _ in range(length)] for _ in range(width)]
    #Storing the route in an array for faster lookup
    route[start[0]][start[1]]=(-1,-1)
    g_scores = [[math.inf for _ in range(length)] for _ in range(width)]

    #(f_score, g_score, coordinates)
    #Switched from euclidian to manhattan distance because it is faster.
    #More information on reoptimization is in the optimization report.
    dist = abs(start[0] - end[0]) + abs(start[1] - end[0])
    heapq.heappush(points, (dist, 0, (start[0],start[1])))
    g_scores[start[0]][start[1]] = 0
    while points:
        current = heapq.heappop(points)
        x, y = current[2]
        if current[1] > g_scores[x][y]:
            continue
        if current[2] == end:
            break
        g_score = current[1]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),]:
            next_x, next_y = (x + dx, y + dy)
            if 0 <= next_x < width and 0 <= next_y < length:
                tile_val = tile_map[next_y][next_x]
                if tile_val < 1:
                    added_cost = tile_val + 0.5
                elif tile_val == 4:
                    added_cost = 0
                elif tile_val in (1, 2):
                    added_cost = 1
                else:
                    added_cost = 0.4
                n_weight = added_cost * weight

                new_g = g_score + 1 + n_weight

                if new_g < g_scores[next_x][next_y]:
                    g_scores[next_x][next_y] = new_g
                    f_score = new_g + abs(next_x - end[0]) + abs(next_y - end[1])
                    heapq.heappush(points, (f_score, new_g, (next_x, next_y)))

                    route[next_x][next_y]=(x, y)

    return route

def trace_route(route, end, start):
    """Trace a route from an array"""
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
    """Used to start A* for the application"""
    routes = []
    for edge in edges:
        tile_map = grid.tile_map
        measure = (length, width)
        array = A_star(edge, measure, tile_map)
        route = trace_route(array, edge[1], edge[0])
        routes.append(route)
        grid.carve_route(route)
    print("AMOUNT OF ROUTES: ", len(routes))
    return routes
