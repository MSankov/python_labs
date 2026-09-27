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
        if k is None:
            k =  len(matrix[y])
        if k != len(matrix[y]):
            raise ValueError('рваная матрица')
        