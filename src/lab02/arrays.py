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

def unique_sorted(nums: list[float | int]):
    '''
    Возвращает отсортированный список уникальных значений

    Args:
        nums: list[float | int] 
    
    Returns:
        list[float | int]
    '''
    unq = []
    for e in nums:
        if e not in unq:
            unq.append(e)

    for i in range(len(unq)-1):
        for j in range(i+1,len(unq)):
            if unq[j] < unq[i]:
                buf = unq[i]
                unq[i] = unq[j]
                unq[j] = buf
    return unq

def flatten(mat: list[list | tuple]):
    '''
    Возвращает "расплющенный" список списков

    Args:
        mat: list[list | tuple]
    
    Returns:
        list

    Raises:
        TypeError: если элемент не является списком/кортежем
    '''
    if type(mat) != list:
        raise TypeError('Аргумент не является списком')
    
    res = []
    for el in mat:
        if type(el) not in (list,tuple):
            raise TypeError('Элемент не является списком/кортежем')
        for e in el:
            res.append(e)
    return res
#    print(type(mat))


'''
print(min_max([1, 2, 3, 4, 5.987, 0,]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
'''
'''
print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))
'''

print(flatten([[1,2],[3,4]]))
print(flatten([[1,2],(3,4,5)]))
print(flatten([[1],[],[2,3]]))
print(flatten([[1,2],'ab']))