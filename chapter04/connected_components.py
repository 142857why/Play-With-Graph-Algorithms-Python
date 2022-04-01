from chapter02.adj_set import AdjSet as Graph

class CC:
    def __init__(self, G, recursive=True):
        self._G = G
        self._visited = [-1] * G.V
        self._ccount = 0

        # if self._G.is_directed:
        #     raise ValueError('CC only works in undirected graph')

        for v in range(G.V):
            if self._visited[v] == -1:
                if recursive:
                    self._dfs_recursive(v, self._ccount)
                else:
                    self._dfs_iteration(v, self._ccount)
                self._ccount += 1

    def _dfs_recursive(self, v, ccid):
        self._visited[v] = ccid
        for w in self._G.adj(v):
            if self._visited[w] == -1:
                self._dfs_recursive(w, ccid)

    def _dfs_iteration(self, v, ccid):
        stack = [v]
        while stack:
            curr = stack.pop()
            if self._visited[curr] == -1:
                self._visited[curr] = 0
            neighbour_list = list(self._G.adj(curr))[::-1]  # [::-1] 是为了保持递归与非递归结果一致
            for w in neighbour_list:
                if self._visited[w] == -1:
                    stack.append(w)
                    self._visited[w] = ccid

    @property
    def ccount(self):
        return self._ccount

    def is_connected(self, v, w):
        self._G.validate_vertex(v)
        self._G.validate_vertex(w)
        return self._visited[v] == self._visited[w]

    @property
    def groups(self):
        res = [[] for _ in range(self._ccount)]
        for v in range(self._G.V):
            res[self._visited[v]].append(v)
        return res

if __name__ == '__main__':
    filename = 'g4.txt'
    g = Graph(filename)
    cc = CC(g)
    print(cc.ccount)
    print(cc.groups)
