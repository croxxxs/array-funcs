value = int(input('enter value > '))

arr = [1,2,3,4,7,12,32,42]

def filter_less(arr,value):
    new_arr = []
    
    for i in arr:
        if i < value:
            new_arr.append(i)
    print(new_arr)
    return new_arr

def filter_greater(arr,value):
    new_arr = []
    
    for i in arr:
        if i > value:
            new_arr.append(i)
    print(new_arr)
    return new_arr

def filter_equal(arr,value):
    new_arr = []
    
    for i in arr:
        if i == value:
            new_arr.append(i)
    print(new_arr)
    return new_arr

def filter_not_equal(arr,value):
    new_arr = []
    
    for i in arr:
        if i != value:
            new_arr.append(i)
    print(new_arr)
    return new_arr

def test_funcs():
    print(f'filter equal results: {filter_equal(arr,value)}')
    print(f'filter not equal results: {filter_not_equal(arr,value)}')
    print(f'filter greater results: {filter_greater(arr,value)}')
    print(f'filter greater results: {filter_less(arr,value)}')


print(f'proves about true result of my work: {test_funcs()}')


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

def mtr_lefttrsumm(matrix):
    summ_triangle = 0

    for row in range(len(matrix)):
        for i in range(len(row)):
            if row == 0 and i == 1 or row == 0 and i == 2 or row == 1 and i == 2:
                summ_triangle.append(matrix[i],[i])
    for i in matrix:
        summ_triangle += i
    print(summ_triangle)
    return summ_triangle

print(mtr_lefttrsumm(matrix))