from collections import defaultdict
import heapq

def distance(a, b):
    #real distance doesnt matter so using the squared distance
    dist = ((a[0] - b[0])**2) + ((a[1] - b[1])**2)
    return round(dist)

def reindex_connections(list):
    #Creating a dictionary from list for faster lookup time
    #This dictionary has all edges for a point and the distance between
    edges_dict = defaultdict(set)
    for edge in list:
        dist = distance(edge[0], edge[1])
        edges_dict[edge[0]].add((dist, edge[0], edge[1]))
        edges_dict[edge[1]].add((dist, edge[1], edge[0]))
    return edges_dict


def prims(edges):
    dict = reindex_connections(edges)
    starting_point = edges[0][0]

    connections = []
    reached_points = {starting_point}
    for conn in dict[starting_point]:
        heapq.heappush(connections, conn)
    
    culled_list = []
    while connections:
        next = heapq.heappop(connections)
        if next[2] in reached_points:
            pass
        else:
            reached_points.add(next[2])
            culled_list.append((next[1], next[2]))
            for conn in dict[next[2]]:
                heapq.heappush(connections, conn)

    return culled_list

