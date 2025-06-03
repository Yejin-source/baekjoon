# N: 진법 수, B: 진법
N, B = input().split()
B = int(B)

# 진법 문자 목록
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0

# N을 뒤에서부터 반복
# enumerate로 자릿수(i)와 문자(ch)를 동시에 가져옴
for i, ch in enumerate(N[::-1]):
    # digits.index(ch): 문자를 숫자로 변환
    # B ** i: 자릿수에 따른 진법 거듭제곱
    result += B ** i * digits.index(ch)

print(result)


# enumerate
# 반복문에서 인덱스와 값을 동시에 꺼낼 수 있게 해주는 내장 함수


# 파이썬 내장 함수를 사용하는 방법
# int(N, B): 문자열 N을 B진수로 해석해 10진수로 변환

# N, B = input().split()
# print(int(N, int(B)))