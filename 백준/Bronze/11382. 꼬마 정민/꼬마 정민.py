# input() 함수로 입력받은 후
# split() 함수로 나누어서 각 변수에 저장
A, B, C = input().split()

# 각 입력값을 정수형으로 변환
A = int(A) 
B = int(B) 
C = int(C)

# 세 정수의 합 출력
print(A+B+C)


# 다른 풀이
# map 함수 사용 -> 입력받을 때부터 자료형 변환 가능
# map(각 요소에 적용할 함수, 반복 가능한 자료형형)

# A, B, C = map(int, input().split())
# print(A+B+C)