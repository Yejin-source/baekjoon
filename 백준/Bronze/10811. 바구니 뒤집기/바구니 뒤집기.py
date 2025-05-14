N, M = map(int, input().split())

# 바구니 초기화 (1번부터 N번까지 번호 설정)
basket = [i for i in range(1, N+1)]

# M번 반복
for _ in range(M):
    i, j = map(int, input().split())
    # i번부터 j번까지 바구니 슬라이싱 후 역순으로 바꾸기
    basket[i-1:j] = reversed(basket[i-1:j]) # 인덱스는 i-1부터 j-1까지
    
print(*basket) # 언패킹 연산자 사용


# reversed(리스트)
# 리스트를 역순으로 뒤집은 결과를 반환

# 언패킹 연산자
# print(*리스트)
# 리스트의 요소들을 공백으로 구분해 한 줄로 출력