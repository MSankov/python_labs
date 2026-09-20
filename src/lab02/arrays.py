def min_max(nums: list[float | int]): 
    '''
    Возвращает кортеж (минимум, максимум) массива

    Args:
        nums: list[float | int] 
    
    Returns:
        Кортеж: tuple[float | int, float | int]
    
    Raises:
        ValueEror: если список пуст

    '''
    if not nums:
        raise ValueError('Список не может быть пуст')

    res_min = None
    res_max = None
    for e in nums:
        if res_min == None or e < res_min:
            res_min = e
        if res_max == None or e > res_max:
            res_max = e
    return (res_min, res_max)
        

print(min_max([1,2,3,4,5.987,0,]))
print(min_max([]))

