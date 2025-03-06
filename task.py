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