from collections import deque
from chapter02.adj_set import AdjSet as Graph


class BipartiteDetection:

    def __init__(self, G):
        self._G = G
        self._colors = [-1] * G.V
        self._is_bipartite = True

        for v in range(G.V):
            if self._colors[v] == -1:
                if not self._bfs(v):
                    self._is_bipartite = False
                    break

    def _bfs(self, s):
        q = deque()
        q.append(s)
        self._colors[s] = 0

        while q:
            v = q.popleft()
            for w in self._G.adj(v):
                if self._colors[w] == -1:
                    q.append(w)
                    self._colors[w] = 1 - self._colors[v]
                    # 如果下一个点w的颜色是当前处理点的颜色
                    # 说明不能对其染色了
                    # 即说明当前的图不是二分图
                elif self._colors[w] == self._colors[v]:
                    return False

        # 能顺利完成当前的染色
        return True

    def is_bipartite(self):
        return self._is_bipartite


if __name__ == '__main__':
    g = Graph('g1.txt')
    bi_partition_detection = BipartiteDetection(g)
    print('Is this a bi-partition graph? : {}'.format(
        bi_partition_detection.is_bipartite()),
    )