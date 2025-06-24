# 1단계: MenOfPassion 알고리즘 파이썬 변환
# A의 모든 쌍 (i, j)에 대해 A[i] * A[j]를 더함
# def MenOfPassion(A, n):
#     sum = 0
#     A = [0] + A  # 인덱스를 1부터 쓰기 위해 0 추가
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             sum = sum + A[i] * A[j]  # 코드1
#     return sum
    
# 2단계: 코드1의 실행 횟수
# 이중 for문 -> 총 n^2회 실행
# 시간 복잡도: O(n^2) -> 최고차항의 차수: 2

# 3단계: 출력
n = int(input())
print(n*n)  # 코드1 실행 횟수 (n^2)
print(2)    # 시간 복잡도의 최고차항 차수