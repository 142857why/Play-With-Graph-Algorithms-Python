from chapter02.adj_set import AdjSet as Graph


class BipartiteDetection:

    def __init__(self, G):
        self._G = G
        self._visited = [False] * G.V
        # -1 means not colored yet, should be either 0 or 1
        self._colors = [-1] * G.V
        self._is_bipartite = True
        for v in range(G.V):
            if not self._visited[v]:
                # if v is not visited
                # means we are entering a new connected component!!
                # so it doesn't matter to color it as 0 or 1
                if self._dfs_recursive(v, 0) is False:
                    self._is_bipartite = False
                    break

    def _dfs_recursive(self, v, color):
        self._visited[v] = True
        self._colors[v] = color
        for w in self._G.adj(v):
            if not self._visited[w]:
                if not self._dfs_recursive(w, 1 - color):
                    # 试图对当前节点的附近邻居染不同的颜色，却不能成功
                    return False
            elif self._colors[w] == self._colors[v]:
                # 访问过（但是是由其他节点访问的），当时给出的染色可能和现在节点v的颜色相同，也是失败的
                return False

        # 目前看下来还没有矛盾
        return True

    @property
    def is_bipartite(self):
        return self._is_bipartite

    # @property
    # def colors(self):
    #     return self._colors


if __name__ == '__main__':
    filename = 'g2.txt'
    g = Graph(filename)
    # bd stands for bipartite_detection
    bd = BipartiteDetection(g)
    print(bd.is_bipartite)
