from chapter02.adj_set import AdjSet as Graph


class SingleSourcePath:
    def __init__(self, G, s, recursive=True):
        G.validate_vertex(s)
        self._G = G
        self._s = s
        self._visited = [False] * G.V
        self._pre = [-1] * G.V

        if recursive:
            self._dfs_recursive(s, s)
        else:
            self._dfs_iteration(s, s)
        pass

    def _dfs_recursive(self, v, parent):
        self._visited[v] = True
        self._pre[v] = parent
        for w in self._G.adj(v):
            if not self._visited[w]:
                # current node v as parent, continuous searching the path
                self._dfs_recursive(w, v)

    ## This is actually like BFS ?
    def _dfs_iteration(self, v, parent):
        stack = [(v, parent)]
        while stack:
            # print(stack)
            curr, currParent = stack.pop()
            if not self._visited[curr]:
                self._pre[curr] = currParent

                self._visited[curr] = True
            neighbour_list = list(self._G.adj(curr))[::-1] # [::-1] 是为了保持递归与非递归结果一致
            for w in neighbour_list:
                if not self._visited[w]:
                    stack.append((w, curr))

    def is_connected_to(self, t):
        # 在初始化后s才会调用该函数，因此直接返回t是否被访问即可知道与s相连与否
        self._G.validate_vertex(t)
        return self._visited[t]

    def path(self, t):
        res = []
        if not self.is_connected_to(t):
            return res

        curr = t
        while curr != self._s:
            res.append(curr)
            curr = self._pre[curr]

        res.append(self._s)
        return res[::-1]

    @property
    def pre(self):
        return self._pre


if __name__ == '__main__':
    filename = 'g1.txt'
    g = Graph(filename)
    # print(g)

    # ssp stands for single_source_path
    ssp = SingleSourcePath(g, 0, recursive=True)
    print('0 -> 6: ' + str(ssp.path(6)))  # 0 -> 1 -> 3 -> 2 -> 6
    print(ssp.pre)

    ssp = SingleSourcePath(g, 0, recursive=False)
    print('0 -> 6: ' + str(ssp.path(6)))
    print(ssp.pre)
