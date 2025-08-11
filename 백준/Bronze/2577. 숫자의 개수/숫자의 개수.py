# 세 개의 자연수
A = int(input())
B = int(input())
C = int(input())

# 곱셈 결과를 문자열로 변환
result = str(A * B * C)

# 각 숫자(0~9)의 등장 횟수 출력
for digit in range(10):
    print(result.count(str(digit)))