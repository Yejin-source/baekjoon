# 거꾸로 읽은 숫자
A, B = input().split()

# 숫자 원래대로 뒤집기
A_rev = int(A[::-1])
B_rev = int(B[::-1])

# 더 큰 수 출력
print(max(A_rev, B_rev))