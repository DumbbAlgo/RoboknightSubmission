import sys

def shortest_path(graph, N, source):
    MAX_INT = 10**9
    distance = [MAX_INT]*N
    distance[source] = 0
    strval = [""]*N
    strval[source]=str(source)
    visited = []
    while len(visited)<N:
        maxval = MAX_INT
        u = 0
        for i in range(N):
            if i not in visited:
                maxval = min(maxval, distance[i])
                if maxval==distance[i]:
                    u = i
        visited.append(u)
        l = graph[u]
        for i in range(len(l)):
            if l[i]>0:
                if distance[i] > distance[u]+l[i]:
                    distance[i] = distance[u]+l[i]
                    strval[i]=strval[u]+str(i)


    return distance, strval


graph = [[0, 2, 1, 4, 0, 0, 0, 0],
        [0, 0, 5, 0, 10, 2, 0, 0],
        [9, 0, 0, 0, 11, 0, 0, 0],   
        [0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 3, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0]]


print(shortest_path(graph, 8, 0))