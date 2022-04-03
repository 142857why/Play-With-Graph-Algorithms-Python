from collections import deque
from chapter02.adj_set import AdjSet as Graph


class CycleDetection:

    def __init__(self, G):
        self._G = G
        self._visited = [False] * G.V

        self._pre = [-1] * G.V
        self._has_cycle = False

        for v in range(G.V):
            if not self._visited[v]:
                if self._bfs(v):
                    self._has_cycle = True
                    break

    def _bfs(self, s):
        q = deque()
        q.append(s)
        self._visited[s] = True
        self._pre[s] = s

        while q:
            curr = q.popleft()
            for w in self._G.adj(curr):
                if not self._visited[w]:
                    q.append(w)
                    self._visited[w] = True
                    self._pre[w] = curr
                    # 如果w已经被访问过了，我们还必须判断，w不是curr的上一个节点
                    # 正常情况下curr应该是w的上一个节点
                    # 即pre[w] = curr
                    # 只能curr指向w
                    # 不能w指向curr，如果发生了就是有环
                elif self._pre[curr] != w:
                    return True

        return False

    @property
    def has_cycle(self):
        return self._has_cycle


if __name__ == '__main__':
    g = Graph('g1.txt')
    cycle_detection = CycleDetection(g)
    print('Does this graph has cycle? : {}'.format(cycle_detection.has_cycle))

    g = Graph('g2.txt')
    # print(g)
    cycle_detection = CycleDetection(g)
    print('Does this graph has cycle? : {}'.format(cycle_detection.has_cycle))