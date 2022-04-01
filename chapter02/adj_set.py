class AdjSet:
    def __init__(self, filename):
        self._filename = filename
        with open(filename, 'r') as f:
            lines = f.readlines()
        if not lines:
            raise ValueError('Expected something from input file!')

        # lines[0] -> V E
        self._V, self._E = (int(i) for i in lines[0].split())

        if self._V < 0:
            raise ValueError('V must be non-negative')

        if self._E < 0:
            raise ValueError('E must be non-negative')

        # size V list of set
        self._adj = [set() for _ in range(self._V)]
        for each_line in lines[1:]:
            a, b = (int(i) for i in each_line.split())
            self.validate_vertex(a)
            self.validate_vertex(b)

            if a == b:
                raise ValueError('Self-Loop is detected!')

            if b in self._adj[a]:
                raise ValueError('Parallel edges are detected!')

            self._adj[a].add(b)
            self._adj[b].add(a)

    @property
    def V(self):
        return self._V

    @property
    def E(self):
        return self._E

    def validate_vertex(self, v):
        if v < 0 or v >= self._V:
            raise ValueError('vertex ' + v + ' is invalid')

    def __str__(self):
        res = ['V = {}, E = {}'.format(self._V, self._E)]
        for v in range(self._V):
            res.append('{}: {}'.format(v, ' '.join(str(w) for w in self._adj[v])))
        return '\n'.join(res)

    def __repr__(self):
        return self.__str__()

    def __copy__(self):
        return AdjSet(self._filename)


if __name__ == '__main__':
    filename = 'g.txt'
    adj_set = AdjSet(filename)
    print(adj_set)