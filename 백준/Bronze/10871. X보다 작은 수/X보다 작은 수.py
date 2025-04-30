N, X = map(int, input().split())

A = list(map(int, input().split()))  # map 객체를 리스트로 변환

for i in range(N):
    if A[i] < X:  # A[i]가 x보다 작다면
        print(A[i], end=" ")  # 작은따옴표도 가능
        

# end 파라미터: 출력 후 맨 끝에 붙이는 문자를 정하는 옵션

# print()는 자동으로 줄바꿈(/n)을 추가함
# end를 바꾸면 원하는 대로 출력 가능