num = int(input())
num2 = input()

# 문자열 슬라이싱 후 정수로 변환
a = int(num2[2:3])  # 일의 자리
b = int(num2[1:2])  # 십의 자리
c = int(num2[0:1])  # 백의 자리

print(num * a)
print(num * b)
print(num * c)
print(num * int(num2))


# 슬라이싱
# 시퀀스 자료형(문자열, 리스트 등)에서 특정 범위를 잘라내는 것

# 시퀀스[start:end:step]
# 끝 인덱스는 포함되지 않음


# 다른 풀이 | 나머지 연산 활용
# A = int(input())
# B = int(input())

# print(A * (B % 10))        # 일의 자리
# print(A * (B // 10 % 10))  # 십의 자리
# print(A * (B // 100))      # 백의 자리
# print(A * B)

# // : 정수 나눗셈 (몫)
# / : 실수 나눗셈