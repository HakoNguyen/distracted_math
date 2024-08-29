"""Cho số tự nhiên n (1 <= n <= 10^6). 
Hãy tính số mất thứ tự D(n), kết quả lấy dư của phép chia cho 10^9+7"""

MOD = 10**9 + 7
MAX_N = 10**6

n = int(input())

def mat_thu_tu(n):
    D = [0] * (n + 1)
    D[1] = 0
    if n > 1:
        D[2] = 1
    for i in range(3, n + 1):
        D[i] = (i - 1) * (D[i-1] + D[i-2]) % MOD
    return D[n]
def slove(n):
    if 1 <= n <= MAX_N:
        return mat_thu_tu(n)
    else:
        return "Giá trị của n không thỏa mãn điều kiện 1 <= n <= 10^6"
print(slove(n))