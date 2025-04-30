import sys

# input 대신 사용하는 sys.stdin.readline
T = int(sys.stdin.readline()) # 문자열 형태이기 때문에 형변환 필요

for i in range(T):
    A, B = map(int, sys.stdin.readline().split()) # 입출력 더 빠르게 처리 가능
    print(A+B)


# 맨 끝의 개행문자(\n)까지 입력받기 때문에
# 문자열을 저장하고 싶을 경우 .rstrip()을 해 주는 것이 좋음