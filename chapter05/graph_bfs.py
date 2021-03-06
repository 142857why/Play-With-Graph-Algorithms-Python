from collections import deque
from chapter02.adj_set import AdjSet as Graph

class GraphBFS:

    def __init__(self, G):
        self._G = G
        self._visited = [False] * G.V
        self._order = []

        for v in range(G.V):
            if not self._visited[v]:
                self._bfs(v)

    def _bfs(self, s):
        q = deque()
        q.append(s)
        self._visited[s] = True

        while q:
            v = q.popleft()
            self._order.append(v)
            for w in self._G.adj(v):
                if not self._visited[w]:
                    q.append(w)
                    self._visited[w] = True

    def order(self):
        return self._order


if __name__ == '__main__':
    filename = 'g1.txt'
    g = Graph(filename)
    graph_bfs = GraphBFS(g)
    print('BFS order : {}'.format(graph_bfs.order()))