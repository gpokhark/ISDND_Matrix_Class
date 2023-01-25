import math
from math import sqrt
import numbers

from copy import deepcopy

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def minor(matrix,r=0,c=0): 
    minor = deepcopy(matrix)
    del minor[r]
    #delete row r
    for b in range(len(minor)):
        #Delete column c
        del minor[b][c]
    return minor

def recursive_det(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    else:
        determinant = 0
        for i in range(len(matrix)):
            determinant += matrix[0][i] * (-1)**(2+i) * recursive_det(minor(matrix,0,i))
        return determinant
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    
        
    
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise ValueError('Cannot calculate determinant of non-square matrix.')
        if self.h > 2:
            raise NotImplementedError ('Calculating determinant not implemented for matrices largerer than 2x2.')
        
        # TODO - your code here
        # If size is 1
        #if self.h == 1:
        #    determinant = self.g[0][0]
        #else:
            # if size is 2
        #    determinant = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        #determinant = recursive_det(self.g)
        return recursive_det(self.g)

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise ValueError ('Cannot calculate the trace of a non-square matrix.')
            return 0
        # TODO - your code here
        trace = 0
        for i in range(len(self.g)):
            trace = trace + self.g[i][i]
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise ValueError ('Non-square Matrix does not have an inverse.')
            return 0
        if self.h > 2:
            raise NotImplementedError ('inversion not implemented for matrices larger than 2x2.')
            return 0

        # TODO - your code here
        det = self.determinant()
        # If size is 1
        if self.h == 1:
            inverse = [[1/det]]
        else:
            # if size is 2
            inverse = [
                [ self.g[1][1]/det , -self.g[0][1]/det],
                [-self.g[1][0]/det ,  self.g[0][0]/det]
            ]
        return Matrix(inverse)
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        # Seperate columns into rows and then append rows to T
        # works from any matric not just square
        T = []
        for i in range(len(self.g[0])):
            row = []
            for j in range(len(self.g)):
                row.append(self.g[j][i])
            T.append(row)
        return Matrix(T) 

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if (self.h != other.h) or (self.w != other.w):
            raise ValueError('Matrices can only be added if the dimensions are the same')
            return 0
        #   
        # TODO - your code here
        #
        # First add elementwise and create a row and later append each row to the final matrix
        mat_add = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[0])):
                row.append(self.g[i][j]+other.g[i][j])
            mat_add.append(row)
        return Matrix(mat_add)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        # First multiply -1 elementwise and create a row and later append each row to the final matrix
        mat_neg = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[0])):
                row.append(self.g[i][j]*-1)
            mat_neg.append(row)
        return Matrix(mat_neg)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if (self.h != other.h) or (self.w != other.w):
            raise ValueError('Matrices can only be subracted if the dimensions are the same')
            return 0
        #   
        # TODO - your code here
        #
        # First subtract elementwise and create a row and later append each row to the final matrix
        mat_sub = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[0])):
                row.append(self.g[i][j]-other.g[i][j])
            mat_sub.append(row)
        return Matrix(mat_sub)
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if (self.w!=other.h):
            raise ValueError('Matrices can only be multiplied if the dimensions are the same')
            return 0
        MatA = self.g
        MatB = other.g
        Obj_MatB_T = other.T()
       
        
        MatB_T = Obj_MatB_T.g
        
        mat_mul = []
        for i in range(len(MatA)):
            rowA = MatA[i]
            
            row_mul = []
            for j in range(len(MatB_T)):
                rowB = MatB_T[j]
                sum_row = 0
                for k in range(len(MatB_T[0])):
                    sum_row = sum_row + rowA[k]*rowB[k]
                row_mul.append(sum_row)
            mat_mul.append(row_mul)
        return Matrix(mat_mul)
                
    
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            # First multiply elementwise and create a row and later append each row to the final matrix
            mat_sub = []
            for i in range(len(self.g)):
                row = []
                for j in range(len(self.g[0])):
                    row.append(self.g[i][j]*other)
                mat_sub.append(row)
            return Matrix(mat_sub)
            