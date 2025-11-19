by, bm, bd = map(int, input().split())  # 생년월일
y, m, d = map(int, input().split())     # 기준 날짜

# 만 나이
if m > bm or (m == bm and d >= bd):
    print(y - by)
else:
    print(y - by - 1)

# 세는 나이
print(y - by + 1)

# 연 나이
print(y - by)