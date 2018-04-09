"""
Dijkstra's shortest path algorithm

Contact:
Ningchuan Xiao
The Ohio State University
Columbus, OH
"""

__author__ = "Ningchuan Xiao <ncxiao@gmail.com>"

# from network2listmatrix import *

def dijkstra(source, distmatrix):
    """
    Dijkstra's single source shortest path algorithm.
    Input
      source: index to source node
      distmatrix: distance matrix where cell (i, j) is INF
                  if nodes i and j are not on an edge,
                  otherwise the value is the weight/distance
                  of the edge
    Output
      dist: cumulative distance from source to each node
      prev: list of previous node for each node on the path
    """
    n = len(distmatrix)
    dist = [INF if i!=source else 0 for i in range(n)]
    prev = [None for i in range(n)]
    Q = list(range(n))
    while len(Q)>0:
        u = get_remove_min(Q, dist)
        U = get_neighbor(u, distmatrix, n)
        for v in U:
            newd = dist[u] + distmatrix[u][v]
            if newd < dist[v]:
                dist[v] = newd
                prev[v] = u
    return dist, prev

def get_remove_min(Q, dist):
    """
    Finds the node in Q with smallest distance in dist, and
    removes the node from Q.
    Input
      Q: a list of candidate nodes
      dist: a list of distances to each node from the source
    Output
      imin: index to the node with smallest distance
    """
    dmin = INF
    imin = -1
    for i in Q:
        if dist[i] < dmin:
            dmin = dist[i]
            imin = i
    Q.remove(imin)
    return imin

def get_neighbor(u, d, n):
    neighbors = [i for i in range(n)
                 if d[i][u]!=INF and i!=u]
    return neighbors

def shortest_path(source, destination, distmatrix):
    dist, prev = dijkstra(source, distmatrix)
    last = prev[destination]
    path = [destination]
    while last is not None:
        path.append(last)
        last = prev[last]
    return path, dist[destination]

if __name__ == "__main__":
    from network2listmatrix import *
    fname = '../data/network-links'
    a = network2distancematrix(fname, True)
    print(shortest_path(1, 6, a))
    print(shortest_path(0, 7, a))
