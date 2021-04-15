#Tính tổng từ 1 - n
def tinh_tong(n):
    if n == 0:
        return 0
    return n + tinh_tong(n - 1)

#tinh giai thua
def giai_thua(n):
    if n == 1:
        return 1
    return n * giai_thua(n - 1)

#tinh fibonaci
def tinh_fibonaci(n):
    if ((n == 1) | (n == 2)):
        return 1
    return tinh_fibonaci(n -1) + tinh_fibonaci(n - 2)     

n = int(input("Nhap n > 0 : "))
tong = tinh_tong(n)
giai_thua = giai_thua(n)
fibonaci = tinh_fibonaci(n)

print("Tong = ", tong)
print(n,"! = ", giai_thua)
print("Tong cua day fibonaci = ", fibonaci)