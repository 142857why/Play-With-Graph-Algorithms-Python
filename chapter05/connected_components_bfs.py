from collections import deque
from chapter02.adj_set import AdjSet as Graph


class CC:

    def __init__(self, G):
        self._G = G
        self._visited = [-1] * G.V
        self._ccount = 0

        for v in range(G.V):
            if self._visited[v] == -1:
                self._bfs(v, v)
                self._ccount += 1


    def _bfs(self, s, group):
        q = deque()
        q.append(s)
        self._visited[s] = group

        while q:
            v = q.popleft()
            for w in self._G.adj(v):
                if self._visited[w] == -1:
                    q.append(w)
                    self._visited[w] = group

    @property
    def ccount(self):
        return self._ccount


if __name__ == '__main__':
    filename = 'g1.txt'
    g = Graph(filename)
    cc = CC(g)
    print('Number of connected components : {}'.format(cc.ccount))
