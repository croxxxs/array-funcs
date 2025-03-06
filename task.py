def filter_greater(arr,value):
    new_arr = []
    value = int(input('enter value > '))
    for i in arr:
        if i < value:
            new_arr.append(i)
    print(new_arr)
    return new_arr

