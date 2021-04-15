#hàm hoán vị 
def Swap(a, b, list):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp

#selection sort, Sắp xếp theo thứ tự từ bé đến lớn
def SelectionSort(list):
    n = len(list)
    for i in range(int(n)):
        index_min = i
        for j in range(i + 1, int(n)):
            if list[index_min] > list[j]:
                index_min = j
        Swap(i, index_min, list)

#print Array
def PrintArray(list, n):
    for i in range(n):
        print(list[i])

list = [1, 5, 4, 7, 3, 9, 0]
n = len(list)
SelectionSort(list)
print("array")
PrintArray(list, n)
