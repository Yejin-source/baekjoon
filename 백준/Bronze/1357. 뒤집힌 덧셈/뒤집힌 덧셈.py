X, Y = input().split()  # 문자열

# 역순으로 만들어서 더하기
rev_sum = int(X[::-1]) + int(Y[::-1])

# 다시 역순으로 뒤집어서 출력
print(int(str(rev_sum)[::-1]))