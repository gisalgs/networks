def bfs(network, v):
    """
    Breadth-first search

    Input
      network     A network represented using a list of lists
                    The i-th list contains the adjacent nodes for node i
      v           Initial node to start search
    Output
      V           A list of nodes visited
    """
    n = len(network)
    Q = []
    Q.append(v)
    V = []
    labeled = [ False for i in range(n)]
    labeled[v] = True
    while len(Q) > 0:
        # print list(Q)
        t = Q.pop(0)
        V.append(t)
        for u in network[t]:
            if not labeled[u]:
                labeled[u] = True
                Q.append(u)
    return V

if __name__ == "__main__":
    from network2listmatrix import network2list
    network = network2list('../data/network-links')
    V = bfs(network, 3)
    print("Visited:", V)
