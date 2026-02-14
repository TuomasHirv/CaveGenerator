import heapq
import numpy as np


points = []

def distance(a, b):
    #real distance does matter now as it has to comapared to g_score
    dist = np.sqrt(((a[0] - b[0])**2) + ((a[1] - b[1])**2))
    return dist



def A_star(start, end, length, width):
    
    points = []
    route = [[None for _ in range(length)] for _ in range(width)]
    #Storing the route in an array for faster lookup
    route[start[0]][start[1]]=(-1,-1)
    #(f_score, g_score, coordinates)
    heapq.heappush(points, (distance(start, end), 0, (start[0],start[1])))
    def add_to_heap(point, end, g_score):
        x, y = point
        if x+1 < width:
            if route[x+1][y] == None:
                heapq.heappush(points, (distance((x+1,y), end) + g_score, g_score, (x+1,y)))
                route[x+1][y]=(x, y)

        if x-1 >= 0:
            if route[x-1][y] == None:
                heapq.heappush(points, (distance((x-1,y), end) + g_score, g_score, (x-1,y)))
                route[x-1][y]=(x, y)

        if y+1 < length:
            if route[x][y+1] == None:
                heapq.heappush(points, (distance((x,y+1), end) + g_score, g_score, (x,y+1)))
                route[x][y+1]=(x, y)

        if y-1 >= 0:
            if route[x][y-1] == None:
                heapq.heappush(points, (distance((x,y-1), end) + g_score, g_score, (x,y-1)))
                route[x][y-1]=(x, y)

    while points:
        next = heapq.heappop(points)
        if next[2] == end:
            break
        add_to_heap(next[2], end, next[1])
    
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



def starter(edges, length, width):
    routes = []
    for edge in edges:
        map = (A_star(edge[0], edge[1], length, width))
        routes.append(trace_route(map, edge[1], edge[0]))
    return routes
