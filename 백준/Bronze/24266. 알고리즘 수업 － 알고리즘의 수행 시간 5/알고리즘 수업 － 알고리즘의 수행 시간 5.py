# 1단계: MenOfPassion 알고리즘을 파이썬으로 구현
# def MenOfPassion(A, n):
#     sum = 0
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 sum += A[i] * A[j] * A[k]  # 코드1
#     return sum

# 2단계: 코드1의 실행 횟수
# 3중 반복문 -> n * n * n = n^3회 실행
# 시간 복잡도: O(n^3) -> 최고차항의 차수: 3

# 3단계: 출력
n = int(input())
print(n ** 3)  # 코드1 실행 횟수 (n^3)
print(3)       # 시간 복잡도의 최고차항 차수