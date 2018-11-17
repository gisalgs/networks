def dfs(network, v):
    """
    Depth-first search

    Input
      network     A network represented using a list of lists
                    The i-th list contains the adjacent nodes for node i
      v           Initial node to start search
    Output
      V           A list of nodes visited
    """
    n = len(network)
    S = [] # empty stack
    S.append(v)
    V = []
    labelled = [ False for i in range(n)]
    labelled[v] = True
    while len(S) > 0:
        t = S.pop()
        V.append(t)
        for u in network[t]:
            if not labelled[u]:
                labelled[u] = True
                S.append(u)
    return V

if __name__ == "__main__":
    from network2listmatrix import network2list
    network = network2list('../data/network-links')
    V = dfs(network, 3)
    print("Visited:", V)
