def create_matrix(order):

    
    matrix = [0 for i in range(size)]
    c = 0
    for i in range(order):
        for j in range(order):
            index = (i+1, j+1)
            element = int(input(f"Enter element at index {index}: "))
            matrix[c] = (element)
            c += 1
    return matrix


def display_matrix(matrix):

   
    width = 0
    for i in matrix:
        if len(str(i)) > width:
            width = len(str(i))
    size = len(matrix)
    side = int(size ** 0.5)
    if side != size ** 0.5:
        print("Please input a square matrix.")
        return
    start = 0
    end = side
    for i in range(side):
        print("|", end = " ")
        for j in matrix[start:end]:
            print(str(j).zfill(width), end = " ")
        start += side
        end += side
        print("|")





def add_matrices(matrix1, matrix2):

    """Adds two square matrices (of the same order) and returns the resultant matrix"""

    if len(matrix1) != len(matrix2):
        return "Please input two square matrices of the same order"
    else:
        resultant = matrix1[:]
        for i in range(len(matrix2)):
            resultant[i] += matrix2[i]
    return resultant

def sub_matrices(matrix1, matrix2):

    """Adds two square matrices (of the same order) and returns the resultant matrix"""

    if len(matrix1) != len(matrix2):
        return "Please input two square matrices of the same order"
    else:
        resultant = matrix1[:]
        for i in range(len(matrix2)):
            resultant[i] -= matrix2[i]
    return resultant





def multiply_matrices(matrix1, matrix2):

    """Returns the product of the multiplication of two square matrices (Returns matrix1 X matrix2)"""

    sowry = "Sorry, matrix multiplication is currently only supported for square matrices of the same order"
    if len(matrix1) != len(matrix2):  # Not of same order
        return sowry
    size = len(matrix1)
    if size**0.5 != int(size**0.5):  # Not square matrices
        return sowry
    resultant = [0 for x in range(size)]
    L = [(0, 0), (0, 1), (0, 2), (3, 0), (3, 1), (3, 2), (6, 0), (6, 1), (6, 2)]
    for i in range(size):
        resultant[i] = (matrix1[L[i][0]] * matrix2[L[i][1]]) + (matrix1[L[i][0]+1] * matrix2[L[i][1]+3]) + (matrix1[L[i][0]+2] * matrix2[L[i][1]+6])
    return resultant



a = [x for x in range(9)]
b = [-x for x in range(9)]
display_matrix(a)
display_matrix(b)
display_matrix(multiply_matrices(a, b))
display_matrix(add_matrices(a, b))
display_matrix(sub_matrices(a, b))