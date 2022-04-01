class AdjMatrix:
    def __init__(self, filename):
        self._filename = filename
        with open(filename, 'r') as f:
            lines = f.readlines()
        if not lines:
            raise ValueError('Check your input file! Perhaps it is empty!')

        self._V, self._E = (int(i) for i in lines[0].split())

        if self._V < 0:
            raise ValueError('V must be non-negative')

        if self._E < 0:
            raise ValueError('E must be non-negative')

        self._adj = [[0] * self._V for _ in range(self._V)]
        for each_line in lines[1:]:
            a, b = (int(i) for i in each_line.split())
            self.validate_vertex(a)
            self.validate_vertex(b)
            if a == b:
                raise ValueError('Self-Loop is detected!')

            if self._adj[a][b] == 1:
                raise ValueError('Parallel edges are detected!')

            self._adj[a][b] = 1
            self._adj[b][a] = 1

    @property
    def V(self):
        return self._V

    @property
    def E(self):
        return self._E

    def has_degree(self, v, w):
        self.validate_vertex(v)
        self.validate_vertex(w)
        return self._adj[v][w] == 1

    def adj(self, v):
        self.validate_vertex(v)
        res = []
        for i in range(self._V):
            if self._adj[v][i] == 1:
                res.append(i)
        return res

    def degree(self, v):
        return len(self.adj(v))

    def remove_edge(self, v, w):
        self.validate_vertex(v)
        self.validate_vertex(w)
        if self._adj[v][w] == 1:
            self._adj[v][w] = 0
        if self._adj[w][v] == 1:
            self._adj[w][v] = 0

    def validate_vertex(self, v):
        if v < 0 or v >= self._V:
            raise ValueError('vertex ' + v + ' is invalid')

    def __str__(self):
        res = ['V = {}, E = {}'.format(self._V, self._E)]
        for i in range(self._V):
            each_line = ''
            for j in range(self._V):
                each_line += '{} '.format(self._adj[i][j])
            res.append(each_line)
        return '\n'.join(res)

    def __repr__(self):
        return self.__str__()

    def __copy__(self):
        return AdjMatrix(self._filename)

if __name__ == '__main__':
    filename = 'g.txt'
    adj_matrix = AdjMatrix(filename)
    print(adj_matrix)