"""
All pair distance

Contact:
Ningchuan Xiao
The Ohio State University
Columbus, OH
"""

__author__ = "Ningchuan Xiao <ncxiao@gmail.com>"

def allpairs(a):
    """
    Returns the weight/distance matrix for all pair
    shortest path using the Floyd-Warshall algorithm.

    Input
      a: initial distance matrix where weights for
         non-adjacent pairs are infinity

    Output
      The function directly changes the values in the input
    """
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if a[i][j] > a[i][k]+a[k][j]:
                    a[i][j] = a[i][k]+a[k][j]

if __name__ == "__main__":
    from network2listmatrix import network2distancematrix
    fname = '../data/network-links'
    a = network2distancematrix(fname, True)
    allpairs(a)
    print(a[1][6])
    print(a[0][7])
