n = int(input())

a, b = 0, 1  # fib(0) = 0, fib(1) = 1

for _ in range(n):
    a, b = b, a + b  # 피보나치 수 갱신: (n번째, n+1번째)

# n번째 피보나치 수 출력
print(a)