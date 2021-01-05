class Service:
    def __init__(self, nm, *args):
        self.n, self.m = map(int, nm.split(" "))
        self.graph = []
        for i in range(self.n):
            self.graph.append(list(map(int, args[i])))

        print(self.graph)

    def ice_cream(self):
        result = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.dfs(i, j) == True:
                    result += 1
        return result

    def dfs(self, x, y):
        if x <= -1 or x >= self.n or y <= -1 or y >= self.m:
            return False

        if self.graph[x][y] == 0:
            self.graph[x][y] = 1
            self.dfs(x - 1, y)
            self.dfs(x, y - 1)
            self.dfs(x + 1, y)
            self.dfs(x, y + 1)
            return True

        return False
