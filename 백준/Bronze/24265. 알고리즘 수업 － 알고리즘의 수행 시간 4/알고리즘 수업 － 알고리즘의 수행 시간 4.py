n = int(input())
print(n*(n-1) // 2)  # 코드1 실행 횟수: n(n-1)/2
print(2)             # 시간 복잡도 O(n^2) -> 최고차항 차수 2


# 시간 초과로 실패한 코드

# 1단계: MenOfPassion 알고리즘을 파이썬으로 구현
# 코드1은 i < j 쌍의 개수만큼 반복
# def MenOfPassion(n):
#     count = 0
#     for i in range(n-1):
#         for j in range(i+1, n):
#             count = count + 1  # 코드1
#     return count

# 2단계: 출력
# n = int(input())
# print(MenOfPassion(n))  # 코드1 실행 횟수: count로 직접 계산
# print(2)                # 시간 복잡도: O(n^2) -> 최고차항의 차수: 2