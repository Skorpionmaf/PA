
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        if self.matrix == other.matrix:
            return True
        else:
            return False

    def copy(self):
        return Matrix(self.matrix)

    def dim_row(self):
        return len( self.matrix )

    def dim_column(self):
        return len( self.matrix[0] )

    def dimension(self):
        return self.dim_row() * self.dim_column()

    def __add__(self, other):
        if self.dimension() == other.dimension():
            new_matrix = []
            for l in range(0, self.dim_row()):
                new_matrix.append( [] )
                for j in range(0, self.dim_column()):
                    new_matrix[i].append( self.matrix[i][j] + other.matrix[i][j] )

            return Matrix(new_matrix)
        else:
            raise Exception('The Matrix you want to add have different dimensions --> operation aborted')

    def __mul__(self, other):

        if isinstance(other, int):
            scalar = other
            new_matrix = []

            for i in range(0, self.dim_row()):
                new_matrix.append( [] )

                for j in range(0, self.dim_column()):
                    new_matrix[i].append( self.matrix[i][j] * scalar )

            return Matrix(new_matrix)

        elif isinstance(other, Matrix):
            if self.dim_column() == other.dim_row():
                new_matrix = []

                for i in range(0, self.dim_row()):
                    new_matrix.append( [] )

                    for j in range(0, other.dim_column()):
                        col = [ other.matrix[x][j] for x in range(0, other.dim_row()) ]
                        rig_col = list(zip(self.matrix[i], col))
                        new_matrix[i].append( sum([x*y for x,y in rig_col]) )

                return Matrix(new_matrix)

            else:
                raise Exception('The Matrixes you want to multiply have wrong dimension')

        else:
            raise Exception('Only multiplication by integer scalar or matrix is supported')

    def transposition(self):
        new_matrix = []
        for j in range(0, self.dim_column()):
            col = [ self.matrix[x][j] for x in range(0, self.dim_row()) ]
            new_matrix.append( col )

        return Matrix(new_matrix)

    def norm_1(self):
        sum_rows = []
        for j in range(0, self.dim_column()):
            col = [ abs(self.matrix[x][j]) for x in range(0, self.dim_row()) ]
            sum_rows.append( sum(col) )

        return max(sum_rows)

    def __repr__(self):

        return str(self.matrix)