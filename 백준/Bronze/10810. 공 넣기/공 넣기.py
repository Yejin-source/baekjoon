# N: 바구니 개수, M: 공을 넣는 횟수
N, M = map(int, input().split())

# 바구니 리스트 (리스트의 크기를 만들기 위해 0으로 초기화)
basket = [0] * (N+1) # 1번부터 N번까지


# M번 반복
for _ in range(M):
    i, j, k = map(int, input().split())
    # i번부터 j번까지 반복
    for x in range(i, j+1):
        basket[x] = k # 바구니 x번에 k번 공 넣기 (덮어쓰기)

# 1번부터 출력
print(*basket[1:]) # 언패킹 연산자


# 언패킹 연산자
# print(*리스트)
# 리스트의 요소들을 공백으로 구분해 한 줄로 출력