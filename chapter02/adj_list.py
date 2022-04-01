class AdjList:

    def __init__(self, filename:str):
        lines = None
        with open(filename, 'r') as f:
            lines = f.readlines()
        if not lines:
            raise ValueError('Check your input file! Perhaps it is empty!')

        # lines[0] -> V, E
        # 从第一行中读取顶点数和边数
        self._V, self._E = (int(i) for i in lines[0].split())

        if self._V < 0: raise ValueError('V must be non-negative')
        if self._E < 0: raise ValueError('E must be non-negative')

        self._adj = [[] for _ in range(self._V)]
        for each_line in lines[1:]:
            a, b = (int(i) for i in each_line.split())
            self._validate_vertex(a)
            self._validate_vertex(b)

            if a == b:
                raise ValueError('self-loop is detected!')

            if self._adj[a].count(b):
                raise ValueError('Parallel edges are detected!')

            self._adj[a].append(b)
            self._adj[b].append(a)


    @property
    def V(self):
        return self._V

    @property
    def E(self):
        return self._E

    def _validate_vertex(self, v):
        if v < 0 or v >= self._V:
            raise ValueError('vertex ' + v + ' is invalid')

    def __str__(self):
        res = ['V = {}, E = {}'.format(self._V, self._E)]
        for v in range(self._V):
            res.append('{}: {}'.format(v, ' '.join(str(w) for w in self._adj[v])))

        return '\n'.join(res)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    filename = 'g.txt'
    adj_list = AdjList(filename=filename)
    print(adj_list)