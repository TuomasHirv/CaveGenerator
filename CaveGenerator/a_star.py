import heapq
import numpy as np


points = []

def distance(a, b):
    #real distance does matter now as it has to comapare to g_score
    dist = np.sqrt(((a[0] - b[0])**2) + ((a[1] - b[1])**2))
    return dist



def A_star(start, end, length, width):
    
    points = []
    route = [[None for _ in range(width)] for _ in range(length)]
    #Storing the route in an array for faster lookup
    route[start[0]][start[1]]=(-1,-1)
    #(f_score, g_score, coordinates)
    heapq.heappush(points, (distance(start, end), 0, (start[0],start[1])))
    def add_to_heap(point, end, g_score):
        if point[0]+1 < length:
            if route[point[0]+1][point[1]] == None:
                heapq.heappush(points, (distance((point[0]+1,point[1]), end) + g_score, g_score, (point[0]+1,point[1])))
                route[point[0]+1][point[1]]=(point[0], point[1])

        if point[0]-1 >= 0:
            if route[point[0]-1][point[1]] == None:
                heapq.heappush(points, (distance((point[0]-1,point[1]), end) + g_score, g_score, (point[0]-1,point[1])))
                route[point[0]-1][point[1]]=(point[0], point[1])

        if point[1]+1 < width:
            if route[point[0]][point[1]+1] == None:
                heapq.heappush(points, (distance((point[0],point[1]+1), end) + g_score, g_score, (point[0],point[1]+1)))
                route[point[0]][point[1]+1]=(point[0], point[1])

        if point[1]-1 >= 0:
            if route[point[0]][point[1]-1] == None:
                heapq.heappush(points, (distance((point[0],point[1]-1), end) + g_score, g_score, (point[0],point[1]-1)))
                route[point[0]][point[1]-1]=(point[0], point[1])

    while points:
        next = heapq.heappop(points)
        if next[2] == end:
            break
        add_to_heap(next[2], end, next[1])
    
    return trace_route(route, end, start)

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
        routes.append(A_star(edge[0], edge[1], length, width))
    return routes
