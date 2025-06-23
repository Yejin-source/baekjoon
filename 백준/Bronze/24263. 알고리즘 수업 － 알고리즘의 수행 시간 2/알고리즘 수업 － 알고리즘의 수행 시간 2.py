# 1단계: MenOfPassion 알고리즘을 파이썬 코드로 바꿔보기
# 리스트 A의 요소 n개를 모두 더하는 함수
# def MenOfPassion(A, n):  # def 함수이름(매개변수): 함수를 정의(define)
#     total = 0
#     for i in range(1, n+1):
#         total += A[i]  # 코드1
#     return total

# 2단계: 코드1의 실행 횟수 파악
# -> for문은 n번 반복됨 -> 수행 횟수: n회
# -> 시간 복잡도: O(n) -> 최고차항의 차수: 1

# 3단계: 출력
n = int(input())
print(n)  # 코드1이 n번 실행됨
print(1)  # O(n)의 최고차항 차수는 1