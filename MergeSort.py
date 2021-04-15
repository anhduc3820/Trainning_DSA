
def mergeSort(arr):
    if len(arr) > 1:
        # Tìm chỉ số giữa mảng
        mid = len(arr)//2
        # Phân chia các phần tử mảng thành 2 nữa
        L = arr[:mid]
        R = arr[mid:]
        # Phân loại lần một
        mergeSort(L)
        # Phân loại lần hai
        mergeSort(R)
 
        i = j = k = 0
 
        # Sao chép dữ liệu vào mảng tạm thời L L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Kiểm tra xem có phần tử nào còn lại không
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 

arr = [12, 11, 13, 5, 6, 7]
print("Given array is\n")
printList(arr)
mergeSort(arr)
print("Sorted array is: \n")
printList(arr)
 