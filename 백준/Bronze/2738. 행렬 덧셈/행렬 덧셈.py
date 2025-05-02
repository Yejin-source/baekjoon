# N: 행의 개수, M: 열의 개수
N, M = map(int, input().split())

A = []  # 빈 리스트 생성
for i in range(N):
    # 한 줄씩 M개의 리스트로 만든 후 A에 추가
    A.append(list(map(int, input().split())))

B = []  # 빈 리스트 생성
for i in range(N):
    # 한 줄씩 M개의 정수를 입력받아 리스트로 만든 후 B에 추가
    B.append(list(map(int, input().split())))
    
# 두 행렬의 같은 위치의 원소끼리 더하고 출력
for i in range(N):  # 각 행 반복
    for j in range(M):  # 각 열 반복
        # A와 B의 i행 j열 원소를 더한 값 출력
        print(A[i][j] + B[i][j], end=' ')
    print()  # 한 행마다 줄 바꿈