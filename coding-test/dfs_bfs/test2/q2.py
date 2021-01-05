from dfs_bfs.test2.service import Service

if __name__ == '__main__':
    sv = Service()
    print(sv.adjacency_matrix())
    print(sv.adjacency_list())
    graph = sv.adjacency_matrix()
    dfs_visited = [False] * 9
    bfs_visited = [False] * 9
    print(sv.dfs(graph, 1, dfs_visited))
    print(sv.bfs(graph, 2, bfs_visited))