"""Cho số tự nhiên n (1 <= n <= 10^6). 
Hãy tính số cách lắc xúc xắc 6 mặt có tổng các mặt của mỗi lần xắc bằng 𝑛. 
Kết quả lấy dư của phép chia cho 10^9+7
"""

MOD = 10**9 + 7
MAX_N = 10**6

n = int(input())

def dice_rolls(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        for j in range(1, 7):
            if i >= j:
                ways[i] = (ways[i] + ways[i - j]) % MOD
    return ways[n]
def slove(n):
    if 1 <= n <= MAX_N:
        return dice_rolls(n)
    else:
        return "Giá trị của n không thỏa mãn điều kiện 1 <= n <= 10^6"
print(slove(n))