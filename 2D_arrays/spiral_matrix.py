""" Given an m x n matrix, return all elements of the matrix in spiral order. """

def spiralOrder(mat):
    top, left = 0, 0
    bottom, right = len(mat) - 1, len(mat[0]) - 1
    result = []
    # while we are withing the matrix limits
    while top <= bottom and left <= right:
        temp = []
        # go trough all elements in the row
        for i in range(right + 1):
            temp.append(mat[top][i])
            print(temp)
        top += 1

        # go trough all elements in the col
        for i in range(bottom):
            temp.append(mat[i][right])
            print(temp)
        right -= 1

        if top <= bottom:
            for i in range(bottom, top - 1, -1):
                temp.append(mat[bottom][i])
                print(i)
            bottom -= 1
        
        if left <= right:
            for i in range(right, left - 1, -1):
                temp.append(mat[i][right])
                print(i)
        
        result.extend(temp)
        
        print("------")
        print(result)
        # row outbounds -1 
        # go trough all elemtns in the colum 
        # colum outbounds -1 


    


matrix = [[1,2,3],[4,5,6],[7,8,9]]
spiralOrder(matrix)