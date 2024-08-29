"""Cho số tự nhiên n (1 <= n <= 10^12), số tự nhiên k (1<=k<=10), 
k số nguyên tố khác nhau. Hãy đếm số các số tự nhiên nhỏ hơn hoặc bằng n 
và không chia hết cho bất cứ số nguyên tố nào trong k số."""


from itertools import combinations
from math import gcd
from functools import reduce

MOD = 10**9 + 7

def lcm(a, b):
    return a * b // gcd(a, b)

def count_integers_not_divisible(n, primes):
    k = len(primes)
    result = 0
    for i in range(1, k + 1):
        for comb in combinations(primes, i):
            l = reduce(lcm, comb, 1)
            if i % 2 == 1:
                result += n // l
            else:
                result -= n // l
    return n - result

def main():

    n = int(input("Nhập giá trị n (1 <= n <= 10^12): "))
    k = int(input("Nhập giá trị k (1 <= k <= 10): "))
    

    if not (1 <= k <= 10):
        print("Giá trị k phải nằm trong khoảng từ 1 đến 10.")
        return
    
    primes = list(map(int, input(f"Nhập {k} số nguyên tố khác nhau, cách nhau bởi dấu cách: ").split()))
    
    if len(primes) != k:
        print(f"Số lượng phần tử nhập vào không bằng k.")
        return
  
    result = count_integers_not_divisible(n, primes)
    print(f"Số lượng số không chia hết cho bất kỳ số nguyên tố nào là: {result}")

if __name__ == "__main__":
    main()
