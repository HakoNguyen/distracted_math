""" Cho 2 số tự nhiên n và k (0 <= k <= n <= 10^9). 
Hãy tính số cấu hình chỉnh hợp lặp chập k của n, 
kết quả lấy phần dư của phép chia cho 10^9+7 """


MOD = 10**9 + 7
k,n = map(int, input().split())

def luy_thua(base, exp, MOD):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % MOD
        base = (base * base) % MOD
        exp //= 2
    return result

def chinh_hop_lap(n, k):
    if 0 <= k <= n <= 10**9:
        return luy_thua(n, k, MOD)
    else:
        return "Giá trị của n và k không thỏa mãn điều kiện 0 <= k <= n <= 10^9"
print(chinh_hop_lap(n, k))