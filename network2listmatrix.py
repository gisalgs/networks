"""
A couple of functions that convert a network file to a distance matrix or a list.

Contact:
Ningchuan Xiao
The Ohio State University
Columbus, OH
"""

__author__ = "Ningchuan Xiao <ncxiao@gmail.com>"

INF = float('inf')

def network2list(fname, is_zero_based = True):
    """
    Converts a network file to a list data structure.

    Input
      fname: name of a network file in the following format
             n
             i j distance
             ...
    Output
      network: a list of lists where the i-th element is the
               list of all nodes adjacent to node i
    """
    f = open(fname)
    l = f.readline()
    n = int(l.strip().split()[0])
    network = [[] for i in range(n)]
    for l in f:
        nodesnedge = l.strip().split()
        if len(nodesnedge)==3:
            i=int(nodesnedge[0])
            j=int(nodesnedge[1])
            if not is_zero_based:
                i = i-1
                j = j-1
            network[i].append(j)
            network[j].append(i)
    f.close()
    return network

def network2distancematrix(fname, is_zero_based = True):
    """
    Reads a list from the input graph file and returns
    the adjacent matrix. The input file has n+1 lines and
    must be in this format:

    n
    i j distance
    ...

    where the first line has the number of edges,
    and each of the remaining lines have the indices and
    distance on each edge. Indices start from 0 (default)
    or 1.
    """
    a = []
    f = open(fname)
    l = f.readline()
    n = int(l.strip().split()[0])   # number of nodes
    a=[[INF]*n for x in range(n)]  # init 2D list of INF
    for l in f:
        nodesnedge = l.strip().split()
        if len(nodesnedge)==3:
            i=int(nodesnedge[0])
            j=int(nodesnedge[1])
            if not is_zero_based:
                i = i-1
                j = j-1
            d=int(nodesnedge[2])
            a[i][j] = d
            a[j][i] = d
    for i in range(n):
        a[i][i] = 0
    return a
