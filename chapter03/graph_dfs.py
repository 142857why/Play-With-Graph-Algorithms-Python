# from chapter02.adj_list import AdjList as Graph
from chapter02.adj_set import AdjSet as Graph

class GraphDFS:
    def __init__(self, G, recursive=True):
        self._pre_order = []
        self._post_order = []
        self._G = G
        self._visited = [False] * G.V

        # 遍历所有的点，相当于遍历图中所有可能存在的联通块
        for v in range(G.V):
            if not self._visited[v]:
                if recursive:
                    self._dfs_recursive(v)
                else:
                    self._dfs_iteration(v)

    def _dfs_recursive(self, v):
        self._visited[v] = True
        self._pre_order.append(v)
        for w in self._G.adj(v):
            if not self._visited[w]:
                self._dfs_recursive(w)
        self._post_order.append(v)

    def _dfs_iteration(self, v):
        # 注意后序遍历是先遍历所有孩子(邻居)，再遍历自己
        # 故此引入tuple, (node, T/F), True 表示终于回到我自己了，可以放心加入后序了; False表示请继续visit children
        stack = [(v, False)]
        while stack:
            # print(stack) # 此处可以打印栈进行调试
            currNode, currIsVisited = stack.pop()
            if currIsVisited:
                self._post_order.append(currNode)
            elif not self._visited[currNode]:
                self._pre_order.append(currNode)
                self._visited[currNode] = True
                stack.append((currNode, True))
                neighbour_list = list(self._G.adj(currNode))[::-1] # [::-1] 是为了保持递归与非递归结果一致
                for w in neighbour_list:
                    stack.append((w, False))

    @property
    def pre_order(self):
        return self._pre_order

    @property
    def post_order(self):
        return self._post_order


if __name__ == '__main__':
    print('连通图，递归')
    filename = 'g1.txt'
    g = Graph(filename)
    # print(g)
    graphDFS = GraphDFS(g)
    print(graphDFS.pre_order)
    print(graphDFS.post_order)
    print('*' * 40)

    print('连通图，迭代')
    graphDFS = GraphDFS(g, recursive=False)
    print(graphDFS.pre_order)
    print(graphDFS.post_order)
    print('*' * 40)

    print('非连通图，递归')
    filename = 'g2.txt'
    g = Graph(filename)
    graphDFS = GraphDFS(g)
    print(graphDFS.pre_order)
    print(graphDFS.post_order)
    print('*' * 40)

    print('非连通图，迭代')
    graphDFS = GraphDFS(g, recursive=False)
    print(graphDFS.pre_order)
    print(graphDFS.post_order)
    print('*' * 40)

