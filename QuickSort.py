def quick_sort_1(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] #trục là điểm đầu
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort_1(less) + [pivot] + quick_sort_1(greater)

def quick_sort_2(array):
    if len(array) < 2:
        return array
    else:
        n = len(array) - 1
        pivot = array[n] #trục là điểm cuối
        less = [i for i in array[0:n] if i <= pivot]
        greater = [i for i in array[0:n] if i > pivot]
        return quick_sort_2(less) + [pivot] + quick_sort_2(greater)

array = [10, 5, 2, 3, 6, 8]
print(quick_sort_1(array)) #trục là điểm đầu
print(quick_sort_2(array)) #trục là điểm cuối