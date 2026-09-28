def transpose(math: list[list[float | int]]):
    '''
    Возвращает транспонированную матрицу

    Args:
        math: list[list[float | int]]
    
    Returns:
        list[list]
    
    Raises:
        ValueError: если матрица рваная
        TypeError: Аргумент не является списком
    '''
    if type(math) != list:
            raise TypeError('Аргумент не является списком')
    if not mat_is_rect(math):
        raise ValueError('рваная матрица')
    m = []
    
    for y in range(len(math)):
        for x in range(len(math[0])):
            if y == 0:
                m.append([])
            m[x].append(math[y][x])
    return m

def row_sums(mat: list[list[float | int]]):
    '''
    Возвращает сумму каждой строки

    Args:
        mat: list[list[float | int]]
    
    Returns:
        list[float | int]
    
    Raises:
        ValueEror: если матрица рваная
        TypeError: Аргумент не является списком
    '''
    if type(mat) != list:
            raise TypeError('Аргумент не является списком')
    if not mat_is_rect(mat):
        raise ValueError('рваная матрица')
    res = []
    for y in range(len(mat)):
        res.append(0)
        for x in range(len(mat[y])):
            res[y]+=mat[y][x]
    return res

def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Возвращает сумму каждого столбца

    Args:
        mat: list[list[float | int]]
    
    Returns:
        list[float | int]
    
    Raises:
        ValueEror: если матрица рваная
        TypeError: Аргумент не является списком
    '''
    if type(mat) != list:
            raise TypeError('Аргумент не является списком')
    if not mat_is_rect(mat):
        raise ValueError('рваная матрица')
    res = []
    for y in range(len(mat)):
#        res.append(0)

        for x in range(len(mat[y])):
            if y == 0:
                res.append(0)
            res[x]+=mat[y][x]
    return res


def mat_is_rect(matrix: list[list]):
    '''
    проверяет, что матрица не рваная

    Args:
        matrix: list[list]
    
    Returns:
        list[list]
    
    Raises:
        ValueEror: если матрица рваная

    '''
    k = None
    for y in range(len(matrix)):
        if type(matrix[y]) != list:
            raise ValueError('Аргумент не является списком')
        if k is None:
            k =  len(matrix[y])
        if k != len(matrix[y]):
            return False

    return True



'''print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))'''

'''print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))'''


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
