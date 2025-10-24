'''Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.'''

# Each diagonal can be found by adding the row and column indices.
#      0 1 2 
#   [1,2,3]3 
#   [4,5,6]4
#   [7,8,9]

def findDiagonalOrder(mat):
    if not mat: return []
    row, col = len(mat), len(mat[0])
    result = []

    # for every diagonal on the Matrix 
    for diagonal in range(row + col -1): 
        temp = []
        
        # for every row
        for i in range(row): 
            # get the diagonal colum index
            j = diagonal - i 
            
            # check if the colum index is within the limits of the matrix
            if 0 <= j < col:
                temp.append(mat[j][i])
        
        # odd diagonals reverse ** optional
        """ if diagonal % 2 == 0:
            temp.reverse() """

        result.extend(temp)
    print(result)
    return result


mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
findDiagonalOrder(mat)