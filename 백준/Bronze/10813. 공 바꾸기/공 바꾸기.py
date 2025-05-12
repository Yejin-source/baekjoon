# N: 바구니 개수, M: 공을 바꿀 횟수
N, M = map(int, input().split())

# 바구니 초기화 (각 바구니에 자기 번호 공 넣기)
basket = [i for i in range(N+1)] # 인덱스 0번은 사용하지 않음


# M번 반복
for _ in range(M):
    i, j = map(int, input().split())
    # i번과 j번 바구니의 공을 교환
    basket[i], basket[j] = basket[j], basket[i]

# 1번부터 출력
print(*basket[1:]) # 언패킹 연산자 사용


# 값 교환
# 파이썬에서는 두 변수의 값을 동시에 교환 가능
# ex. a, b = b, a