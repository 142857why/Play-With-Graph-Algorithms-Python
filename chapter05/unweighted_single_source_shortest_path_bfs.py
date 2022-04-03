from collections import deque
from chapter02.adj_set import AdjSet as Graph

class UnweightedSingleSourceShortestPath:

    def __init__(self, G, s):
        self._G = G
        self._s = s
        self._visited = [False] * G.V
        self._pre = [-1] * G.V
        self._dis = [-1] * G.V

        self._bfs(s)
        print("初始化后，节点{}到达各点的最短路径:".format(s), ', '.join(str(i) for i in self._dis))

    def _bfs(self, s):
        q = deque()
        q.append(s)
        self._visited[s] = True

        self._pre[s] = s
        self._dis[s] = 0

        while q:
            v = q.popleft()
            for w in self._G.adj(v):
                if not self._visited[w]:
                    q.append(w)
                    self._visited[w] = True

                    self._pre[w] = v
                    self._dis[w] = self._dis[v] + 1

    def is_connected_to(self, t):
        self._G.validate_vertex(t)
        # 如果在初始化BFS以后t被访问过，说明t和s是相通的
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

    def dis(self, t):
        """某个点t到s的steps"""
        self._G.validate_vertex(t)
        return self._dis[t]


if __name__ == '__main__':
    filename = 'g1.txt'
    g = Graph(filename)
    sspath = UnweightedSingleSourceShortestPath(g, 0)
    print('0 -> 6 : {}'.format(sspath.path(6)))
    print(sspath.dis(6))