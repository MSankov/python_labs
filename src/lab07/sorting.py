def bubble_sort(nums):
    """Новый список, отсортированный по возрастанию. Исходный не меняется.
 
    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    m = list(nums)
    for i in range(len(m) - 1):
        swapped = False
        for j in range(len(m) - 1 - i):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
                swapped = True
        if not swapped:
            break
    return m
'''
print(bubble_sort([3, 1, 2]))
print(bubble_sort([2, 2, 1]))
print(bubble_sort([]))'''

 
def insertion_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    m = list(nums)
    for i in range(1, len(m)):
        key = m[i]
        j = i - 1
        while j >= 0 and m[j] > key:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = key
    return m

'''print(insertion_sort([3, 1, 2]))
print(insertion_sort([2, 2, 1]))
print(insertion_sort([]))'''
 
def selection_sort(nums):
    """Тот же контракт, что у bubble_sort."""
    arr = list(nums)
    n = len(arr)
    for i in range(n - 1):
        min_id = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_id]:
                min_id = j
        if min_id != i:
            arr[i], arr[min_id] = arr[min_id], arr[i]
    return arr

'''print(selection_sort([3, 1, 2]))
print(selection_sort([2, 2, 1]))
print(selection_sort([]))'''
 