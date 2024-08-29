"""Cho 2 số tự nhiên n và k (0 <= k <= n <= 100). 
Hãy tính số cấu hình tổ hợp chập k của n, 
kết quả lấy phần dư của phép chia cho 10^9+7"""

MOD = 10**9 + 7
MAX_N = 100 

k, n = map(int, input().split())

giai_thua = [1] * (MAX_N + 1)
giai_thua_nghich_dao = [1] * (MAX_N + 1)

def facts():
    for i in range(2, MAX_N + 1):
        giai_thua[i] = giai_thua[i-1] * i % MOD
    giai_thua_nghich_dao[MAX_N] = pow(giai_thua[MAX_N], MOD-2, MOD)
    for i in range(MAX_N-1, 0, -1):
        giai_thua_nghich_dao[i] = giai_thua_nghich_dao[i+1] * (i+1) % MOD

def to_hop(n, k):
    if 0 <= k <= n <= MAX_N:
        return giai_thua[n] * giai_thua_nghich_dao[k] * giai_thua_nghich_dao[n-k] % MOD
    else:
        return "Giá trị của n và k không thỏa mãn điều kiện 0 <= k <= n <= 100"
facts()

print(to_hop(n, k))