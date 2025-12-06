# N: 정수 개수, M: 나머지 기준
N, M = map(int, input().split())
nums = list(map(int, input().split()))

result = 1

for n in nums:
    # N개의 정수의 곱을 M으로 나눈 나머지
    result = (result * n) % M

print(result)