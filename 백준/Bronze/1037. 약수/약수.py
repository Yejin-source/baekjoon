# N의 진짜 약수의 개수
divisor_count = int(input())  # 사용하지 않음

# N의 진짜 약수 목록
divisors = list(map(int, input().split()))

# 오름차순 정렬
divisors.sort()

# N = 가장 작은 약수 × 가장 큰 약수
print(divisors[0] * divisors[-1])


# 다른 풀이 (정렬 없이)
# print(max(divisors) * min(divisors))