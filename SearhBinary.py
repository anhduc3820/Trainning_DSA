def SearchBinary(list, item):
    low = 0
    hight = int(len(list) - 1)
    while low <= hight:
        mid = int((low + hight) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            hight = int(mid - 1)
        else:
            low = int(mid + 1)
    return None
mylist = [1, 2, 3, 4, 5, 6, 7]
print(SearchBinary(mylist, 3))
