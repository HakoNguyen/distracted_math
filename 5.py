"""Cho số tự nhiên n, m (1 <= n, m <= 100), 
dãy Y1, Y2, ..., Yn (Y1 + Y2 + ... + Yn <= n) . 
Hãy đếm số nghiệm của phương trình X1+X2+...+Xn =m sao cho Xi >= Yi. 
Kết quả lấy dư của phép chia cho 10^9+7"""

MOD = 10**9 + 7
MAX_N = 100

def initialize_factorials_and_inverses(max_n, mod):
    factorials = [1] * (max_n + 1)
    inv_factorials = [1] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        factorials[i] = factorials[i-1] * i % mod
    
    inv_factorials[max_n] = pow(factorials[max_n], mod - 2, mod)  # Nghịch đảo của giai thừa của MAX_N
    for i in range(max_n - 1, 0, -1):
        inv_factorials[i] = inv_factorials[i + 1] * (i + 1) % mod
    
    return factorials, inv_factorials

def comb(n, k, fact, inv_fact, mod):
    if k > n or k < 0:
        return 0
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

def count_solutions(n, m, Y, fact, inv_fact, mod):
    total = sum(Y)
    if m < total:
        return 0
    m -= total
    return comb(n + m - 1, n - 1, fact, inv_fact, mod)

def solve(n, m, Y):
    if not (1 <= n <= MAX_N and 1 <= m <= MAX_N and all(1 <= y <= n for y in Y)):
        print("Giá trị của n, m và Y không thỏa mãn điều kiện 1 <= n, m <= 100 và 1 <= Yi <= n")
        return
    
    if len(Y) != n:
        print("Số lượng phần tử trong Y không bằng n")
        return
    
    if sum(Y) > m:
        print("Tổng các phần tử trong Y lớn hơn m")
        return
    
    factorials, inv_factorials = initialize_factorials_and_inverses(n + m - 1, MOD)
    result = count_solutions(n, m, Y, factorials, inv_factorials, MOD)
    print(result)

if __name__ == "__main__":

    n = int(input("Nhập giá trị n (1 <= n <= 100): "))
    m = int(input("Nhập giá trị m (1 <= m <= 100): "))
    

    Y = list(map(int, input(f"Nhập dãy Y (độ dài {n} với tổng các phần tử <= m): ").split()))
    
    solve(n, m, Y)
