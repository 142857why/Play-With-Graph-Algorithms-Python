from chapter02.adj_set import AdjSet as Graph


class CycleDetection:

    def __init__(self, G):
        self._G = G
        self._visited = [False] * G.V
        self._has_cycle = False

        for v in range(G.V):
            if not self._visited[v]:
                self._dfs_recursive(v, v)

    def _dfs_recursive(self, v, parent):
        self._visited[v] = True
        for w in self._G.adj(v):
            if not self._visited[w]:
                if self._dfs_recursive(w, v):
                    return True

            elif w != parent:
                self._has_cycle = True
                return True

        return False

    @property
    def has_cycle(self):
        return self._has_cycle


if __name__ == '__main__':
    filename = 'g3.txt'
    g = Graph(filename)

    # cd is short for cycle_detection
    cd = CycleDetection(g)
    print(cd.has_cycle)

    