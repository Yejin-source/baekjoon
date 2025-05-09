# 총 금액
X = int(input())

# 구매한 물건 종류의 수
N = int(input())


# 금액 저장할 변수 초기화
total = 0

# N번 반복 (a: 물건의 가격, b: 개수)
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b

# 총 금액 비교
if X == total:
    print('Yes')
else:
    print('No')