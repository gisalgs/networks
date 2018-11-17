def dfs(network, v):
    """
    Depth-first search
    Input
      network: a network represented using a list of lists
      v: initial node to start search
    Output
      V: a list of nodes visited
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
