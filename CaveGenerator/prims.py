"""Implementation for prims algorithm"""
from collections import defaultdict
import heapq
import random
def distance(a, b):
    """Calculates the relative distance of 2 points"""
    dist = ((a[0] - b[0])**2) + ((a[1] - b[1])**2)
    return round(dist)

def reindex_connections(edges_list):
    """Indexes connections to a list"""
    #Creating a dictionary from list for faster lookup time
    #This dictionary has all edges for a point and the distance between
    edges_dict = defaultdict(set)
    for edge in edges_list:
        dist = distance(edge[0], edge[1])
        edges_dict[edge[0]].add((dist, edge[0], edge[1]))
        edges_dict[edge[1]].add((dist, edge[1], edge[0]))
    return edges_dict


def prims(edges):
    """Culls Edges favoring shortest ones"""
    e_dict = reindex_connections(edges)
    starting_point = edges[0][0]

    connections = []
    reached_points = {starting_point}
    for conn in e_dict[starting_point]:
        heapq.heappush(connections, conn)

    culled_list = []

    extra_connections = []
    while connections:
        e_next = heapq.heappop(connections)
        if e_next[2] in reached_points:
            if random.randint(0, 12) == 12:
                extra_connections.append((e_next[1], e_next[2]))
        else:
            reached_points.add(e_next[2])
            culled_list.append((e_next[1], e_next[2]))
            for conn in e_dict[e_next[2]]:
                heapq.heappush(connections, conn)
    culled_list.extend(extra_connections)
    return culled_list
